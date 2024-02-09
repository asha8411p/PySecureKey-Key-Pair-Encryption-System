from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# In essence, the initiator generates the key pair and distributes the public key for encrypting data, maintaining exclusive control over the private key to decrypt the data securely.
# The integrity of this encryption process relies heavily on the private key being kept in a secure location and never compromised, underlining its importance in the secure communication channel.


# Generate a private key for RSA encryption
private_key = rsa.generate_private_key(     
    public_exponent=65537,                  # Exponent used to decode the original value
    key_size=2048,                          # Specifies the key size in bits. A size of 2048 bits offers a good balance between security and performance.                        
)

# Serialize the private key to the PEM format for secure storage
priv_pem = private_key.private_bytes(               # PEM stands for privacy enhanced mail. PEM format is widely used for storing keys. 
    encoding = serialization.Encoding.PEM,          # serialize the key for storage
    format = serialization.PrivateFormat.TraditionalOpenSSL,    # OpenSSL's traditional format for private keys.
    encryption_algorithm = serialization.NoEncryption()         # No additional encryption on the key itself.
)

with open('priv_pem', 'wb') as priv_pem_file:               # Write the private key to a file for later use
    priv_pem_file.write(priv_pem)                   

public_key = private_key.public_key()                       # Extract the public key from the private key

# Serialize the public key to the PEM format for sharing with other users

pub_pem = public_key.public_bytes(
    encoding = serialization.Encoding.PEM, 
    format = serialization.PublicFormat.SubjectPublicKeyInfo    # Standard format for public keys.
)

with open('pub_pem', 'wb') as pub_pem_file:         # Write the public key to a file for distribution
    pub_pem_file.write(pub_pem)         