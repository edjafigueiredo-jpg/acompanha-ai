#!/usr/bin/env python3
"""
Gera um arquivo .ics com as calls de entrevista, pronto para importar no
Google Agenda (Configuracoes > Importar e exportar > Importar).

Resolve o "colocar no calendario" sem precisar de acesso a sua conta.

USO
    1. cp calls.exemplo.csv calls.local.csv
    2. preencha calls.local.csv com as calls reais
    3. python3 gerar-ics.py
    4. importe entrevistas.ics no Google Agenda

calls.local.csv e entrevistas.ics estao no .gitignore: dado de prospect nao
entra neste repositorio, que e publico.

Cada evento ja vem com dois lembretes:
    - 1 dia antes  -> disparo da mensagem de confirmacao (corta no-show)
    - 15 min antes -> abrir o roteiro 03-roteiro-entrevista.md
"""

import csv
import os
import sys
from datetime import datetime, timedelta, timezone

ENTRADA = "calls.local.csv"
SAIDA = "entrevistas.ics"

# Fuso do seu consultorio. Brasilia/SP = -3 (sem horario de verao desde 2019).
# Manaus = -4, Rio Branco = -5.
UTC_OFFSET_HORAS = -3

DURACAO_PADRAO_MIN = 30


def escapar(texto):
    """Escapa os caracteres que o formato iCalendar (RFC 5545) reserva."""
    return (
        texto.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def dobrar_linha(linha):
    """RFC 5545 limita a 75 octetos por linha; continuacao comeca com espaco."""
    bruto = linha.encode("utf-8")
    if len(bruto) <= 75:
        return linha
    partes, atual = [], b""
    for char in linha:
        c = char.encode("utf-8")
        limite = 75 if not partes else 74
        if len(atual) + len(c) > limite:
            partes.append(atual)
            atual = b""
        atual += c
    partes.append(atual)
    return "\r\n ".join(p.decode("utf-8") for p in partes)


def para_utc(data, hora):
    local = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
    return local.replace(
        tzinfo=timezone(timedelta(hours=UTC_OFFSET_HORAS))
    ).astimezone(timezone.utc)


def main():
    if not os.path.exists(ENTRADA):
        sys.exit(
            f"'{ENTRADA}' nao existe.\n"
            f"Rode: cp calls.exemplo.csv {ENTRADA} e preencha com as calls reais."
        )

    carimbo = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    linhas = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Acompanha.ai//Prospeccao//PT-BR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ]

    total = 0
    with open(ENTRADA, encoding="utf-8") as f:
        for i, linha in enumerate(csv.DictReader(f), start=1):
            if not linha.get("data") or linha["data"].lstrip().startswith("#"):
                continue

            nome = (linha.get("nome") or "nutricionista").strip()
            cidade = (linha.get("cidade") or "").strip()
            telefone = (linha.get("telefone") or "").strip()
            notas = (linha.get("notas") or "").strip()

            try:
                minutos = int(linha.get("duracao_min") or DURACAO_PADRAO_MIN)
                inicio = para_utc(linha["data"].strip(), linha["hora"].strip())
            except ValueError as erro:
                print(f"  linha {i} ignorada ({erro})", file=sys.stderr)
                continue

            fim = inicio + timedelta(minutes=minutos)

            titulo = f"Entrevista - {nome}"
            if cidade:
                titulo += f" ({cidade})"

            corpo = [
                "Entrevista de descoberta - NAO e demo.",
                "Roteiro: _prospeccao/03-roteiro-entrevista.md",
                "",
                "Bloco 2 (o paciente que sumiu) e o mais importante.",
                "Meta: voce fala menos de 25% do tempo.",
            ]
            if telefone:
                corpo.insert(1, f"WhatsApp: {telefone}")
            if notas:
                corpo += ["", f"Notas: {notas}"]

            linhas += [
                "BEGIN:VEVENT",
                f"UID:entrevista-{i}-{carimbo}@acompanha.ai",
                f"DTSTAMP:{carimbo}",
                f"DTSTART:{inicio.strftime('%Y%m%dT%H%M%SZ')}",
                f"DTEND:{fim.strftime('%Y%m%dT%H%M%SZ')}",
                dobrar_linha(f"SUMMARY:{escapar(titulo)}"),
                dobrar_linha(f"DESCRIPTION:{escapar(chr(10).join(corpo))}"),
                "BEGIN:VALARM",
                "TRIGGER:-P1D",
                "ACTION:DISPLAY",
                dobrar_linha(f"DESCRIPTION:{escapar(f'Confirmar com {nome} no WhatsApp')}"),
                "END:VALARM",
                "BEGIN:VALARM",
                "TRIGGER:-PT15M",
                "ACTION:DISPLAY",
                dobrar_linha(f"DESCRIPTION:{escapar(f'Abrir roteiro - {nome} em 15 min')}"),
                "END:VALARM",
                "END:VEVENT",
            ]
            total += 1

    linhas.append("END:VCALENDAR")

    if not total:
        sys.exit(f"Nenhuma call valida encontrada em '{ENTRADA}'.")

    with open(SAIDA, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(linhas) + "\r\n")

    print(f"{total} call(s) -> {SAIDA}")
    print("Google Agenda > Configuracoes > Importar e exportar > Importar")


if __name__ == "__main__":
    main()
