from string import ascii_letters


def cipher(text, shift, decode=False):
    result = ''
    for i in text:
        result += ascii_letters[ascii_letters.index(i) - shift] if decode \
            else ascii_letters[ascii_letters.index(i) + shift]

    return result


message = 'Hello'
encoded_message = cipher(message, 1)
print(f'Encoded message {message}', encoded_message)

print(f'Decoded message {encoded_message}', cipher(encoded_message, 1, decode=True))
