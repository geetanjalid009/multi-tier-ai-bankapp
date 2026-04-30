from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Multi-Tier AI BankApp Backend is Running",
        "routes": ["/health", "/accounts", "/ai-chat"]
    })

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "bankdb")
DB_USER = os.getenv("DB_USER", "bankuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "bankpass")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/health")
def health():
    return jsonify({"status": "Backend is healthy"})

@app.route("/accounts")
def accounts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, customer_name, balance FROM accounts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "customer_name": row[1],
            "balance": float(row[2])
        })

    return jsonify(data)

@app.route("/transactions")
def transactions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, account_id, transaction_type, amount FROM transactions;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "account_id": row[1],
            "transaction_type": row[2],
            "amount": float(row[3])
        })

    return jsonify(data)

@app.route("/ai-chat", methods=["POST"])
def ai_chat():
    user_message = request.json.get("message", "")

    response = {
        "user_message": user_message,
        "ai_response": "This is a mock AI banking assistant response. Real LLM integration will be added later."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)