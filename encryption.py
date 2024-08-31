from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import standard_b64encode

# Ключ шифрования:
KEY: bytes = b'\x8a9\xda7\xf6\xadN\xe7\xc5\xf1\xc3\xbf\x97W\xeaF'


def aes_encrypt(data: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))

    return standard_b64encode(encrypted_data).decode()


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