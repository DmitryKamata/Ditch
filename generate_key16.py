import hashlib


def generate_key_from_word(word: str) -> bytes:
    return hashlib.sha256(word.encode('utf-8')).digest()[:16]


input_word: str = 'знание'

print(generate_key_from_word(word=input_word))
