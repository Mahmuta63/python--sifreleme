def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Lütfen şifrelenecek metni girin: ")
shift = int(input("Lütfen Sezar şifreleme için kaydırma miktarını girin: "))

atbash_encrypted = atbash_cipher(text)
caesar_encrypted = caesar_cipher(atbash_encrypted, shift)

print("Şifrelenmiş metin:", caesar_encrypted)

caesar_decrypted = caesar_cipher(caesar_encrypted, -shift)
atbash_decrypted = atbash_cipher(caesar_decrypted)

print("Çözülmüş metin:", atbash_decrypted)