# 💰 Expense Tracker MCP Server

A lightweight Expense Tracking MCP (Model Context Protocol) Server built using Python and SQLite. This project is fully integrated with Claude, enabling natural language-based expense management.

---

## 🚀 Features

- Add expenses  
- List expenses by date range  
- Summarize expenses by category  
- Edit existing expenses  
- Delete expenses  
- Load categories from JSON  
- MCP-compatible with Claude  

---

## 🛠️ Tech Stack

- Python  
- SQLite  
- FastMCP  
- Claude (MCP Integration)

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

## 🤖 Claude Integration

This project is integrated with Claude using MCP (Model Context Protocol), allowing you to interact with your expense tracker using natural language.

### What you can do inside Claude:
- "Add ₹500 for food today"
- "Show my expenses for last week"
- "Summarize my spending by category"

Claude automatically calls the MCP tools and returns structured responses.

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

## 🔮 Future Improvements

- Budget tracking  
- Dashboard & analytics  
- Multi-user support  

---
