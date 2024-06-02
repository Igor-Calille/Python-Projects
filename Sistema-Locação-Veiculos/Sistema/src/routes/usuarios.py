from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from db_config import get_db_connection

usuarios_bp = Blueprint('usuarios', __name__)

# Create - Adicionar um novo usuário
@usuarios_bp.route('/', methods=['POST'])
def create_usuario():
    ativo = 1
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Usuarios (ativo, nome, email, senha, telefone, endereco) VALUES (%s, %s, %s, %s, %s, %s)',
        (ativo, nome, email, senha, telefone, endereco)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('usuarios.read_usuarios'))

# Read - Obter todos os usuários
@usuarios_bp.route('/', methods=['GET'])
def read_usuarios():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Usuarios WHERE ativo=1')
    usuarios = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('usuarios.html', usuarios=usuarios)

# Read - Obter um usuário específico
@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def read_usuario(usuario_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Usuarios WHERE usuario_id=%s AND ativo=%s', (usuario_id,1))
    usuario = cursor.fetchone()
    cursor.close()
    connection.close()
    if usuario:
        return render_template('usuario.html', usuario=usuario)
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404

# Update - Atualizar um usuário
@usuarios_bp.route('/<int:usuario_id>', methods=['POST'])
def update_usuario(usuario_id):
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    telefone = request.form.get('telefone')
    endereco = request.form.get('endereco')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE Usuarios SET nome=%s, email=%s, senha=%s, telefone=%s, endereco=%s WHERE usuario_id=%s',
        (nome, email, senha, telefone, endereco, usuario_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('usuarios.read_usuarios'))

# soft Delete - atualizar ativo(1) para inativo(0)
@usuarios_bp.route('/delete/<int:usuario_id>', methods=['POST'])
def soft_delete_usuario(usuario_id):
    ativo = 0

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Usuarios SET ativo=%s WHERE usuario_id=%s', (ativo,usuario_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('usuarios.read_usuarios'))
