from flask import Flask, request, jsonify, render_template
import requests
import mysql.connector

app = Flask(__name__, template_folder='.')

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "mistral"   

db = mysql.connector.connect(
    host="localhost",
    user="appuser",          
    password="password",  
    database="company_db"
)

cursor = db.cursor(dictionary=True)


@app.route("/")
def home():
    return render_template("index.html")


def generate_sql(user_query):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a senior MySQL database engineer. "
                        "Convert natural language into a syntactically correct MySQL query. "
                        "Return ONLY the SQL statement. No explanation."
                    )
                },
                {
                    "role": "user",
                    "content": f"""
Database schema:
employees(id, name, department, salary, joining_date)

User request:
{user_query}
"""
                }
            ],
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
    )

    data = response.json()
    print("OLLAMA RAW:", data)

    if "message" in data:
        sql = data["message"]["content"]
    elif "response" in data:
        sql = data["response"]
    else:
        raise Exception("Unexpected Ollama response format")

    sql = sql.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


@app.route("/query", methods=["POST"])
def query():

    user_query = request.json.get("query")

    if not user_query:
        return jsonify({"error": "No query provided"})

    try:

        sql_query = generate_sql(user_query)

        cursor.execute(sql_query)

        if sql_query.lower().startswith("select"):
            result = cursor.fetchall()
        else:
            db.commit()
            result = [{"status": "Query executed successfully"}]

        return jsonify({
            "question": user_query,
            "generated_sql": sql_query,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True, port=5003)
