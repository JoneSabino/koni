import calculadora

def test_soma_retorna_resultado_correto():
    assert calculadora.soma(1, 2) == 3

#TDD
def test_subtracao_retorna_resultado_correto():
    assert calculadora.subtracao(1, 2) == -1

def test_mensagem_correta_e_exibida():
    assert calculadora.mensagem() == "Olá, mundo!"