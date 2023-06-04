from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match=f"tipo inválido para key"):
        encrypt_message('1', '1')
    with pytest.raises(TypeError, match=f"tipo inválido para message"):
            encrypt_message(1, 1)
    assert encrypt_message('mensagem', 9) == 'megasnem'
    assert encrypt_message('mensagem', 3) == 'nem_megas'
    assert encrypt_message('mensagem', 2) == 'megasn_em'