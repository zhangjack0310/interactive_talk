from hashlib import md5

def md5_encrypt(data):
    m = md5()
    m.update(data)
    return m.hexdigest()
