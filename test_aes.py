
from crypto_app.aes_algo import AdvancedEncryptionStandard

def test_aes():
    """
    Un exemple de fonction de test, ici avec le cryptage
    d'aes.
    """

    aes = AdvancedEncryptionStandard()
    msg = "Message"
    key = "justineisthebest"

    encrypted = aes.encrypt(msg, key)
    assert encrypted == "3d87266b6f76d9"
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == "Message"
