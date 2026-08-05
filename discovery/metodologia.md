# Metodologia — Problem Discovery simulado (100 entrevistas)

> ⚠️ **Tudo neste estudo é simulação por IA.** Nenhuma nutricionista real foi entrevistada.
> O que este documento descreve é o desenho que torna a simulação *útil como geradora de
> hipóteses* — e os limites que a impedem de valer como evidência de mercado.

## Objetivo

Stress-testar as hipóteses de negócio do acompanha.ai (ver tabela em
`protocolo-entrevista.md`) antes de gastar entrevistas reais, que são escassas e caras de
recrutar. O exercício produz: roteiro afiado, objeções antecipadas, priorização de hipóteses
e um mapa de segmentos onde a tese tende a falhar.

## Arquitetura da simulação

### 1. Amostra desenhada por cotas (n=100)

100 personas de nutricionistas brasileiras geradas por cotas exatas em 6 eixos,
espelhando o formulário da landing e o mercado (194 mil profissionais, CFN):

| Eixo | Distribuição |
|------|--------------|
| Carteira ativa | até 10 (15) · 10–30 (30) · 30–60 (30) · 60+ (25) |
| Modelo | particular (40) · convênio/produção (15) · 100% online (15) · CLT/PJ em clínica multiprofissional (15) · pacote/consultoria com suporte incluso (15) |
| Especialidade | clínica/emagrecimento (35) · esportiva (15) · geral/família (15) · outras (15) · materno-infantil (10) · comportamental (10) |
| Região | SE (30) · NE (25) · S (15) · CO (15) · N (15); capital 56 / interior 44 |
| Carreira | <5 anos (25) · 5–15 (45) · 15+ (30) |
| Prognóstico de desenho | favorável à tese (35) · **tese deve falhar (40)** · ambígua (25) |

O eixo "prognóstico" é a principal contramedida anti-viés: **40% das personas foram
desenhadas para que a tese central do produto não se aplique a elas** (convênio repõe
paciente pela fila e evasão não custa nada; a dor real é captação, não retenção; filosofia
comportamental rejeita monitoramento alimentar; a carteira é da clínica e reter paciente
não muda o salário). 15 personas carregam "cicatriz de ferramenta": já pagaram um app de
acompanhamento e cancelaram decepcionadas.

Cada ficha contém **fatos privados** (os últimos 3 pacientes que sumiram, com história; a
última mensagem fora de horário, literal; gasto mensal com ferramentas; horas/semana
respondendo pacientes) — sem esse lastro, a persona inventa generalidades e a entrevista
vira opinião, exatamente o que o Mom Test proíbe.

### 2. Isolamento de informação (a propriedade central)

Três papéis, três dietas de informação:

- **A entrevistada** recebe apenas a própria ficha. Nunca vê as hipóteses, a copy da
  landing ou qualquer menção a produto/IA. Regra anti-complacência explícita no prompt:
  *"desinteresse educado é resposta válida e frequente; só demonstre engajamento se o tema
  tocar dor que a SUA ficha contém"*.
- **A entrevistadora** (persona "Marina", pesquisadora sênior Mom Test) recebe as hipóteses
  como agenda oculta + o protocolo, com leis duras: nunca mencionar solução, só perguntas
  de passado/fato, vocabulário da landing proibido ("evasão", "retenção", "plantão" só se a
  entrevistada usar primeiro).
- **O analista** (um por entrevista) vê tudo — ficha, transcript e hipóteses — e julga cada
  hipótese apenas pelo transcript, com critério conservador (na dúvida, `inconclusiva`;
  resposta educada/genérica não valida nada). Também detecta vazamentos da entrevistadora.

### 3. Entrevistas em ping-pong real

Cada entrevista é uma conversa entre **dois agentes de IA distintos e sem estado
compartilhado**, alternando com o transcript acumulado — a entrevistada não sabe qual é a
próxima pergunta, a entrevistadora não sabe o que há na ficha. Até 7 rodadas (≈14 falas),
blocos B0–B5 do protocolo. Formato deliberadamente rejeitado: um único agente "diretor de
cena" escrevendo os dois lados, que conhece a agenda e converge para entrevistas
complacentes.

### 4. Análise em camadas

1. **Analista individual** (100×): veredicto por hipótese com evidência, dores confirmadas
   e ausentes, citações verbatim, números colhidos, falhas da entrevistadora.
2. **Agregação quantitativa determinística**: matriz hipótese × persona contada por script
   (não por modelo de linguagem), com cortes por segmento.
3. **Sintetizadores de grupo** (10× de 10 entrevistas) → **síntese-mestre** com padrões por
   segmento, objeções ranqueadas e leitura do funil (H9).
4. **Advogado do diabo**: auditor independente que recebe síntese + análises e procura viés
   de confirmação, citações fora de contexto e distribuição de entusiasmo suspeita. Seu
   relatório (`auditoria-vies.md`) é publicado **intacto e separado**, para não ser diluído.

## Limites (leia antes de usar qualquer número deste estudo)

1. **As personas derivam das mesmas crenças que produziram a landing.** Quem escreveu as
   fichas conhece as hipóteses do produto. As cotas céticas mitigam, não eliminam, a
   circularidade.
2. **Modelos de linguagem tendem à coerência narrativa e à cordialidade.** Entrevistas
   reais têm mais ruído, silêncio e contradição do que qualquer simulação.
3. **Todos os números citados pelas personas são fabricados.** Frequências e percentuais da
   síntese descrevem *o comportamento das personas*, não do mercado.
4. **Validação aqui = hipótese refinada, nunca evidência.** O único uso legítimo dos
   resultados é decidir **o que testar primeiro com nutricionistas de verdade** — roteiro
   pronto em `protocolo-entrevista.md`, plano em `proximos-passos.md`.
