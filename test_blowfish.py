from crypto_app.blowfish_algo import Blowfish


def test_blowfish():
    """
    Pour cette algo il est difficile de vérifier la valeur de la variable encryped,
    car elle est différente à chaque exécution du code. 
    Le test verifie seulement que le msg de départ est different de la variable encrypted.
    Par contre il est possible de vérifier la fonction decrypted.
    """

    algo = Blowfish()
    msg = "Message"
    key = "justineisthebest"

    encrypted = algo.encrypt(msg, key)
    assert encrypted != msg
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == msg


if __name__ == '__main__':
    test_blowfish()
