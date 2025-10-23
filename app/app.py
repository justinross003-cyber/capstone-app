
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from datetime import datetime
import uuid
from .db import get_db

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "dev-secret-change-me" 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customers")
def list_customers():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT CustomerId, Name, Email, CreatedAt FROM Customers ORDER BY CreatedAt DESC")
    rows = cur.fetchall()
    conn.close()
    return render_template("customers.html", customers=rows)

@app.route("/customers.json")
def customers_json():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT CustomerId, Name, Email, CreatedAt FROM Customers")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route("/customers/new", methods=["POST"])
def create_customer():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    if not name or not email:
        flash("Name and Email are required.", "error")
        return redirect(url_for("list_customers"))
    new_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat() + "Z"
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Customers (CustomerId, Name, Email, CreatedAt) VALUES (?, ?, ?, ?)",
            (new_id, name, email, now),
        )
        conn.commit()
        flash("Customer created.", "ok")
    except Exception as e:
        conn.rollback()
        flash(f"Error: {e}", "error")
    finally:
        conn.close()
    return redirect(url_for("list_customers"))

@app.route("/orders/<customer_id>")
def list_orders(customer_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Customers WHERE CustomerId = ?", (customer_id,))
    customer = cur.fetchone()
    cur.execute(
        "SELECT OrderId, Total, CreatedAt FROM Orders WHERE CustomerId = ? ORDER BY CreatedAt DESC",
        (customer_id,),
    )
    orders = cur.fetchall()
    conn.close()
    return render_template("orders.html", customer=customer, orders=orders, customer_id=customer_id)

@app.route("/orders/<customer_id>/new", methods=["POST"])
def create_order(customer_id):
    try:
        total = float(request.form.get("total", "0").strip())
    except ValueError:
        total = 0.0
    if total <= 0:
        flash("Total must be a positive number.", "error")
        return redirect(url_for("list_orders", customer_id=customer_id))
    new_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat() + "Z"
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Orders (OrderId, CustomerId, Total, CreatedAt) VALUES (?, ?, ?, ?)",
            (new_id, customer_id, total, now),
        )
        conn.commit()
        flash("Order created.", "ok")
    except Exception as e:
        conn.rollback()
        flash(f"Error: {e}", "error")
    finally:
        conn.close()
    return redirect(url_for("list_orders", customer_id=customer_id))

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "capstone-flask", "version": "0.1.0"}), 200
