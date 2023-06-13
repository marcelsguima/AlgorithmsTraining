from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    message = "bolo de fuba"
    assert encrypt_message(message, 3) == "lob_abuf ed o"
    assert encrypt_message(message, 4) == "abuf ed _olob"
    assert encrypt_message(message, 0) == "abuf ed olob"

    with pytest.raises(TypeError):
        encrypt_message(80001, 1)

    with pytest.raises(TypeError):
        encrypt_message(message, "8")
