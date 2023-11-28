MORSE_CODE_DICT = { 
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.','O': '---',
'P': '.--.', 'Q': '--.-','R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
'5':'.....', '6': '-....', '7':'--...', '8': '---..', '9': '----.', ' ':' '
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += MORSE_CODE_DICT.get(char, char) + ' '
    return morse_code

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code == '':
            text += ' '
        else:
            for k, v in MORSE_CODE_DICT.items():
                if v == code:
                    text += k.lower() if code.islower() else k
                    break
    return text 

# Get user input
user_input = input("Please enter a word or phrase: ")

# Encrypt input to Morse code
encrypted_text = text_to_morse(user_input)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt Morse code back to text       
decrypted_text = morse_to_text(encrypted_text)
print(f"Decrypted Text: {decrypted_text}")    

