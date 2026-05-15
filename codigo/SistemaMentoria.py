from abc import ABC, abstractmethod

# --- PADRÃO STRATEGY (Comportamental) ---
# Motivação: Diferentes formas de validar a competência do mentor (GitHub, Histórico, etc)
class EstrategiaValidacao(ABC):
    @abstractmethod
    def validar(self, dados):
        pass

class ValidacaoGithub(EstrategiaValidacao):
    def validar(self, dados):
        print(f"Verificando repositórios de {dados} no GitHub...")
        return "github.com" in dados

class ValidacaoAcademica(EstrategiaValidacao):
    def validar(self, dados):
        try:
            nota = float(dados)
            return nota >= 8.0
        except (ValueError, TypeError):
            return False

# --- PADRÃO FACTORY METHOD (Criacional) ---
# Motivação: Criar diferentes tipos de 'Templates de Dúvida' (Hardware vs Software)
class TemplateDuvida(ABC):
    @abstractmethod
    def exibir_formulario(self):
        pass

class TemplateHardware(TemplateDuvida):
    def exibir_formulario(self):
        return "Campos: [Modelo da Placa], [Esquemático], [Componentes usados]"

class TemplateSoftware(TemplateDuvida):
    def exibir_formulario(self):
        return "Campos: [Linguagem], [Stack Trace do Erro], [Link do Repositório]"

class FabricaTemplates:
    def criar_template(self, tipo):
        if tipo == "hardware": return TemplateHardware()
        if tipo == "software": return TemplateSoftware()
        raise ValueError("Tipo de template desconhecido")

# --- EXECUÇÃO DO PROTÓTIPO ---
if __name__ == "__main__":
    print("--- 1. Cadastro de Mentor (Validação) ---")
    validador = ValidacaoAcademica()
    sucesso = validador.validar(5.0)
    print(f"Resultado da validação: {'Aprovado' if sucesso else 'Reprovado'}\n")

    print("--- 2. Criação de Template de Dúvida ---")
    fabrica = FabricaTemplates()
    meu_template = fabrica.criar_template("software")
    print(f"O mentorado verá: {meu_template.exibir_formulario()}")