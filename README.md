# Personal Productivity Suite

## Project Overview

The Personal Productivity Suite is a modular Python-based command-line application that integrates multiple productivity tools including:

- Calculator
- Notes Manager
- Timer
- File Organizer
- Backup System

The application is built using Object-Oriented Programming principles and follows a clean modular architecture.

---

## Objectives

- Demonstrate modular software architecture
- Implement file handling using multiple formats (TXT, JSON, CSV)
- Provide interactive CLI-based user experience
- Ensure robust error handling
- Achieve high unit test coverage using pytest

---

## Features

- Interactive CLI menu system
- File creation and deletion
- Backup management
- Stopwatch timer
- Persistent notes handling
- Comprehensive error validation
- 94% unit test coverage

---

## Installation Guide

### 1. Clone Repository
git clone https://github.com/Vrishti-vibes/personal-productivity-suite.git

cd personal-productivity-suite


### 2. Create Virtual Environment


python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies


pip install -r requirements.txt


### 4. Run Application


python main.py


---

## Run Tests


python -m pytest --cov=modules --cov-report term-missing


---

## Code Structure

- `main.py` → Application entry point
- `modules/` → Individual tool modules
- `tests/` → Unit test suite
- `requirements.txt` → Dependencies
- `.gitignore` → Excludes virtual environment and cache files

---

## Technical Requirements Fulfilled

- Modular architecture with separate modules
- Object-Oriented Design
- File operations (TXT format implemented; extensible to JSON/CSV)
- Error handling for invalid input
- Unit testing with coverage
- CLI-based user-friendly interface

---

## Author

Vrishti

Then:

git add README.md
git commit -m "Updated professional README"
git push
