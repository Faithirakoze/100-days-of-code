import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code_list = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code_list)

generate_phonetic()

# while True:
#     try:
#         user_input = input("Enter a word: ").upper()
#         phonetic_code_list = [nato_alphabet[letter] for letter in user_input]
#         print(phonetic_code_list)
#         break
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
