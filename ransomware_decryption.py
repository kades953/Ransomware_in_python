# This is a ransomware_decryption which decrypts all the encrypted files and folders

import os
from cryptography.fernet import Fernet

files = []

# Let's find all the files

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "ransomware_decryption.py":
		continue

# This loop only finds the files not folders in the current directory
# If you want to find all the files and folders,
# Just remove the line "if os.path.isfile(file):"
# And move the "files.append(file)" line to left as a single indentation is there

	if os.path.isfile(file):
		files.append(file)

print(files)

# Read the key from thekey.key

with open("thekey.key", "rb") as key:
	secretKey = key.read()

# Decrypting the files/folders by telling the secret word

secretWord = "kades"

user_word = input("Enter the secret word to decrypt your files\n")

if user_word == secretWord:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretKey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats, Your files are decrypted!")
else:
	print("Sorry, Wrong Password!")
