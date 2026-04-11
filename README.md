# 💰 Expense Tracker MCP Server

A lightweight Expense Tracking MCP (Model Context Protocol) Server built using Python and SQLite. This project allows seamless expense management and integrates with AI assistants like Claude.

---

## 🚀 Features

- Add expenses  
- List expenses by date range  
- Summarize expenses by category  
- Edit existing expenses  
- Delete expenses  
- Load categories from JSON  
- MCP-compatible (Claude / AI agents)

---

## 🛠️ Tech Stack

- Python  
- SQLite  
- FastMCP  

---

## 📁 Project Structure

.
├── expenses.db  
├── categories.json  
├── main.py  
└── README.md  

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/expense-tracker-mcp.git
cd expense-tracker-mcp
pip install fastmcp
python main.py
```

---

## 🧠 MCP Tools

- add_expense(date, amount, category, subcategory="", note="")
- list_expenses(start_date, end_date)
- summarize(start_date, end_date, category=None)
- edit_expense(expense_id, date, amount, category, subcategory="", note="")
- delete_expense(expense_id)

---

## 📂 Resource

expense://categories → Returns categories from JSON

---

## 🧾 Database Schema

CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    amount REAL,
    category TEXT,
    subcategory TEXT,
    note TEXT
);

---

## 🤖 Use Cases

- Add expenses via AI  
- Track spending  
- Get summaries  

---
