🚀 Python Mini Projects Collection

📌 Overview

This repository contains a collection of beginner-to-intermediate level Python projects built as part of a BCA (AI & Data Analytics) learning journey. These projects demonstrate practical implementation of core Python concepts, web development, file handling, and basic security.

---

🧠 Projects Included

🔗 1. URL Shortener

A simple web application that converts long URLs into short, manageable links.

Features:

- Generate unique short URLs
- Redirect to original URL
- REST API support using Flask

Tech Used:
Python, Flask

---

📂 2. File Organizer

Automatically organizes files into folders based on their file type.

Features:

- Sort files (Images, PDFs, etc.)
- Automatically creates folders
- Easy file management

Tech Used:
Python (os, shutil)

---

🔐 3. Password Manager

A basic password manager that securely stores and retrieves passwords using encryption.

Features:

- Encrypt passwords
- Decrypt when needed
- Secure storage concept

Tech Used:
Python, Cryptography

---

🎮 4. Quiz Game

A command-line quiz game to test knowledge on various topics.

Features:

- Multiple questions
- Score tracking
- User input handling

Tech Used:
Python (Core Concepts)

---

⚙️ Installation & Setup

🔹 Clone Repository

git clone https://github.com/your-username/python-mini-projects.git
cd python-mini-projects

🔹 Install Dependencies

pip install flask cryptography

---

▶️ How to Run

Run URL Shortener

python app.py

Then open:

http://127.0.0.1:5000

---

🧪 Example API Usage

import requests

url = "http://127.0.0.1:5000/shorten"
data = {"url": "https://www.google.com"}

response = requests.post(url, json=data)
print(response.json())

---

📁 Project Structure

python-mini-projects/
│
├── app.py                 # URL Shortener Flask App
├── file_organizer.py     # File Organizer Script
├── quiz_game.py          # Quiz Game Script
├── password_manager.py   # Password Manager Script
└── README.md             # Project Documentation

---

📊 Learning Outcomes

- Understanding of Python fundamentals
- Web development using Flask
- File handling and automation
- Basic encryption techniques
- API creation and testing

---

🚀 Future Improvements

- Add database (SQLite/MySQL)
- Build frontend UI (Streamlit/React)
- Deploy projects online
- Add authentication system

---

👨‍💻 Author

Your Name
BCA (AI & Data Analytics) Student

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
