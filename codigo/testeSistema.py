import unittest
from SistemaMentoria import ValidacaoAcademica, FabricaTemplates, TemplateSoftware

class TestSistemaMentoria(unittest.TestCase):

    def setUp(self):
        self.validador_academico = ValidacaoAcademica()
        self.fabrica = FabricaTemplates()

    # --- Testes para Validação Acadêmica (Strategy) ---
    def test_validacao_academica_sucesso(self):
        """Cenário de Sucesso: Nota acima do limite (8.0)"""
        self.assertTrue(self.validador_academico.validar(9.5))

    def test_validacao_academica_falha(self):
        """Cenário de Falha: Nota abaixo do limite"""
        self.assertFalse(self.validador_academico.validar(5.0))

    def test_validacao_academica_borda(self):
        """Cenário de Borda: Nota exatamente no limite (8.0)"""
        self.assertTrue(self.validador_academico.validar(8.0))

    # --- Testes para Fábrica de Templates (Factory Method) ---
    def test_criacao_template_sucesso(self):
        """Cenário de Sucesso: Tipo existente"""
        template = self.fabrica.criar_template("software")
        self.assertIsInstance(template, TemplateSoftware)

    def test_criacao_template_excecao(self):
        """Cenário de Exceção: Tipo inexistente deve levantar ValueError"""
        with self.assertRaises(ValueError):
            self.fabrica.criar_template("civil")

    def test_criacao_template_case_sensitivity(self):
        """Cenário de Borda: Entrada com letras maiúsculas/espaços"""
        # Se a fábrica não tratar case-sensitivity, isso falhará. 
        # É um ponto importante para testar a robustez da entrada.
        with self.assertRaises(ValueError):
            self.fabrica.criar_template("SOFTWARE")

if __name__ == "__main__":
    unittest.main()