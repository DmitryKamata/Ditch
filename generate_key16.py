"""
Вводим набор символов в input_word по которым через хэш-функцию получим 16-байт.
Это будет наш ключ.
"""
import hashlib


def generate_key_from_word(word: str) -> bytes:
    return hashlib.sha256(word.encode('utf-8')).digest()[:16]


input_word: str = 'Скуфа любят все'

print(generate_key_from_word(word=input_word))
