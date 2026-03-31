from fastmcp import FastMCP
import sqlite3
import os

# File paths
DB_PATH = "expenses.db"
CATEGORIES_PATH = "categories.json"

# Create MCP app
mcp = FastMCP("ExpenseTracker")


# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            subcategory TEXT,
            note TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()


# Add expense
@mcp.tool()
def add_expense(date, amount, category, subcategory="", note=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (date, amount, category, subcategory, note) VALUES (?, ?, ?, ?, ?)",
        (date, amount, category, subcategory, note)
    )

    conn.commit()
    expense_id = cursor.lastrowid
    conn.close()

    return {"status": "ok", "id": expense_id}


# List expenses
@mcp.tool()
def list_expenses(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, date, amount, category, subcategory, note
        FROM expenses
        WHERE date BETWEEN ? AND ?
    """, (start_date, end_date))

    rows = cursor.fetchall()
    conn.close()

    # Convert to list of dictionaries
    result = []
    for row in rows:
        expense = {
            "id": row[0],
            "date": row[1],
            "amount": row[2],
            "category": row[3],
            "subcategory": row[4],
            "note": row[5]
        }
        result.append(expense)

    return result


# Summarize expenses
@mcp.tool()
def summarize(start_date, end_date, category=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if category:
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            WHERE date BETWEEN ? AND ? AND category = ?
            GROUP BY category
        """, (start_date, end_date, category))
    else:
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            WHERE date BETWEEN ? AND ?
            GROUP BY category
        """, (start_date, end_date))

    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "category": row[0],
            "total_amount": row[1]
        })

    return result

@mcp.tool()
def edit_expense(expense_id, date, amount, category, subcategory="", note=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if expense exists
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    data = cursor.fetchone()

    if data is None:
        conn.close()
        return {"status": "error", "message": "Expense not found"}

    # Update expense
    cursor.execute("""
        UPDATE expenses
        SET date = ?, amount = ?, category = ?, subcategory = ?, note = ?
        WHERE id = ?
    """, (date, amount, category, subcategory, note, expense_id))

    conn.commit()
    conn.close()

    return {"status": "updated", "id": expense_id}

@mcp.tool()
def delete_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if expense exists
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    data = cursor.fetchone()

    if data is None:
        conn.close()
        return {"status": "error", "message": "Expense not found"}

    # Delete expense
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()

    return {"status": "deleted", "id": expense_id}


# Read categories file
@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    file = open(CATEGORIES_PATH, "r", encoding="utf-8")
    data = file.read()
    file.close()
    return data


# Run server
if __name__ == "__main__":
    mcp.run()