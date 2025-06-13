# 🏦 Basic Banking System (Python)

A simple command-line banking system built in Python using **Object-Oriented Programming (OOP)** concepts. This project allows users to create and manage bank accounts with basic functionalities like credit, debit, and balance checks.

> ⚠️ **Disclaimer:** This is an educational/demo project. It stores data in memory and does **not** implement encryption, real authentication, or database support.

---

## 🚀 Features

- ✅ Create a new account with a unique account number
- 🔐 Secure login using password authentication
- 💰 Deposit (credit) and withdraw (debit) money
- 📊 Check current account balance
- 🚪 Exit banking session securely

---

## 📂 How It Works

### 1. 🔘 Menu Options
- **Option 1:** Create a new account
- **Option 2:** Login to an existing account

---

### 2. 🆕 Account Creation
- Requires **mobile number** (to avoid duplicates)
- Asks for **name** and **password**
- Generates a **random 4-digit account number**
- Starts with an initial **balance of ₹0**

---

### 3. 🔐 Login
- Enter **account number** and **password**
- On success, access full banking functionalities

---

### 4. 💼 Banking Session Options
- **DEBIT:** Withdraw money (if balance allows)
- **CREDIT:** Deposit money (> ₹0)
- **CHECK BALANCE:** View account balance
- **EXIT:** Log out of session

---

## 🧾 Code Structure

- `Account` class handles:
  - `credit()`
  - `debit()`
  - `bank()` — the main session loop
- `user` dictionary stores all user data (account number as key)
- All data is **stored in-memory** during runtime only

---

## 🛠️ Dependencies

Uses only **standard Python libraries**:
- `random` – for generating unique account numbers
- `time` – to simulate real-time banking delays

> ✅ No external packages or databases required.

---

## 📌 Ideal For
- Beginners learning Python
- Practicing OOP concepts
- Building simple terminal-based applications

---

## 🧠 Learning Outcomes
- OOP fundamentals in Python (classes, objects)
- Control flow using loops and conditionals
- Basic data storage using dictionaries
- Simple input validation and session handling

---

## 🏁 Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/Basic-Banking-System-Python
   cd Basic-Banking-System-Python
