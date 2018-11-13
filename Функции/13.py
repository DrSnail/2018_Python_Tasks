print("Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, "
      "и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) "
      "над символами строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной "
      "строке и ключу восстанавливает исходную строку.")


def XOR_cipher(string, key):
    chip = ""
    for letter in string:
        chip += chr(ord(letter) ^ key)
    # string = string.encode()
    # string = int.from_bytes(string, 'big')
    return chip

def XOR_unchiper(string, key):
    # print(chip.bit_length())a asdk
    # return chip.to_bytes((chip.bit_length() + 7) // 8, 'big').decode()
    return XOR_cipher(string, key)

inp = input("Input string to encript = ")
key = input("Input key = ").encode()
key = int.from_bytes(key, 'big')
chip = XOR_cipher(inp, 2)
print(chip)
chip = XOR_unchiper(chip, 2)
print(chip)