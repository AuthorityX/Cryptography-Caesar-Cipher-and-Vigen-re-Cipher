# Cryptography: Caesar Cipher and Vigenère Cipher

## Description

This Python project implements two classic cryptographic methods: the Caesar Cipher and the Vigenère Cipher. These ciphers are fundamental in the study of cryptography and provide a foundational understanding of how encryption and decryption can be achieved through simple algorithms.

## Features

- **Caesar Cipher:** Implements both encoding and decoding functions for the Caesar Cipher, which shifts each letter in the plaintext by a fixed number of positions.
- **Vigenère Cipher:** Includes functions to encrypt and decrypt using the Vigenère Cipher, a more sophisticated encryption method that uses a keyword to determine the shift for each letter.

## How to Use

1. **Caesar Cipher:**
   - To encode a message: `caesar_encode('your message', offset)`
   - To decode a message: `caesar_decode('encoded message', offset)`

2. **Vigenère Cipher:**
   - To encrypt a message: `vig_encryption('your message', 'keyword')`
   - To decrypt a message: `vig_cihper('encrypted message', 'keyword')`

Replace `'your message'` with the text you wish to encrypt or decrypt, `'encoded message'` with the text to be decoded, `'encrypted message'` with the text to be decrypted, `'keyword'` with your chosen keyword, and `offset` with the numerical shift for the Caesar Cipher.

## Implementation Details

- The Caesar Cipher functions shift each letter by a specified number of positions in the alphabet. The `caesar_encode` function can be used to both encode and decode by adjusting the offset.
- The Vigenère Cipher functions utilize a keyword to create a more secure encryption. Each letter of the plaintext is shifted according to the corresponding letter in the keyword.

## Usage Examples

```python
# Caesar Cipher
encoded_message = caesar_encode('hello world', 3)
decoded_message = caesar_decode(encoded_message, 3)

# Vigenère Cipher
encrypted_message = vig_encryption('hello world', 'key')
decrypted_message = vig_cihper(encrypted_message, 'key')
```

## Contributing

Feel free to fork this repository and contribute to the project. Whether it's adding new features, improving the code, or fixing bugs, your contributions are welcome.

## License

This project is open-sourced under the MIT License.

## Notes

- This implementation is meant for educational purposes and should not be used for secure encryption needs.
- Ensure that the input messages are in lowercase and do not contain special characters for optimal performance.

This README provides a comprehensive guide for users to understand and interact with your cryptography project. It can be placed in the root directory of your GitHub repository to serve as the first point of information for anyone visiting your project.
