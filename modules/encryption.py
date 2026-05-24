import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

#symmetric encryption
def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce,message.encode(), None)
    plaintext = aes.decrypt(ciphertext[:12],ciphertext[12:],None)
    return key.hex(), ciphertext.hex(),plaintext.hex(),plaintext.decode()

#asymmetric encryption
def rsa_ed(message):
    privatekey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048)
    publickey = privatekey.public_key()

#encryption using Public key
    ciphertext = publickey.encrypt(
        message.encode(),
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label = None
        )
    )

#decryption using Private key
    plaintext = privatekey.decrypt(
        ciphertext,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label = None
        )
    )

    return ciphertext.hex(),plaintext.decode()

if __name__ == "__main__":
    print(aes_ed("This is the input for the AES encryption function."))
    print(rsa_ed("This is the input for the RSA encryption function."))