from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

import sys, os

if(len(sys.argv)) != 2:
    print('Usage: ./decrypt.py original_filename')
    exit(-1) # Exit the script if the incorrect number of arguments is provided

# Open and read the encrypted file
with open(sys.argv[1]+'.encrypted', 'rb') as encrypt_file:
    encrypted = encrypt_file.read()

# Retrieve the private key file path from an environment variable or use the default
priv_pem = os.environ.get('PEMK', 'priv_pem')

# Load the private key for decryption
with open('E:\Coding\Python Projects\priv_pem', 'rb') as key_file:              # Adjust the hardcoded path according to your setup or use the variable
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password = None                                                          # Assumes the private key is not password protected
        )


# Decrypt the data with the private key using OAEP padding and SHA-256 for hashing
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),          # Use SHA-256 as the hash function for the mask generation function
        algorithm = hashes.SHA256(),                            # Use SHA-256 as the hashing algorithm
        label = None                                            # 'label' is optional and not used here
    )
)

# Save the decrypted data to a new file with '.decrypted' extension
with open(sys.argv[1]+'.decrypted', 'wb') as file:
    file.write(decrypted)

