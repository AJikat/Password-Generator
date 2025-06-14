# Password Generator (Python)

A simple, secure random‐password generator in Python that:
- Ensures at least one uppercase, one lowercase, one digit, and one symbol.
- Avoids sequential characters (e.g. “abc”, “123”, or their reversals).
- Uses configurable length (default 16, minimum recommended 8).

## Features

- **Entropy-rich**: mixes char types and shuffles.
- **No simple patterns**: filters out runs like `abc`, `123`, `321`, etc.
- **Interactive CLI**: generate new passwords in a loop or exit.

## Requirements

- Python 3.6+
- No external libraries (only built‑ins: `string`, `re`, `random`).

## Usage

```bash
python password_generator.py

## Author

Created by **Adam Jikat**  
Feel free to connect with me on [LinkedIn](www.linkedin.com/in/adam-jikat-48635b2a5)
