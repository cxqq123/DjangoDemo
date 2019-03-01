#coding:utf-8

#pip install pyctyptodome 模块

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64


class AESUtils(object):

    def __init__(self , key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_ECB

    def encrypt(self , text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key , self.mode)
        length = 16
        count = len(text)
        if(count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        # if count < length:
        #     add = length - count
        #     text = text + ('\0' * add).encode('utf-8')
        # elif count > length:
        #     add = (length - (count % length))
        #     text = text + ('\0' * add).encode('utf-8')
        print("add: " , add)
        text = text + ('\0' * add).encode('utf-8')
        print("encrypt : text : " , text)
        ciphertext = cryptor.encrypt(text)
        encrypted_text = str(base64.encodebytes(ciphertext), encoding='utf-8')
        return encrypted_text

    def decrypt(self , text):
        cryptor = AES.new(self.key , self.mode)
        print("decrypt : text :" , text)
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        decrypted_text = str(cryptor.decrypt(base64_decrypted), encoding='utf-8').replace('\0','')
        return decrypted_text

if __name__ == '__main__':
    pc = AESUtils('744cx185185cx744')  # 初始化密钥
    e = pc.encrypt("{\"username\": \"cx3\", \"email\": \"1522321800@qq.com\", \"phone\": \"13710651984\"}")  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)