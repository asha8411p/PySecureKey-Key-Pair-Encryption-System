# PySecureKey-Key-Pair-Encryption-System

Safeguard your sensitive data with the RSA Encryption &amp; Decryption Utility. Developed using Python and the cryptography library, this tool provides robust RSA encryption to ensure secure handling of your files.

## Features

- RSA encryption and decryption.
- Supports encryption and decryption of any file type.

## Setting Up

- **Clone this repository** to your local machine.
- Ensure you have **Python** and **pip** installed.
- **Install the required library** using pip:
```bash
pip install cryptography 
```
## RSA Encryption & Decryption Utility

Generate an RSA key pair and store them as `priv_pem` and `pub_pem` files in your project directory. You can use the provided scripts to generate these keys.

## Usage

### Encrypting a File

To encrypt a file, you will need the public key (`pub_pem`). Use the `encrypt.py` script as follows:

```bash
python encrypt.py <path_to_file>
```
This will create an encrypted version of the file with the .encrypted extension.

## Decrypting a File

To decrypt a file, you will need the private key (`priv_pem`). Use the `decrypt.py` script as follows:

```bash
python decrypt.py <path_to_encrypted_file>
```
This will create a decrypted version of the file with the .decrypted extension.

## Configuration

The `encrypt.py` and `decrypt.py` scripts use environment variables to locate the public and private key files, respectively.

By default, these are named `pub_pem` and `priv_pem`.

If you store your keys in different files or locations, you can set the `PUB_PEMK` and `PEMK` environment variables to point to the correct files.

## Security

- Never share your private key (`priv_pem`).
- Always ensure your public key (`pub_pem`) is distributed securely to your intended audience.
