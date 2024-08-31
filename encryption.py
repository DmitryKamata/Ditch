"""
Используем алгоритм AES и шифруем введенные данные логина и пароля.
Вставляем наш новый 16-байтовый ключ (если требуется) и упаковываем все
это дело в .exe файл.
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Ключ шифрования:
KEY: bytes = b'\x9dy\x04\xb3\xb9\x9c\xa9\x19\xd8\xef\x91\xad\xcb\xa7\x93\x1e'


def aes_encrypt(data: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))

    return base64.standard_b64encode(encrypted_data).decode()


def main():
    print('Введите логин:')
    login = input().strip()
    print('Введите пароль:')
    password = input().strip()

    encrypted_login = aes_encrypt(login, KEY)
    encrypted_password = aes_encrypt(password, KEY)

    print("\nЗашифрованные данные:")
    print(f"Зашифрованный логин: {encrypted_login}")
    print(f"Зашифрованный пароль: {encrypted_password}")


if __name__ == '__main__':
    main()
    input('Для выхода нажмите клавишу Enter...')
