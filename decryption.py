"""
Вставляем наш новый ключ для дешифровки(если требуется).
Для проверки вставляем зашифрованное значение в encrypted_str и выполняем файл.
Получаем исходное значение.
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Ключ шифрования:
KEY: bytes = b'\x9dy\x04\xb3\xb9\x9c\xa9\x19\xd8\xef\x91\xad\xcb\xa7\x93\x1e'


def aes_decrypt(encrypted_data: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_encrypted_data = base64.standard_b64decode(encrypted_data)

    decrypted_data = unpad(cipher.decrypt(decoded_encrypted_data), AES.block_size)
    return decrypted_data.decode()


# Далее все для проверки корректности дешифровки
encrypted_str = 'zwubY/C15yhaFUxfhuFJc/vqMR2+JiXBesKIRnIURRU='

decrypted_str = aes_decrypt(encrypted_data=encrypted_str, key=KEY)
print(f'Исходные данные после расшифровки: {decrypted_str}')
