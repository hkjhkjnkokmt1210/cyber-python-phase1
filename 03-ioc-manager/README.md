# Target & IOC Manager

A persistent command-line utility built with Python OOP, `pathlib`, and JSON storage to manage Indicators of Compromise (IOCs).

## Features
- Automatically loads existing IOC records from JSON or initializes a clean store with exception handling (`try/except`).
- Supports adding, case-insensitive searching, and exact removal of IOC entries.
- Persists changes immediately to local JSON storage.

## Usage
```bash
python manager.py