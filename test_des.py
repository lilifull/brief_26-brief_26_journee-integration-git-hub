from crypto_app.des_algo import DES


def test_des():

    algo = DES()
    msg = "Message"
    key = "adtjcopr"

    encrypted = algo.encrypt(msg, key)
    #print(encrypted)
    assert encrypted == "18888565fbd90544"
    decrypted = algo.decrypt(encrypted, key)
    #print(decrypted)
    assert decrypted == "Message"

if __name__ == '__main__':
    test_des()