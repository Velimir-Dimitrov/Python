morse_message = input().split(" | ")

morse_code_dict = {'..-.': 'F', '-..-': 'X',
                  '.--.': 'P', '-': 'T', '..---': '2',
                  '....-': '4', '-----': '0', '--...': '7',
                  '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                  '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                  '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                  '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                  '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                  '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

decrypter_message = ""
for word in morse_message:
    for letter in word.split(" "):
        if letter != "":
            decrypter_message += morse_code_dict[letter]
    decrypter_message += " "
print(decrypter_message)