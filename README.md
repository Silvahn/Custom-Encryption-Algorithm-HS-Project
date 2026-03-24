# Custom-Encryption-Algorithm-HS-Project
AKA Piercon Encryption Algorithm
Overview

This project is a custom encryption algorithm built in Python for a high school cybersecurity course. It demonstrates how layered transformations and randomness can be used to obscure data and simulate core ideas behind encryption systems.

The focus of this project is on problem-solving, algorithm design, and understanding tradeoffs, rather than creating production-level security.

Features
Multi-step encryption pipeline
Reversible transformations (encryption + decryption)
Randomized obfuscation using a user-defined key
ASCII-based encoding and decoding
Technologies Used
Python
How It Works

The algorithm processes a message through several stages:

1. ASCII Transformation

Each character is converted to its ASCII value and increased by 100:

char → ASCII → ASCII + 100


2. Obfuscation
All ASCII values are concatenated into a string
Random digits are inserted:
At the beginning
Between each digit of the message
The number of random digits added is determined by a user-provided key


3. Pair Encoding
The numeric string is split into pairs of digits
Each pair is converted back into a character using ASCII (+22 shift)
This produces the final encrypted message


4. Decryption Process

The process is reversed:

Convert characters back to numbers
Remove +22 shift
Strip out random digits using the key
Reconstruct ASCII values
Subtract 100 and convert back to original characters


Example
Input:  Hello
Key:    2
Output (Encrypted):  [varies due to randomness]
Output (Decrypted):  Hello


Key Concepts Demonstrated
Data transformation and encoding
Use of randomness for obfuscation
Reversible algorithm design
Multi-step problem decomposition


Limitations
Not secure for real-world use
Predictable structure despite randomness
Inefficient due to string concatenation and repeated processing

This project is intended for educational purposes to explore how encryption-like systems can be constructed and analyzed.

What I Learned
How to break complex problems into sequential transformations
Designing reversible algorithms
Debugging multi-step data pipelines
Collaborating on technical problem-solving
Evaluating tradeoffs between simplicity, performance, and security

Future Improvements
Improve efficiency using better data structures
Reduce predictability in the encoding process
Implement standard cryptographic techniques for comparison
Refactor code for readability and maintainability
Author

Developed by Connor and Pierce as part of a cybersecurity course project.

Feel free to explore the code and experiment with different keys and inputs to see how the algorithm behaves.
