
from crypto_app.blowfish_algo import Blowfish

def test_blowfish():
    """
    Un exemple de fonction de test, ici avec le cryptage
    de blowfish.
    """

    blowfish = Blowfish()
    msg = "Message"
    key = "justineisthebest"

    # pour cette fonction il est difficile de vérifier la valeur de la variable encryped,
    # car elle est différente à chaque exécution du code. 
    # la vérification sur fait seulement sur le fait que le msg de départ est different de la variable encrypted.
    # par contre il est possible de vérifier que la fonction decrypted.

    encrypted = blowfish.encrypt(msg, key)
    assert decrypted != "Message"
    decrypted = blowfish.decrypt(encrypted, key)
    assert decrypted == "Message"
