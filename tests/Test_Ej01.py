from src.Ej01 import repetir_diez

def test_repetir_diez():
    assert repetir_diez("hola") == (
        "0. hola" "\n"
        "1. hola" "\n"
        "2. hola" "\n"
        "3. hola" "\n"
        "4. hola" "\n"
        "5. hola" "\n"
        "6. hola" "\n"
        "7. hola" "\n"
        "8. hola" "\n"
        "9. hola" "\n"
    )
    