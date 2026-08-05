# Protocolo de entrevista — Problem Discovery com nutricionistas

> Este roteiro foi escrito para ser usado **verbatim em entrevistas reais** com nutricionistas.
> Foi também o roteiro seguido pela entrevistadora simulada nas 100 entrevistas deste estudo
> (ver `metodologia.md`). Base metodológica: *The Mom Test* (Rob Fitzpatrick) e
> *Continuous Discovery Habits* (Teresa Torres).

## O que este roteiro testa (agenda oculta — a entrevistada nunca vê isto)

| ID | Hipótese |
|----|----------|
| H1 | Evasão/abandono de pacientes é uma dor top-3, **nomeada espontaneamente** pela nutricionista |
| H2 | O abandono nasce de lapsos do dia a dia entre consultas (fim de semana, festas) — e ela percebe essa mecânica |
| H3 | Existe "plantão" não remunerado de WhatsApp, com volume que incomoda |
| H4 | A perda financeira da evasão é percebida como relevante (colher o palpite espontâneo dela em R$/ano) |
| H6' | Histórico com ferramentas de acompanhamento: os **pacientes** abandonam as ferramentas? O que já fracassou e por quê? |
| H7' | Quanto ela gasta hoje com ferramentas e quanto já pagou tentando resolver acompanhamento (proxy de disposição a pagar) |

Duas hipóteses do acompanha.ai **não são testáveis** em discovery puro e ficam para uma rodada
separada de teste de solução: H5 (aceitaria uma IA falando com pacientes em nome dela) e
H8 (onboarding por PDF do plano é aceitável).

## Enquadramento de abertura (obrigatório, sem variação)

> "Obrigada por topar. Estou fazendo uma pesquisa independente sobre a rotina de nutricionistas
> — especificamente sobre o que acontece com os pacientes **entre** as consultas. Não tenho nada
> para vender e não existe resposta certa: eu quero entender o seu dia a dia real."

**Nunca** mencionar: produto, solução, IA, automação, assistente, empresa, startup.

## As leis da entrevistadora

1. **Nunca vender, nunca sugerir solução.** Esta entrevista é 100% sobre o problema.
2. **Passado e fatos, não futuro e opinião.** Proibido: "você usaria…", "você pagaria…",
   "você acha que seus pacientes aceitariam…". Forma canônica: **"me conta a última vez que…"**.
3. **No máximo 2 perguntas por fala.** A entrevistada fala 80% do tempo.
4. **Resposta seca não se preenche com animação.** Devolver "como assim?" ou pedir o caso concreto.
5. **Perseguir emoção.** Culpa, orgulho, irritação, cansaço → cavar ali antes de mudar de bloco.
6. **Espelhar o vocabulário dela.** Não introduzir "evasão", "retenção", "adesão", "plantão"
   antes que ela use algo equivalente — se ela usar espontaneamente, é um achado (anotar!).
7. **Única pergunta de opinião permitida:** "por que você acha que *aquele* paciente sumiu?"
   — seguida de "ele chegou a te dizer isso, ou é sua leitura?".
8. **Sinais de compra falsos vs. reais** (para quando houver rodada de solução): elogio e
   "me manda quando lançar" valem zero; valem: piloto com data, pacientes específicos oferecidos,
   pergunta espontânea de preço, pedido para apresentar a uma colega.

## Blocos

### B0 — Abertura e contexto (≈2 min)
- Enquadramento acima.
- "Me dá um retrato do consultório hoje: quantos pacientes ativos você acompanha? Quantas consultas por semana?"

### B1 — Rotina e carga de trabalho (≈5 min)
- "Como foi a sua última terça-feira, do início ao fim?"
- "Fora da consulta em si, o que mais consome seu tempo?"

### B2 — Comunicação entre consultas (≈8 min)
- "Pega seu WhatsApp mentalmente: qual foi a última mensagem de paciente que chegou fora do horário? O que dizia?"
- "Você respondeu quando? Por quê?"
- "Num dia normal, quantas mensagens de paciente chegam? Quem responde?"

### B3 — Casos concretos de abandono (≈10 min — o coração da entrevista)
- "Me conta do último paciente que sumiu. Como você percebeu?"
- "Quanto tempo levou entre ele sumir e você notar? O que você fez?"
- "Nos últimos 3 meses, quantos sumiram assim?"
- (única opinião permitida) "Por que você acha que *aquele* paciente sumiu? Ele te disse ou é leitura sua?"

### B4 — O que já tentou (≈7 min)
- "Você já tentou alguma coisa para acompanhar ou segurar paciente entre consultas — app, diário,
  mensagem programada, secretária, pacote com suporte? O que aconteceu **de verdade** com cada uma?"
- Se citar ferramenta paga: "quanto custava? por que cancelou/manteve?"

### B5 — Custo atual e fechamento (≈5 min)
- "Somando tudo, quantas horas por semana você gasta respondendo paciente fora da consulta?"
- "Quanto você paga hoje, por mês, de ferramentas do consultório?"
- "Se tivesse que chutar: quanto os pacientes que somem custam para você num ano?"
  — **jamais sugerir um número ou fazer a conta por ela.** (O interessante é comparar o palpite
  espontâneo com os R$ 25.920/ano da calculadora da landing.)
- Agradecer + pedir indicação: "conhece uma colega com uma rotina bem diferente da sua que toparia conversar?"

## Registro pós-entrevista (preencher em até 1h)

- Veredicto por hipótese: `validada` (evidência concreta espontânea) / `refutada` (negação clara
  ou ausência onde deveria aparecer) / `inconclusiva` (na dúvida, é esta).
- Dor dominante DELA (pode não ser retenção — anotar a real).
- 3–5 citações verbatim.
- Surpresas.
- Falhas da entrevistadora (perguntas induzidas, oportunidades perdidas).

## Critérios de invalidação pré-registrados (para a rodada REAL)

Definidos **antes** de entrevistar, para não racionalizar depois:

1. Se **menos de 4 em cada 10** nutricionistas de consultório particular nomearem espontaneamente
   pacientes que somem como uma das 3 coisas que mais as incomodam → H1 refutada → a headline
   da landing está apontando para a dor errada.
2. Se a estimativa espontânea mediana de perda anual ficar **abaixo de R$ 5.000** → H4 refutada →
   a calculadora de R$ 25.920 soa inflada e mina a credibilidade da página.
3. Se a maioria relatar que pacientes abandonaram **toda** ferramenta de acompanhamento já tentada
   (H6' contra) → o produto precisa de prova de engajamento do paciente antes de qualquer promessa
   à nutricionista.
