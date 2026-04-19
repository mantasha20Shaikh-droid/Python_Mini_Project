# Python Mini Projects Notebook
# Name: Mantasha Md Anish Shaikh 
# Course: BCA AI & Data Analytics
# Project: Multiple Python Projects Implementation


!pip install flask cryptography

from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)
url_db = {}

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return "URL Shortener Running!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json.get("url")
    code = generate_code()
    url_db[code] = long_url
    
    return jsonify({"short_url": f"http://localhost:5000/{code}"})

@app.route('/<code>')
def redirect_url(code):
    if code in url_db:
        return redirect(url_db[code])
    return "URL not found!"

from threading import Thread

def run_app():
    app.run(port=5000)

Thread(target=run_app).start()

import requests

url = "http://127.0.0.1:5000/shorten"
data = {"url": "https://www.google.com"}

response = requests.post(url, json=data)
print(response.json())

import os
import shutil

# Create test folder
os.makedirs("test_folder", exist_ok=True)

# Create sample files
open("test_folder/file1.jpg", "w").close()
open("test_folder/file2.pdf", "w").close()

# Create folders
os.makedirs("test_folder/Images", exist_ok=True)
os.makedirs("test_folder/PDFs", exist_ok=True)

# Organize files
for file in os.listdir("test_folder"):
    if file.endswith(".jpg"):
        shutil.move("test_folder/" + file, "test_folder/Images/" + file)
    elif file.endswith(".pdf"):
        shutil.move("test_folder/" + file, "test_folder/PDFs/" + file)

print("Files organized successfully!")

questions = {
    "Python is a language? (yes/no)": "yes",
    "5 + 5 = ?": "10",
    "AI stands for?": "artificial intelligence"
}

score = 0

for q, ans in questions.items():
    user = input(q + " ")
    if user.lower() == ans:
        score += 1

print("Final Score:", score)

from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

# Store password
password = "mysecret123"
encrypted = cipher.encrypt(password.encode())

print("Encrypted:", encrypted)

# Decrypt password
decrypted = cipher.decrypt(encrypted).decode()
print("Decrypted:", decrypted)

print("""
This notebook includes:
1. URL Shortener using Flask
2. File Organizer using OS & Shutil
3. Quiz Game using Python basics
4. Password Manager with Encryption

These projects demonstrate practical Python skills.
""")
