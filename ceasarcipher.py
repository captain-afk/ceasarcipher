import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shiftWord(secretWord,shiftAmount,seed = 10):        # The function shuffles the alphabet, using a set seed that the user chooses. Then shifts along the index to jumble up the word
    random.seed(int(seed))                              # Encrypting and decrypting is the same function. Just need to shift the opposite direction to decrypt
    random.shuffle(alphabet)                            # So to decrypt, you need to know how far to shift, and what seed was chosen
    encryptedWord = ""
    for x in secretWord.lower():
        if x == ' ':
            encryptedWord += x
        else:
            indexAlphabet = alphabet.index(x)
            newLetter = (indexAlphabet + int(shiftAmount)) % 26
            encryptedWord += alphabet[newLetter]
    return(encryptedWord)

def main():
    print("Would you like to 'encrypt' or 'decrypt' a word?:")
    command = input()

    if command.lower() == 'encrypt':                    # The only difference between encrypt and decrypted is the phrases that are printed
        startMessage = "What word or phrase would you like to encrypt?"
        endMessage = "Here it is encrypted:"

    elif command.lower() == 'decrypt':
        startMessage = "What word or phrase would you like to decrypt?"
        endMessage = "Here it is decrypted:"

    print(startMessage)
    secretWord = input()
    print("How much did you need to shift the word by? (negative numbers shift to the left, positive shift to the right)")
    shiftAmount = input()
    print("What is your secret number? (this sets the random seed)")
    setSeed = input()
    shiftedWord = shiftWord(secretWord,shiftAmount,setSeed)
    print(endMessage,shiftedWord)

main()