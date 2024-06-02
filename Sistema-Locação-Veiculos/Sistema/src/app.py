from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from routes.usuarios import usuarios_bp
from routes.veiculos import veiculos_bp
from routes.locacoes import locacoes_bp
from db_config import get_db_connection

app = Flask(__name__)


# Registrando os Blueprints
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(veiculos_bp, url_prefix='/veiculos')
app.register_blueprint(locacoes_bp, url_prefix='/locacoes')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO UsuáriosLogin (nome, email, senha_hash) VALUES (%s, %s, %s)',
                           (nome, email, senha_hash))
            conn.commit()
            flash('Registro bem-sucedido! Faça login.')
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            flash(f'Erro: {err}')
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM UsuáriosLogin WHERE email = %s', (email,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario and check_password_hash(usuario['senha_hash'], senha):
            session['user_id'] = usuario['id']
            return redirect(url_for('index'))
        else:
            flash('Email ou senha incorretos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
