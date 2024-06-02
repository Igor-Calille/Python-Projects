from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from db_config import get_db_connection

veiculos_bp = Blueprint('veiculos', __name__)

# Create - Adicionar um novo veículo
@veiculos_bp.route('/', methods=['POST'])
def create_veiculo():
    categoria_id = request.form['categoria_id']
    ativo = 1
    placa = request.form['placa']
    status = request.form['status']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Veiculos (categoria_id, ativo, placa, status) VALUES (%s, %s, %s, %s)',
        (categoria_id, ativo,placa, status)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('veiculos.read_veiculos'))

# Read - Obter todos os veículos
@veiculos_bp.route('/', methods=['GET'])
def read_veiculos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Veiculos WHERE ativo=1')
    veiculos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('veiculos.html', veiculos=veiculos)

# Read - Obter um veículo específico
@veiculos_bp.route('/<int:veiculo_id>', methods=['GET'])
def read_veiculo(veiculo_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Veiculos WHERE veiculo_id=%s AND ativo=%s', (veiculo_id,1,))
    veiculo = cursor.fetchone()
    cursor.close()
    connection.close()
    if veiculo:
        return render_template('veiculos.html', veiculo=veiculo)
    else:
        return jsonify({"message": "Veículo não encontrado"}), 404

# Update - Atualizar um veículo
@veiculos_bp.route('/<int:veiculo_id>', methods=['POST'])
def update_veiculo(veiculo_id):
    categoria_id = request.form.get('categoria_id')
    placa = request.form.get('placa')
    status = request.form.get('status')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE Veiculos SET categoria_id=%s, placa=%s, status=%s WHERE veiculo_id=%s',
        (categoria_id, placa, status, veiculo_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('veiculos.read_veiculos'))

# soft Delete - atualizar ativo(1) para inativo(0)
@veiculos_bp.route('/delete/<int:veiculo_id>', methods=['POST'])
def soft_delete_veiculo(veiculo_id):
    ativo = 0

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Veiculos SET ativo=%s WHERE veiculo_id=%s', (ativo,veiculo_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('veiculos.read_veiculos'))
