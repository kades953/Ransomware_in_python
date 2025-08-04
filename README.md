# 🔐 Python Ransomware Simulation (Encryption + Decryption)

> ⚠️ **DISCLAIMER:** This project is intended strictly for educational purposes and ethical cybersecurity training in isolated lab environments. Do not use this code for malicious purposes.

## 📌 Overview

This repository contains a simple Python-based ransomware simulation that can **encrypt** and **decrypt** files within the same directory. It is designed to help students, security enthusiasts, and ethical hackers understand how file encryption-based ransomware operates.

The simulation uses Python's `cryptography` library and is split into two scripts:
- `ransomware.py` — Encrypts files and saves a generated key
- `ransomware_decryption.py` — Decrypts the files using the key and a user-defined secret word

## 🔧 How It Works

### Encryption Phase (`ransomware.py`)
- Searches for all non-directory files in the current working directory (excluding key/script files).
- Generates a symmetric encryption key using `Fernet`.
- Saves the key in a file named `thekey.key`.
- Encrypts the contents of each file and overwrites them with encrypted data.
- Prints: `"Your all files are encrypted!"`

### Decryption Phase (`ransomware_decryption.py`)
- Reads `thekey.key` to load the original symmetric key.
- Prompts the user to enter a secret word (`"kades"` by default).
- If correct, it decrypts all files that were previously encrypted.
- If incorrect, it aborts the decryption with an error message.

## 🧪 File Structure

```bash
.
├── ransomware.py               # Encrypts files in current directory
├── ransomware_decryption.py    # Decrypts previously encrypted files
├── thekey.key                  # Generated automatically during encryption
├── [your_test_files...]        # Example files you want to encrypt/decrypt
