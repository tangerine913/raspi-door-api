from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# デフォルトメッセージ
messages = {
    "touch": "初回ドアです",
    "switch": "最終ゲートです"
}

# POSTでメッセージを更新する
@app.route("/set_message", methods=["POST"])
def set_message():
    data = request.json
    if "touch" in data:
        messages["touch"] = data["touch"]
    if "switch" in data:
        messages["switch"] = data["switch"]
    print("更新:", messages)
    return jsonify({"status": "ok"})

# GETで最新のメッセージを取得する
@app.route("/get_message", methods=["GET"])
def get_message():
    return jsonify(messages)

if __name__ == "__main__":
    app.run()