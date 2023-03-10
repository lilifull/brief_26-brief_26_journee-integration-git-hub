from crypto_app.md5_algo import MD5

def test_md5():

    algo = MD5()
    msg = "Message"
    key = "adtjcopr"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == "4c2a8fe7eaf24721cc7a9f0175115bd4"
    #print(encrypted)
    decrypted = algo.decrypt(encrypted, key)
    #print(decrypted)
    assert decrypted == False

if __name__ == '__main__':
    test_md5()