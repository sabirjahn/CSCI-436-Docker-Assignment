from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from datetime import datetime

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
DB_NAME = os.getenv("MONGO_DB", "assignment3db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
visits_collection = db["visits"]


@app.route("/")
def home():
    return jsonify({
        "message": "CSCI 436 - Assignment 3 Docker & Containerization",
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/visit", methods=["POST"])
def add_visit():
    payload = request.get_json(silent=True) or {}
    user = payload.get("user", "student")
    doc = {
        "user": user,
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    result = visits_collection.insert_one(doc)
    return jsonify({
        "message": "Visit stored",
        "id": str(result.inserted_id),
        "user": user
    }), 201


@app.route("/visits", methods=["GET"])
def list_visits():
    docs = list(visits_collection.find({}, {"_id": 0}))
    return jsonify({
        "count": len(docs),
        "items": docs
    })


@app.route("/health", methods=["GET"])
def health():
    try:
        client.admin.command("ping")
        return jsonify({"app": "up", "mongo": "up"}), 200
    except Exception as e:
        return jsonify({"app": "up", "mongo": "down", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
