# 🖥️ PMT-Eng
### Plataforma de Mentoria Técnica para Engenharia da Computação

---

## 📋 Sumário

- [Tarefa 1.1 — Proposta de Tema](#-tarefa-11--proposta-de-tema)
- [Tarefa 1.2 — Planejamento de Entrevista](#-tarefa-12--planejamento-de-entrevista)
- [Tarefa 1.3 — Histórias de Usuário](#-tarefa-13--histórias-de-usuário)
- [Tarefa 1.4 — Validação de Requisitos](#-tarefa-14--validação-de-requisitos)

---

## 💡 Tarefa 1.1 — Proposta de Tema

### O problema que o sistema resolve

Centraliza o suporte técnico para projetos que integram hardware e software, facilitando o agendamento de sessões de *pair programming*, revisão de esquemáticos e auxílio em *firmware*, resolvendo a fragmentação de informações comum em grupos de mensagens informais.

### Usuários principais

| Perfil | Descrição |
|--------|-----------|
| **Alunos Mentores** | Veteranos com competências validadas |
| **Alunos Mentorados** | Graduandos em busca de suporte prático |
| **Coordenadores de Curso** | Responsáveis pelo monitoramento de impacto |

### Por que esse problema é relevante

A Engenharia da Computação possui alta carga técnica e taxas de evasão elevadas; uma rede estruturada mitiga gargalos em disciplinas práticas, acelera o aprendizado de ferramentas de mercado e otimiza a resolução de problemas de baixo nível que travam o progresso acadêmico.

---

## 🎙️ Tarefa 1.2 — Planejamento de Entrevista

### Objetivo

Identificar os principais obstáculos técnicos e de comunicação que os alunos enfrentam ao desenvolver projetos de hardware e software, validando como o processo de busca por ajuda ocorre atualmente e mapeando os requisitos necessários para que uma plataforma de mentoria seja integrada à rotina acadêmica de forma eficiente.

---

### Roteiro de Perguntas

#### 🔍 Compreensão do Problema *(Perguntas Abertas)*

**1.** Quando você trava em um projeto, qual é o seu maior desafio: entender a parte técnica do erro ou conseguir explicar para alguém o que está acontecendo?

**2.** Você sente algum tipo de barreira social ou timidez ao abordar veteranos ou professores para tirar dúvidas? Por quê?

**3.** Na sua visão, o que mais impede a resolução rápida de um problema técnico no laboratório hoje?

---

#### 🗂️ Fluxos de Trabalho e Rotinas

**4.** Como é a sua rotina de estudos e como você encaixa a resolução de dúvidas nela?

**5.** Se você fosse atuar como mentor, você se sentiria confortável em ajudar um aluno de forma puramente técnica ou preferiria dar orientações mais gerais sobre como estudar a disciplina?

---

#### ⚠️ Frustrações e Limitações

**6.** Quais são os maiores problemas que você encontra ao tentar tirar dúvidas diretamente com professores ou veteranos em grupos de mensagens (ex: demora, linguagem muito complexa, falta de disponibilidade)?

**7.** Quais soluções você já tentou usar para resolver suas dúvidas de engenharia que acabaram não funcionando bem?

---

#### 🏁 Encerramento

**8.** Se existisse uma plataforma que conectasse você ao mentor certo no momento em que você trava, você a utilizaria no seu dia a dia acadêmico?

---

> **Reflexão:** Na parte de compreensão do problema, quero saber da pessoa qual a sua maior dificuldade em resolver o problema em que ela se encontra, se ela tem dificuldade em conversar com as pessoas, se tem problemas em resolver a parte técnica. Quero saber a rotina da pessoa, se ela consegue ajudar um aluno a resolver os problemas sendo técnico ou não. Quais são os maiores problemas delas em tirar dúvidas com os professores ou com alunos veteranos, e pra fechar se gostariam de uma plataforma que resolvesse esse grande problema.

---

## 📖 Tarefa 1.3 — Histórias de Usuário

---

### US-01 · Agendamento de Mentoria Específica
> *Como aluno mentorado, quero filtrar mentores por competências técnicas (ex: C++, Arduino, FPGA) para encontrar ajuda qualificada que resolva meu problema técnico específico.*

**Critérios de Aceitação:**
- O sistema deve exibir uma lista de mentores que possuem a *tag* da tecnologia selecionada.
- O usuário deve conseguir visualizar os horários disponíveis na agenda do mentor escolhido.
- O sistema deve permitir a confirmação do agendamento com envio de notificação para ambas as partes.

| Atributo | Valor |
|----------|-------|
| **Prioridade** | 🔴 Alta |
| **Justificativa** | É a funcionalidade central (*core*) do sistema; sem a conexão mentor-mentorado baseada em temas técnicos, o sistema perde seu propósito. |

---

### US-02 · Template de Dúvida Estruturada
> *Como aluno mentorado com dificuldade de comunicação, quero preencher um formulário padronizado ao solicitar mentoria para conseguir explicar meu problema de forma clara sem depender apenas da minha habilidade de conversação.*

**Critérios de Aceitação:**
- O formulário deve conter campos obrigatórios para: Descrição do Erro, Componentes/Linguagem utilizados e O que já foi tentado.
- O sistema deve permitir o upload de fotos do circuito ou prints do código/erro.
- O mentor deve conseguir visualizar essas informações antes de aceitar ou iniciar a sessão.

| Atributo | Valor |
|----------|-------|
| **Prioridade** | 🔴 Alta |
| **Justificativa** | Resolve diretamente a dor identificada na reflexão sobre a dificuldade dos alunos em se expressar e "quebrar o gelo". |

---

### US-03 · Validação de Competências do Mentor
> *Como coordenador do curso, quero validar as competências técnicas dos mentores através do histórico escolar ou portfólio para garantir que os mentorados recebam orientações corretas e seguras.*

**Critérios de Aceitação:**
- O mentor deve anexar um comprovante de aprovação na disciplina ou link do GitHub no perfil.
- O status do mentor deve aparecer como **"Pendente"** até que um administrador/coordenador aprove o perfil.
- O perfil aprovado deve exibir selos de competência verificada.

| Atributo | Valor |
|----------|-------|
| **Prioridade** | 🟡 Média |
| **Justificativa** | Garante a credibilidade da plataforma, evitando que informações técnicas erradas sejam propagadas. |

---

### US-04 · Registro de Soluções (FAQ Dinâmico)
> *Como aluno mentor, quero marcar uma dúvida como "resolvida" e publicar um breve resumo da solução para que outros alunos com o mesmo problema técnico possam consultar sem precisar de uma nova mentoria.*

**Critérios de Aceitação:**
- O sistema deve oferecer uma opção **"Publicar Solução"** ao final de cada mentoria.
- As soluções publicadas devem ser buscáveis por palavras-chave ou tags técnicas.
- O mentorado deve confirmar que a solução postada foi realmente útil e resolveu o problema.

| Atributo | Valor |
|----------|-------|
| **Prioridade** | 🟢 Baixa |
| **Justificativa** | É um recurso de otimização que ajuda a escala do sistema, mas não impede o funcionamento básico das mentorias individuais. |

---

### US-05 · Painel de Disponibilidade e Rotina
> *Como aluno mentor, quero definir meus horários fixos de disponibilidade semanal para ajudar calouros sem comprometer minha própria rotina de estudos e provas.*

**Critérios de Aceitação:**
- O mentor deve ter uma interface de calendário para marcar blocos de horários livres.
- O sistema deve impedir agendamentos em horários fora da janela definida pelo mentor.
- O mentor deve poder cancelar ou reagendar sessões com uma antecedência mínima pré-configurada.

| Atributo | Valor |
|----------|-------|
| **Prioridade** | 🔴 Alta |
| **Justificativa** | Essencial para que os veteranos aceitem ser mentores, garantindo que a ajuda não se torne um fardo em suas rotinas acadêmicas. |

---

> **Reflexão:** Ao escrever essas histórias de usuário, foquei em garantir que os mentores possuam a qualificação técnica necessária para oferecer um suporte seguro e correto. Ao mesmo tempo, me preocupei em criar mecanismos que facilitem a interação para o mentorado que possui barreiras de comunicação, utilizando formulários estruturados para que ele se sinta à vontade e consiga expressar suas dúvidas sem o peso da interação social improvisada. O objetivo é que o sistema não seja apenas um chat, mas uma ferramenta que remova tanto o obstáculo técnico quanto o psicológico.

---

## ✅ Tarefa 1.4 — Validação de Requisitos

Nesta etapa, analisamos as histórias **US-02** (Template de Dúvida) e **US-03** (Validação de Competências) para garantir que não haja furos no planejamento.

---

### Análise da US-02 · Template de Dúvida Estruturada

**🔶 Ambiguidades identificadas:**
- O termo *"Descrição do Erro"* é vago — o usuário pode escrever apenas "não funciona". Seria necessário definir campos como **"comportamento esperado"** vs **"comportamento observado"**.
- O tamanho máximo do upload de fotos também não foi especificado.

**⚡ Conflitos Potenciais:**
- Pode conflitar com a agilidade esperada na **US-01**. Se o formulário for longo demais, o aluno pode desistir de pedir ajuda, voltando para o WhatsApp.

**❓ Informações a elucidar:**
- É necessário perguntar aos alunos quais tipos de arquivos eles mais usam (PDF, `.c`, `.ino`, imagens de osciloscópio) para garantir que o sistema suporte os formatos corretos.

---

### Análise da US-03 · Validação de Competências do Mentor

**🔶 Ambiguidades identificadas:**
- O termo *"Histórico Escolar"* é sensível. Não está claro se o coordenador verá todas as notas do aluno ou apenas a disciplina da mentoria.
- O critério de "aprovado" (nota 5.0 ou nota 9.0?) precisa ser quantificado.

**⚡ Conflitos Potenciais:**
- Se o processo de aprovação do coordenador for muito lento, ele impede a **US-05** (Disponibilidade), pois o mentor não conseguirá liberar sua agenda enquanto estiver com status *"Pendente"*.

**❓ Informações a elucidar:**
- Precisamos confirmar com os coordenadores se eles têm tempo para validar esses perfis manualmente ou se preferem uma integração automática com o sistema acadêmico da faculdade.

---

### 🗑️ Revisão Crítica — História Removida

**História removida: US-04 · Registro de Soluções (FAQ Dinâmico)**

> Embora ajude a escala do sistema, ela é a única que não é essencial para o fluxo direto de conexão entre mentor e aluno. Sua remoção não impede que as mentorias aconteçam, enquanto a retirada de qualquer outra história afetaria ou a segurança técnica, ou a organização da agenda, ou a facilidade de comunicação — que são a base do projeto.

---

*PMT-Eng · Plataforma de Mentoria Técnica para Engenharia da Computação*
