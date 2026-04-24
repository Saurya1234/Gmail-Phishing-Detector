# Gmail Phishing Detector

A modern Python-based phishing detection project that scans suspicious email content using a FastAPI backend and web frontend.

This project helps identify phishing emails by checking:

* Suspicious keywords
* Malicious URLs
* IP-based links
* Dangerous domains (`.xyz`, `.top`, `.tk`)
* Risk score calculation

---

# Features

## Backend (FastAPI)

* REST API with `/scan`
* JSON input/output
* Automatic Swagger docs
* Fast scoring engine

## Frontend

* Beautiful dark dashboard
* Gmail login UI (email + app password fields)
* Manual Email Scan
* Live API communication
* Risk result display

---

# Technologies Used

```text id="n1"
Python
FastAPI
Uvicorn
HTML
CSS
JavaScript
```

---

# Project Structure

```text id="n2"
gmail-phishing-detector/
│── backend/
│   ├── main.py
│   └── detector.py
│
│── frontend/
│   └── index.html
│
│── venv/
│── README.md
```

---

# Installation Guide (Kali Linux / Ubuntu)

## 1. Clone or Open Project

```bash id="n3"
cd ~/gmail-phishing-detector
```

---

## 2. Create Virtual Environment

```bash id="n4"
python3 -m venv venv
```

Activate:

```bash id="n5"
source venv/bin/activate
```

---

## 3. Install Packages

```bash id="n6"
python -m pip install fastapi uvicorn
```

---

# Run Backend API

```bash id="n7"
cd backend
python -m uvicorn main:app --reload
```

Backend runs on:

```text id="n8"
http://127.0.0.1:8000
```

Swagger docs:

```text id="n9"
http://127.0.0.1:8000/docs
```

---

# Run Frontend UI

Open another terminal:

```bash id="n10"
cd frontend
python3 -m http.server 5500
```

Then open browser:

```text id="n11"
http://127.0.0.1:5500
```

---

# How To Use

## Manual Email Scan

Paste suspicious email content into the text box.

Example:

```text id="n12"
Urgent verify your account now
Click here:
http://123.45.67.89/login
```

Click:

```text id="n13"
Scan Email
```

---

# Example Output

```json id="n14"
{
  "score": 50,
  "status": "suspicious",
  "reasons": [
    "Keyword: urgent",
    "Keyword: verify",
    "Suspicious URL: http://123.45.67.89/login"
  ]
}
```

---

# Score System

## Keywords

Each suspicious keyword adds:

```text id="n15"
+10 points
```

Keywords:

```text id="n16"
urgent
verify
suspended
login now
click here
password reset
bank alert
```

---

## URLs

Suspicious URLs add:

```text id="n17"
+30 points
```

Examples:

```text id="n18"
http://123.45.67.89/login
fakebank.xyz
securemail.top
```

---

# Risk Levels

```text id="n19"
0–19   Safe
20–39  Low Risk
40–59  Suspicious
60+    Malicious
```

---

# Gmail Login Section

Frontend includes:

* Gmail address field
* App password field
* Connect Gmail button

This is for future Gmail live inbox scanning integration.

---

# How To Generate Gmail App Password

1. Enable Google 2-Step Verification
2. Open Google Account Security
3. Search **App Passwords**
4. Generate password for Mail
5. Use generated 16-character password

---

# Future Upgrades

* Live Gmail inbox scanning
* Auto phishing alerts
* VirusTotal API integration
* Telegram notifications
* SQLite logging
* Charts dashboard
* AI phishing detection

---

# Security Warning

Never upload real Gmail passwords or App Passwords to GitHub.

Use:

```text id="n20"
.env
environment variables
```

---

# GitHub Ready

Recommended repo name:

```text id="n21"
gmail-phishing-detector
```

---

# Author

Built as a cybersecurity Python project for phishing detection, email security, and portfolio development.

---

# License

MIT License
