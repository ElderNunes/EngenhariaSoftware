# 🖥️ PMT-Eng — Parte 2
### Plataforma de Mentoria Técnica para Engenharia da Computação

---

## 📋 Sumário

- [Tarefa 2.1 — Definição da Arquitetura](#-tarefa-21--definição-da-arquitetura)
- [Tarefa 2.2 — Implementação com Padrões de Projeto](#-tarefa-22--implementação-com-padrões-de-projeto)
- [Tarefa 2.3 — Testes](#-tarefa-23--testes)

---

## 🏗️ Tarefa 2.1 — Definição da Arquitetura

### Padrão Arquitetural: Arquitetura em Camadas (N-Tier)

**Justificativa:** Escolhi este padrão porque ele permite isolar a complexa lógica de validação técnica da Engenharia da Computação (Camada de Negócio) das interfaces de usuário (Camada de Apresentação). Como o sistema possui regras de negócio específicas — como a verificação de competências e templates de dúvidas —, essa separação facilita a manutenção e permite que a interface seja atualizada (ex: criar um app mobile no futuro) sem mexer nas regras principais.

---

### Fluxo Geral

```
Usuário  ↔  Camada de Apresentação  ↔  Camada de Lógica/Serviços  ↔  Camada de Dados
```

---

### Componentes e Responsabilidades

| Componente | Camada | Responsabilidade |
|---|---|---|
| **Frontend** | Apresentação | Exibe formulários de dúvida e o calendário de agendamento. Garante interface amigável para mentorados com dificuldade de comunicação. |
| **Controlador de Autenticação e Perfil** | Lógica | Gerencia o acesso e a distinção entre Mentores, Mentorados e Coordenadores. |
| **Módulo de Gestão de Mentorias** | Serviço | Orquestra a lógica de agendamento, verifica a disponibilidade de horários e gerencia o status das sessões (`solicitada`, `aceita`, `concluída`). |
| **Módulo de Validação Técnica** | Serviço | Processa uploads de documentos e valida as competências do mentor antes de liberar o perfil. |
| **Camada de Dados** | Persistência | Armazena o histórico de mentorias, o repositório de dúvidas resolvidas e os dados de perfil dos usuários. |

---

### ⚠️ Limitação / Trade-off

**Aumento da Latência e Complexidade:** Ao separar o sistema em muitas camadas, a comunicação entre elas (ex: uma requisição que passa por `controller → service → repository`) pode adicionar uma leve latência e tornar o desenvolvimento inicial mais lento do que um padrão monolítico simples, exigindo mais código para realizar tarefas básicas.

---

> **Reflexão:** Escolhi essa Arquitetura de camadas, pois com ela consigo separar certinho o que cada coisa do meu sistema vai fazer. Vamos ter a interface de usuário, onde lá seria a "cara" do projeto; temos o "cérebro", onde vão estar todas as funções necessárias; e por último temos a "memória", que seria onde vou guardar tudo o que o sistema fizer.

---

## 🧩 Tarefa 2.2 — Implementação com Padrões de Projeto

---

### Padrão 1 — Strategy *(Comportamental)*

**Onde foi aplicado:** No arquivo `SistemaMentoria.py`, através da classe abstrata `EstrategiaValidacao` e suas implementações concretas (`ValidacaoGithub`, `ValidacaoAcademica`).

**Estrutura:**

```
EstrategiaValidacao  (Interface/Abstrata)
        ├── ValidacaoGithub
        └── ValidacaoAcademica
```

---

### Padrão 2 — Factory Method *(Criacional)*

**Onde foi aplicado:** No arquivo `SistemaMentoria.py`, na classe `FabricaTemplates` e no método `criar_template`, que decide qual objeto de template instanciar baseado na entrada do usuário.

**Estrutura:**

```
FabricaTemplates
        └── cria ──► TemplateDuvida  (Interface)
                            ├── TemplateHardware
                            └── TemplateSoftware
```

---

### 🔍 Revisão Crítica

O uso do **Factory Method** pode se tornar um problema se o sistema crescer para suportar dezenas de áreas diferentes (Redes, IA, Robótica, etc.), pois a classe da fábrica se tornará um "objeto gigante" difícil de manter. Além disso, para um novo membro da equipe, o excesso de abstrações nos padrões pode aumentar a curva de aprendizado em tarefas simples, como adicionar apenas um novo campo em um formulário.

---

## 🧪 Tarefa 2.3 — Testes

### Estratégia de Teste: Testes de Unidade

A estratégia adotada foi a de **Testes de Unidade**, focando no comportamento lógico isolado das classes. Escolhi essa abordagem porque, em um sistema de mentoria, a precisão das regras de negócio — como a nota de corte e a entrega do formulário correto — é o que garante a confiabilidade entre calouros e veteranos.

| Aspecto | Cobertura |
|---|---|
| Entradas válidas | ✅ Coberto |
| Recusas por critérios técnicos | ✅ Coberto |
| Tratamento de erros (exceções) | ✅ Coberto |
| Persistência de dados no banco | ❌ Fora do escopo do protótipo |
| Interface gráfica | ❌ Fora do escopo do protótipo |

---

### 🔍 Revisão Crítica

A parte do código mais difícil de testar seria a `ValidacaoGithub`, caso ela fizesse uma conexão real com a internet para verificar o perfil do aluno. Em um projeto de maior escala, depender de uma API externa torna os testes instáveis e dependentes de fatores fora do nosso controle (como queda de conexão ou limites de requisição), o que exigiria a criação de objetos simulados (**Mocks**) mais complexos para garantir que os testes continuem funcionando de forma isolada.

---

*PMT-Eng · Plataforma de Mentoria Técnica para Engenharia da Computação*
