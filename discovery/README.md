# Problem discovery simulado — acompanha.ai

> **⚠️ Estas entrevistas são simuladas por IA.** Não validam nem invalidam nada sobre o mercado real. Servem para: (1) afiar o roteiro antes de gastar entrevistas reais; (2) antecipar objeções; (3) priorizar hipóteses. As personas derivam das mesmas crenças que produziram a landing; LLMs tendem à coerência e cordialidade; todos os números citados são fabricados. A única evidência que conta vem de nutricionistas de verdade — roteiro pronto em `proximos-passos.md`.

**O estudo:** 100 entrevistas de problem discovery (método Mom Test, discovery puro — o produto nunca foi revelado) entre uma entrevistadora-agente e 100 nutricionistas-persona geradas com cotas de carteira, modelo de atendimento, especialidade, região e carreira — ~40% delas desenhadas para a tese central **falhar**. Cada entrevista tem transcript integral e análise individual em `entrevistas/`; a síntese cruzada, a auditoria independente de viés e o plano de discovery real estão nos arquivos abaixo.

## Resultado em uma linha

**A tese "nutricionistas sofrem com pacientes que somem" fisga o clique mas não é a dor nº 1: a evasão como dor espontânea foi refutada em 68% das personas — inclusive dentro do grupo desenhado a favor dela — enquanto a dor espontânea dominante é o plantão não remunerado de WhatsApp, e a dor de evasão que sobrevive é "descobrir tarde demais que o paciente sumiu".**

## Matriz de hipóteses (% das 100 personas)

| # | Hipótese | Validada | Refutada | Inconclusiva | Veredicto |
|---|---|---|---|---|---|
| H1 | Evasão é dor top-3 espontânea | 18% | **68%** | 14% | Refutada — a dor existe, mas raramente é a primeira da boca |
| H2 | Lapso de fim de semana → vergonha → sumiço | 13% | **62%** | 25% | Refutada como mecanismo dominante ("melhorou e sumiu" + transições de vida dominam) |
| H3 | Plantão não remunerado de WhatsApp | **50%** | 48% | 2% | Dividida — forte no particular (73%), zero em clínica/convênio; validações seguem o desenho (ver anexo da síntese) |
| H4 | Perda financeira percebida como relevante | 43% | **47%** | 10% | Empate técnico — depende de quem captura a perda |
| H6' | Pacientes abandonam ferramentas de acompanhamento | 26% | 20% | **54%** | Subtestada (falha de roteiro); quando testada, adesão colapsa em 2–4 semanas |
| H7' | Já paga por ferramentas (proxy de WTP) | **45%** | 42% | 13% | Divide por modelo: particular 68%, convênio 0%; WTP da categoria segue desconhecida |
| H9 | Por que clicam e não convertem | — | — | — | Ver leitura do funil em `sintese.md` |
| H5/H8 | IA falando com paciente / onboarding PDF | — | — | — | **Adiadas** — só rodada de teste de solução responde |

## Os 5 achados (detalhe em `sintese.md`)

1. **A dor espontânea nº 1 é o plantão de WhatsApp, não a evasão** (34/100 personas, 6–15h/semana) — com a ressalva da auditoria: parte disso pode ser eco do desenho das fichas.
2. **A dor de evasão que sobrevive é a detecção tardia** ("nove meses sem vir e eu nem tinha percebido" — 001) — candidata a dor-núcleo para produto e copy.
3. **Modelo de remuneração muda o sinal de tudo:** convênio/clínica multi refutam a tese em bloco (fila repõe, quem decide é o dono) — provável fonte de clique-sem-conversão.
4. **O mecanismo da landing (vergonha de fim de semana) praticamente não apareceu** — os mecanismos documentados são "melhorou e sumiu", parto, GLP-1, dinheiro.
5. **"Meu paciente não vai usar" é a objeção nº 1** — cicatriz de apps abandonados; e é também o melhor argumento do WhatsApp como canal (nada para baixar).

## Leitura do funil (CTR 4,77%, zero leads)

O anúncio compra o clique por reconhecimento emocional parcial; a landing perde a conversão porque: (1) não desarma "meu paciente não vai usar"; (2) dispara medo de despersonalização do vínculo; (3) parte de quem clica não decide a compra (convênio/CLT); (4) a dor anunciada não é a dor nº 1 de boa parte da audiência; (5) número de perda pronto ativa reflexo anti-vendas; (6) "agende uma demo" perde para teste self-service + prova social. Recomendações acionáveis na síntese.

## Auditoria de viés (leia antes de citar qualquer número)

Um advogado do diabo independente auditou a síntese contra os dados (`auditoria-vies.md`): aritmética 100% conferida e refutações reportadas com destaque, **mas** encontrou circularidade não confessada no achado do WhatsApp, 1 citação inexistente + 4 paráfrases entre aspas (corrigidas na síntese, nota no topo), um par de personas quase-clone inflando o corte de clínica, e sobre-correção anti-tese no achado da vergonha. Veredicto: **gerador de hipóteses, não evidência.**

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `metodologia.md` | Desenho do estudo, cotas, isolamento de informação, regras anti-viés |
| `personas.md` | Índice das 100 personas |
| `protocolo-entrevista.md` | Roteiro Mom Test B0–B5 (reutilizável em entrevistas reais) |
| `entrevistas/NNN-*.md` | 100 transcripts integrais + análise individual |
| `fichas/NNN.json` | Fichas completas das personas (fatos privados usados na simulação) |
| `sintese.md` | Síntese cruzada: matriz, padrões por segmento, funil, ICP, implicações |
| `auditoria-vies.md` | Auditoria independente do advogado do diabo (intacta) |
| `proximos-passos.md` | Plano de discovery REAL: roteiro ajustado, recrutamento, critérios de invalidação |
