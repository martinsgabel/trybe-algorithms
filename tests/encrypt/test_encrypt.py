import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("livros", 1) == "l_sorvi"
    assert encrypt_message("livros", 2) == "sorv_il"
    assert encrypt_message("livros", 10) == "sorvil"

    with pytest.raises(TypeError):
        encrypt_message(8, 8)
    with pytest.raises(TypeError):
        encrypt_message("string", "string")
