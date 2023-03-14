from crypto_app.des_algo import DES


def test_des():

    algo = DES()
    msg = "Message"
    key = "adtjcopr"
    result = "18888565fbd90544"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == result
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == msg


if __name__ == '__main__':
    test_des()
  