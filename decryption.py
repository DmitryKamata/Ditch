from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Ключ шифрования:
KEY: bytes = b'\x8a9\xda7\xf6\xadN\xe7\xc5\xf1\xc3\xbf\x97W\xeaF'


def aes_decrypt(encrypted_data: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_encrypted_data = base64.standard_b64decode(encrypted_data)

    decrypted_data = unpad(cipher.decrypt(decoded_encrypted_data), AES.block_size)
    return decrypted_data.decode()


encrypted_str = 'zwubY/C15yhaFUxfhuFJc/vqMR2+JiXBesKIRnIURRU='

decrypted_str = aes_decrypt(encrypted_data=encrypted_str, key=KEY)
print(f'Исходные данные после расшифровки: {decrypted_str}')
