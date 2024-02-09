from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

import sys, os

if(len(sys.argv)) != 2:
    print('Usage: ./encrypt.py original_filename')
    exit(-1)                                            # Exit if the number of arguments is incorrect


# Open and read the original file to be encrypted
with open(sys.argv[1], 'rb') as org_file:
    org_data = org_file.read()

# Retrieve the public key file path from an environment variable or default to 'pub_pem'
pub_pem = os.environ.get('PUB_PEMK','pub_pem')    # Load the public key for encryption

with open('E:\Coding\Python Projects\pub_pem', 'rb') as pub_key_file:      # Ensure to adjust the hardcoded path according to your environment or use the variable above
    public_key = serialization.load_pem_public_key(
        pub_key_file.read()
        )

# Encrypt the data with the public key using OAEP padding and SHA-256 for hashing
encrypted = public_key.encrypt(
    org_data,
    padding.OAEP(                                           # Optimal Asymmetric Encryption Padding should be used for RSA encryption 
    mgf = padding.MGF1(algorithm = hashes.SHA256()),        # mgf (mask generation function) produces a mask that is associated with the size of the input data
    algorithm= hashes.SHA256(),                             # hashes.256() produces a hash (message digest) to check that the sent message is unaltered, but in itself is of fixed size (in this case 256 bits). 
    label = None                    # 'label' can be used in certain scenarios for additional security, here it is not used.
    )
)

# Save the encrypted data to a new file with '.encrypted' extension
with open(sys.argv[1]+'.encrypted', 'wb') as file:
    file.write(encrypted)