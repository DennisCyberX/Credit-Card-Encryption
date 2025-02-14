```python
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    credit_card_number = input("Enter credit card number: ")
    encrypted = encrypt_data(credit_card_number)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_data(encrypted)
    print(f"Decrypted: {decrypted}")
