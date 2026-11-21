# Password Strength & Hash Checker

A Python utility built with Object-Oriented Programming (OOP) to audit password policy compliance and generate cryptographic SHA-256 hashes.

## Features
- Evaluates password complexity against configurable minimum length, uppercase letters, digits, and special characters.
- Classifies password strength into `WEAK`, `MEDIUM`, and `STRONG`.
- Computes SHA-256 cryptographic digests using Python's built-in `hashlib` module.

## Usage
```bash
python auditor.py