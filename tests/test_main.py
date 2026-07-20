from utils.mensagem import criar_mensagem


def test_criar_mensagem():
    resultado = criar_mensagem()

    assert resultado == "Cloud Data Platform funcionando!"
