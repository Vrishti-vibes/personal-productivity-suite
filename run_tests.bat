@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Run pytest with coverage
python -m pytest --cov-report term-missing

pause