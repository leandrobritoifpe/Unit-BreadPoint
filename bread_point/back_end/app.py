import os
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Conexão com o banco
def get_db():
    conn = sqlite3.connect('bread_point.db')
    conn.row_factory = sqlite3.Row  # Para acessar por nome de coluna
    return conn

def close_db(conn):
    conn.close()

# Página inicial - renderizar produtos
@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    
    # Buscar produtos do banco
    cursor.execute("""
        SELECT id, product_name, image FROM products
    """)
    products = [dict(row) for row in cursor.fetchall()]  # Converter para dicionário
    close_db(conn)

    # Passar produtos para o template
    return render_template('home.html', products=products)

# Página de planos
@app.route('/plans')
def plans():
    return render_template('plans.html')

# Registro de usuário
@app.route('/register')
def register():
    return render_template('register.html')

# Login de usuário
@app.route('/login')
def login():
    return render_template('login.html')

# Página de checkout
@app.route('/checkout')
def checkout():
    return render_template('checkout-plan.html')


# Buscar produto específico pelo ID
@app.route('/product/<int:product_id>', methods=['GET'])
def product_description(product_id):
    conn = get_db()
    cursor = conn.cursor()

    # Buscar produto pelo ID
    cursor.execute("""
        SELECT product_name, description, price, calories, protein, carbohydrates, fats, image
        FROM products
        WHERE id = ?
    """, (product_id,))
    product = cursor.fetchone()
    close_db(conn)

    # Se o produto não for encontrado, retorne erro 404
    if not product:
        return render_template('404.html', message="Produto não encontrado"), 404

    # Converter os dados em um dicionário para o template
    product_data = {
        "name": product[0],
        "description": product[1],
        "price": product[2],
        "calories": product[3],
        "protein": product[4],
        "carbohydrates": product[5],
        "fats": product[6],
        "image": product[7],
    }

    # Renderizar o template com os dados do produto
    return render_template('product-description.html', product=product_data)
# Registro de usuário (API)
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    close_db(conn)
    return jsonify({"message": "User registered successfully"}), 201

# Login de usuário (API)
@app.route('/api/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    close_db(conn)

    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
