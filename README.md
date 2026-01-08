# 🌸 ShubhSay

**ShubhSay** is an open-source app to organise contacts, create groups, and prepare personalised wishes for any occasion — quickly and effortlessly.

---

## ✨ Why ShubhSay?

On festivals, birthdays, or special occasions, we often want to wish many people — friends, family, relatives, colleagues — but selecting contacts one by one and typing messages repeatedly is time-consuming and tiring.

**ShubhSay simplifies this by:**
- Organising your contacts
- Letting you create groups
- Generating personalised wishes in bulk in just a few clicks

---

## 🚀 Features

- 📥 Import contacts from `.vcf` files  
- 👤 Store full name and multiple phone numbers per contact  
- 💾 Save data in CSV or SQLite  
- 🗂️ Create and manage groups (Friends, Family, Office, etc.)  
- 📝 Create message templates like:
  ```
  Happy Diwali {name}! 🎉
  ```
- 🤖 Auto-generate personalised messages for each contact  
- ⚡ Prepare messages group-wise in one click  

---

## 🧱 Project Scope

- 🐍 Backend in Python (FastAPI)
- 📱 Frontend planned for mobile and web
- ⚠️ Focuses on organising and preparing messages (not illegal automation)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLite / CSV
- VCF parsing libraries

---

## 📁 Planned Structure

```
shubhsay/
  backend/
    app/
        main.py        -> FastAPI entry point
        core/          -> Config, settings, constants
        api/           -> API routes (upload, groups, etc.)
        services/      -> Business logic (VCF parsing, grouping, etc.)
        models/        -> DB models / schemas
        utils/         -> Helper utilities (file parsing, etc.)
  frontend/
  docs/
  README.md
```

---

## 🔐 Privacy First

- 🔒 Your data stays with you
- ☁️ No cloud dependency by default
- 🌍 Fully open-source and transparent

---

## 🧪 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/shubhsay.git
cd shubhsay
```

---

### 2️⃣ Create a Virtual Environment

#### 🪟 On Windows (PowerShell / CMD):

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### ➡️ Deactivate the Virtual Environment

```bash
deactivate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📌 Project Status

🚧 This project is in early development.

---


## 🌼 Meaning of the Name

**Shubh** = Auspicious / Good  
**Say** = To say or to wish  

**ShubhSay** means: *"Say something good"* 🌸

---

## ⭐ Support

If you like this idea, consider starring the repo and contributing!

---

> Built with ❤️ in India 🇮🇳 using Python
