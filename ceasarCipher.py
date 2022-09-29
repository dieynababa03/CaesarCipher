import string
# Function to encode word
def encrypt(text, shift):
  encrypted = []
  # Generating alphabet
  alphabet = list(string.ascii_lowercase)
  for index in range(len(text)):
    # Setting letter equal to and index of text
    letter = text[index]
    # Setting the index to encode the letter equal
    # to the index of the letter + shift
    encodedIndex = alphabet.index(letter) + shift
    # If my index exceeds the last letter of the alphabet
    if(encodedIndex > 25):
      encodedIndex -= 26
    encrypted.append(alphabet[encodedIndex])
    # Printing the word
    print(encrypted[index], end="")


    
def decrypt(text, shift):
  decrypted = []
  alphabet = list(string.ascii_lowercase)
  for index in range(len(text)):
    letter = text[index]
    decodedIndex = alphabet.index(letter) - shift
    if(decodedIndex < 0):
      decodedIndex += 26
    decrypted.append(alphabet[decodedIndex])
    print(decrypted[index], end="")
      

gameLoop = True
# Taking in user input
while gameLoop:
  direction = input("Type 'encode' to encode, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # if statement to either encode or decode
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
  else:
    print("Invalid input")
  goAgain = input("Do you want to play again? 'yes' or ' no' ")
  if goAgain == "no":
    print("Thanks for playing!")
    gameLoop = False

