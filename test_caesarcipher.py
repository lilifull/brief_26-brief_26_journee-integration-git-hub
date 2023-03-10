
from crypto_app.caesarcipher_algo import CaesarCipher

def test_caesarcipher():
    """
    Un exemple de fonction de test, ici avec le cryptage
    d'caesarcipher.
    """

    caesarcipher = CaesarCipher()
    msg = "Message"
    key = 10

    encrypted = caesarcipher.encrypt(msg, key)
    print(encrypted)
    assert encrypted == "Wocckqo"
    decrypted = caesarcipher.decrypt(encrypted, key)
    print(decrypted)
    assert decrypted == "Message"

