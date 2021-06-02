import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

__key_num__ = 1024


def create_rsa_key():
    random_generator = Random.new().read
    rsa = RSA.generate(__key_num__, random_generator)

    private_pem = rsa.exportKey()
    with open('private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open('public.pem', 'wb') as f:
        f.write(public_pem)


def RSA_gKey_Encrypt(message):
    with open('public.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的公钥
        cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
        # 加密message明文，python3加密的数据必须是bytes，不能是str
        cipher_text = base64.b64encode(cipher.encrypt(
            message.encode(encoding='utf-8')))
        return cipher_text


def RSA_gKey_Decrypt(cipher_text):
    with open('private.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的私钥
        cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
        # 将密文解密成明文，返回的是bytes类型，需要自己转成str,主要是对中文的处理
        text = cipher.decrypt(base64.b64decode(cipher_text), b'ERROR')
        return text.decode(encoding='utf-8')


if __name__ == '__main__':
    # create_rsa_key()
    a = RSA_gKey_Encrypt('https://api.jp-tok.speech-to-text.watson.cloud.ibm.com/instances/eda25322-4418-4e73-a8d9-f942e6b7f1c4')
    print(RSA_gKey_Decrypt(a))