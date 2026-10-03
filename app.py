from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "devops_app")
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("contact"))

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO messages (name, email, message)
                VALUES (%s, %s, %s)
            """

            cursor.execute(query, (name, email, message))
            connection.commit()

            cursor.close()
            connection.close()

            flash("Your message has been saved successfully!", "success")

        except mysql.connector.Error as error:
            print("Database error:", error)
            flash("Unable to save your message.", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Flask DevOps App"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
