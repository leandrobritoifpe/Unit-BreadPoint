import sqlite3

def create_db():
    conn = sqlite3.connect('bread_point.db')  
    cursor = conn.cursor()

    # Criação da Tabela de Usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    ''')

    # Criação da Tabela de Planos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plan_name TEXT NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL
    );
    ''')

    # Criação da Tabela de Produtos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL,
        calories INTEGER,
        protein INTEGER,
        carbohydrates INTEGER,
        fats INTEGER,
        image TEXT
    );
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

# Executar a criação do banco de dados
if __name__ == "__main__":
    create_db()
