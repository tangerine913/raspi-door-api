import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# DB初期化
def init_db():
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            touch TEXT,
            switch TEXT
        )
    """)
    cur.execute(
        "INSERT OR IGNORE INTO messages (id, touch, switch) VALUES (1, '初回ドアです', '最終ゲートです')"
    )
    conn.commit()
    conn.close()

init_db()

# POST
@app.route("/set_message", methods=["POST"])
def set_message():
    data = request.json

    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    if "touch" in data:
        cur.execute("UPDATE messages SET touch=? WHERE id=1", (data["touch"],))
    if "switch" in data:
        cur.execute("UPDATE messages SET switch=? WHERE id=1", (data["switch"],))

    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})

# GET
@app.route("/get_message", methods=["GET"])
def get_message():
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    cur.execute("SELECT touch, switch FROM messages WHERE id=1")
    row = cur.fetchone()

    conn.close()

    return jsonify({
        "touch": row[0],
        "switch": row[1]
    })

if __name__ == "__main__":
    app.run()