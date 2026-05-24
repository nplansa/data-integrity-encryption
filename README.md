Data Integrity & Encryption Toolkit

A simple Python utility that demonstrates how to secure data using modern cryptographic standards. It covers two main areas
1. verifying file integrity (Hashing) 
2. keeping data private (Encryption).

## 🛠️ Key Features

1. File Integrity Checks (`SHA-256`):
   Reads files in small chunks (1024 bytes) to safely calculate hashes for large files without running out of computer memory.
2. Symmetric Encryption (`AES-GCM`):
   Fast encryption for text payloads using a secure 256-bit key and a unique randomized tracker (`nonce`) for every message.
3. Asymmetric Encryption (`RSA-OAEP`)
   Secure key exchange using a 2048-bit Public/Private keypair with modern, safe padding.

---

## 📁 Project Structure

```text
data-integrity-encryption/
├── modules/
│   ├── hash.py            # SHA-256 file hashing logic
│   └── encryption.py      # AES-GCM and RSA-OAEP logic
├── sample_files/
│   ├── sample.text        # Original test file
│   └── sample2.text       # Modified test file
├── main.py                # Main script to run the project
└── .gitignore             # Tells Git to ignore background clutter
