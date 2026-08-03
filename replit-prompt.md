# Prompt para o Replit Agent — Acompanha.ai (MVP)

> Cole tudo abaixo da linha no Replit Agent. Instruções de uso no fim do arquivo.

---

## Contexto

Construa o **Acompanha.ai**: um app web para **nutricionistas de consultório no Brasil**, com uma assistente de IA que acompanha os pacientes entre as consultas. Na versão final o paciente conversa pelo WhatsApp; **neste MVP o canal do paciente é um simulador de chat estilo WhatsApp embutido no app**, para testar a assistente antes de conectar o WhatsApp real (fase 2 — apenas deixe a arquitetura preparada). A assistente responde dúvidas **somente dentro do plano alimentar prescrito pela nutricionista**, faz check-ins proativos, registra fotos de refeição e escala para a nutricionista tudo o que não pode responder. Mantra do produto: **"A IA tria. Você decide."**

Interface 100% em **português do Brasil** (código e nomes de entidades em inglês). Antes de implementar, **me faça perguntas se algo estiver ambíguo** — não decida sozinho pontos de regra de negócio.

## Stack e infraestrutura

- Stack padrão do Replit (React + TypeScript no front, Express no back).
- **Banco PostgreSQL integrado do Replit** desde o início — nada de armazenamento em memória ou JSON.
- PDFs de plano e fotos de refeição no **Replit Object Storage privado**, servidos apenas por rotas autenticadas ou URLs assinadas (nunca públicos: são dados de saúde). Aceitar JPG, PNG e PDF nos uploads, com mensagem de erro clara para formatos não suportados.
- Login da nutricionista com **Replit Auth**. **Isolamento estrito por conta**: toda query filtra por `nutritionist_id` — uma nutricionista jamais vê pacientes de outra.
- IA: **API da Anthropic (Claude)** com o SDK oficial `@anthropic-ai/sdk`; confirme comigo o model ID atual antes de fixá-lo no código. Configure a chave via **Replit Secrets** como `ANTHROPIC_API_KEY` — peça-me o valor quando precisar; não invente integração alternativa.
- Datas e horários armazenados e calculados no fuso **America/Sao_Paulo**.
- Jobs recorrentes (disparo de check-ins, recálculo de risco): **scripts separados executáveis** (`npm run dispatch-checkins`, `npm run compute-risk`) que eu agendarei depois via Scheduled Deployment — **não** use cron embutido no servidor. No painel, um botão de teste "Disparar check-ins agora".

## Usuários e papéis

1. **Nutricionista** — usuária do painel web (desktop-first): cadastra pacientes, aprova planos, define check-ins, revisa a triagem, audita conversas. Não deve precisar vigiar a tela o dia todo.
2. **Paciente** — no MVP existe só através do simulador de chat (mobile-first), acessado de dentro do painel autenticado ("conversar como este paciente"). Sem login próprio.
3. **Assistente de IA** — nome configurável por nutricionista (padrão "Ana"); sempre se apresenta como "Ana, assistente virtual da equipe da Dra. [nome]". Nunca finge ser humana.

## Funcionalidades do MVP

1. **Dashboard "silêncio organizado"**: alertas de risco de abandono no topo (ex.: "Juliana M. — risco alto — 3 check-ins sem resposta, lapso relatado no sábado"), fila de triagem pendente e card de resumo da semana (ex.: "84% dos pacientes fizeram check-in, 12 dúvidas respondidas pela IA, 2 encaminhadas para você").
2. **Onboarding de paciente**: cadastro (nome, telefone, objetivo) + plano alimentar por **upload de PDF ou foto** (exportado do software de prescrição), que o Claude extrai para formato estruturado (refeições, horários, alimentos, quantidades, substituições) — **ou cadastro manual** quando o arquivo for ilegível. A extração é sempre uma **proposta**: a nutricionista revisa, edita e aprova (status `draft` → `confirmed`) antes de o paciente ser ativado. No mesmo fluxo ela cadastra as substituições aprovadas e os horários de check-in. **Consentimento LGPD como gate**: a primeira mensagem da assistente explica o acompanhamento (telemonitoramento — Resolução CFN 760/2023), quais dados são usados e para quê; a conversa só começa após o aceite, registrado com data/hora e texto. Recusa bloqueia a conversa; deve existir a ação "encerrar acompanhamento e excluir/anonimizar os dados do paciente".
3. **Simulador de chat estilo WhatsApp**: bolhas `#D8F0CE` para o paciente, brancas para a assistente, timestamps; suporta texto, botões de resposta rápida e **foto de refeição** (analisada pelo Claude com visão, registrada como refeição e respondida com orientação gentil, sem julgamento).
4. **Pipeline de IA com guardrails** (seção própria abaixo).
5. **Check-ins proativos**: por paciente, dia da semana + horário + mensagem (ex.: sábado 18h "como foi o fim de semana?"); responder leva um toque (botões "consegui / mais ou menos / não consegui") ou um texto/foto.
6. **Fila de triagem**: cada item com tipo (sintoma | medicamento | pedido de mudança | fora do plano | risco emocional | outro), prioridade (sinal de relação difícil com comida = alta), trecho da conversa e campo de resposta da nutricionista — enviada ao paciente pelo canal. Estado vazio: "Tudo em dia. A Ana está cuidando das conversas."
7. **Risco de abandono**: score explicável (baixo/médio/alto) calculado pelo script recorrente com sinais simples: check-ins sem resposta consecutivos, dias sem mensagem, lapsos relatados. O "porquê" sempre visível junto do alerta.
8. **Página do paciente + histórico auditável**: plano aprovado, substituições, linha do tempo de check-ins e refeições, e **toda conversa registrada** (incluindo a rota do classificador e o motivo de cada resposta da IA). Botão "marcar resposta como incorreta" com correção da nutricionista, com escopo **este paciente** ou **regra geral**, injetada no contexto das próximas respostas.

## Guardrails da IA (inegociáveis — implementar como código no backend, não só no prompt)

Fluxo de CADA mensagem do paciente: **(1)** uma chamada de classificação decide a rota; **(2)** rota "dentro do plano" (dúvida coberta pelo plano `confirmed` + substituições aprovadas) → a IA responde usando SOMENTE o plano estruturado, as substituições e as correções da nutricionista como contexto, citando o plano; **(3)** qualquer outra coisa → resposta padrão acolhedora de encaminhamento ("Boa pergunta! Vou encaminhar para a Dra. [nome], ela te responde em breve") + item na fila de triagem. A decisão de rota é do classificador em código — não confie apenas no system prompt.

- **NUNCA prescrever, criar ou alterar dieta** (prescrição dietética é ato privativo do nutricionista — Lei 8.234/91). A assistente executa o plano existente, jamais inventa um.
- **NUNCA decidir conduta clínica**: sintoma, medicamento/suplemento, pedido de mudança no plano, sinal de relação difícil com comida → triagem, sempre.
- **Emergência**: sinal de sintoma agudo grave ou de risco à própria vida → além de triagem com prioridade máxima, a assistente orienta procurar atendimento imediato (emergência / CVV 188), sem diagnosticar.
- **NUNCA improvisar** fora do plano/substituições aprovadas. Paciente sem plano `confirmed` recebe só acolhimento + triagem.
- **NUNCA esconder conversa**: 100% registrado e auditável — o histórico é também a documentação do telemonitoramento.
- **Falha da API do Claude**: nunca deixar o paciente no vácuo — mensagem padrão ("recebi sua mensagem, já te respondo!") + retry + registro do erro. Nenhuma resposta sai sem passar pelo classificador.
- Momentos de "socorro" (rodízio, festa, viagem, "já estraguei tudo"): acolher, orientar dentro do que o plano permite e desarmar a culpa, sem julgamento.
- Tom: acolhedor, direto, gentil, pt-BR. System prompt em arquivo versionável (ex.: `server/ai/system-prompt.ts`), interpolando plano, substituições, correções e nome da assistente.

## Modelo de dados (Postgres; nomes em inglês)

`nutritionists` (perfil, CRN, nome da assistente) · `patients` (dados, telefone, status, nível de risco, `consent_at`/`consent_text`) · `meal_plans` (arquivo original, versão estruturada, `draft/confirmed`) · `meal_plan_items` (refeição, horário, alimento, quantidade) · `substitutions` (item do plano → alternativas aprovadas) · `conversations`/`messages` (`sender_type`: patient|ai|nutritionist; `channel`: simulator|whatsapp; tipo texto|foto|checkin; rota do classificador + motivo; flag `marked_incorrect`) · `checkin_schedules` · `checkin_events` (disparos e respostas) · `meal_logs` (foto, refeição associada, análise da IA) · `triage_items` (tipo, prioridade, trecho, status, resposta) · `risk_assessments` (score, nível, fatores em JSON explicável) · `ai_corrections` (resposta original, correção, escopo).

## Canal preparado para WhatsApp (fase 2 — NÃO implementar agora)

Toda troca de mensagens passa por uma interface `ChannelAdapter` (enviar mensagem/check-in; receber mensagem/foto normalizadas). Única implementação no MVP: `SimulatorChannel`. Crie apenas o stub da rota de webhook `/webhook/whatsapp` (GET de verificação com `hub.challenge` + POST de eventos), **sem lógica**. Toda a lógica de negócio (IA, triagem, check-ins, logs) deve ser independente do canal. Secrets da fase 2 (não pedir agora): `WHATSAPP_ACCESS_TOKEN`, `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_VERIFY_TOKEN`.

## Design

Fundo creme `#FAF9F6`, verdes `#14532D` / `#166534` / `#15803D` como cores primárias; **dark mode** com verde `#22C55E` sobre fundo `#101613`. Tipografia system-ui, cantos arredondados, visual limpo e acolhedor — sem cara de software hospitalar. Badges de risco com cores acessíveis (não só vermelho/verde puros). Toda a microcopy em pt-BR no tom da marca: direto, gentil, sem tecniquês.

## O que NÃO construir no MVP

Integração real com WhatsApp/Twilio/Meta; pagamentos/assinatura; multi-clínica/equipes; app mobile nativo; notificações push/e-mail; login de paciente; qualquer cálculo nutricional ou geração de dieta.

## Por onde começar

Primeiro checkpoint = **fluxo vertical completo com dados seed** (Dra. Camila, assistente "Ana", 2 pacientes fictícios com planos aprovados): paciente pergunta uma substituição → a IA responde dentro do plano; paciente relata um sintoma → vai para a triagem. Inclua no seed um conjunto de mensagens de teste dos guardrails (dúvida coberta, dúvida não coberta, sintoma, medicamento, pedido de mudança no plano, "já estraguei tudo") para eu validar as rotas do classificador. Me mostre esse fluxo funcionando antes de seguir para check-ins, risco e resumos.

---

## Como usar este prompt no Replit (não colar esta parte)

1. **Cole o prompt** (da seção "Contexto" até "Por onde começar") num app novo no Replit Agent. Se quiser, use o botão "Improve prompt" antes de enviar.
2. **Anexe um print da landing page** (acompanhanutri.com.br) como referência visual — referência de imagem funciona muito melhor que descrição de cores.
3. **Tenha a chave da Anthropic em mãos** (console.anthropic.com → API Keys). O Agent vai pausar e pedir o valor para guardar em Secrets — nunca cole a chave no chat do prompt.
4. **Valide o primeiro checkpoint** (fluxo seed com as mensagens de teste) antes de pedir mais coisas. Depois, itere com **uma tarefa por mensagem** — cada mensagem vira um checkpoint com rollback.
5. **Check-ins em produção**: depois do deploy, crie um Scheduled Deployment na interface do Replit apontando para `npm run dispatch-checkins` (o Agent não configura isso sozinho de forma confiável).
6. **WhatsApp real (fase 2)**: exige conta na Meta WhatsApp Business Cloud API (ou Twilio como ponte), número aprovado e cadastro manual do webhook na URL de deploy `*.replit.app` — essa parte de contas e aprovações é manual, fora do alcance do Agent.
