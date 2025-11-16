"""Secure Hugging Face login helper.
Run with the project's venv Python and paste your token when prompted.

Usage (PowerShell):
.\.venv\Scripts\python.exe scripts\hf_login.py

This stores the token using huggingface_hub.login() so the CLI and git helpers can use it.
"""
import getpass
import sys

try:
    from huggingface_hub import login
except Exception as e:
    print("Error: huggingface_hub not installed in this Python environment.")
    print("Install it with: pip install --upgrade huggingface_hub")
    raise

print("Paste your Hugging Face token (input hidden). Press Enter when done.")
token = getpass.getpass(prompt='Token: ')
if not token:
    print("No token provided. Aborting.")
    sys.exit(2)

try:
    login(token=token)
    print("Success: token stored for Hugging Face CLI/Spaces access.")
except Exception as e:
    print("Login failed:", e)
    raise
