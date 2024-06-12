from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from db_config import get_db_connection

locacoes_bp = Blueprint('locacoes', __name__)

# Create - Adicionar uma nova locação
@locacoes_bp.route('/', methods=['POST'])
def create_locacao():
    usuario_id = request.form['usuario_id']
    veiculo_id = request.form['veiculo_id']
    localizacao_id = request.form['localizacao_id']
    ativo = 1
    data_inicio = request.form['data_inicio']
    data_fim = request.form['data_fim']
    preco_total = request.form['preco_total']
    status = request.form['status']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Locacoes (usuario_id, veiculo_id, localizacao_id, ativo,data_inicio, data_fim, preco_total, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (usuario_id, veiculo_id, localizacao_id, ativo, data_inicio, data_fim, preco_total, status)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('locacoes.read_locacoes'))

# Read - Obter todas as locações
@locacoes_bp.route('/', methods=['GET'])
def read_locacoes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Locacoes WHERE ativo=1')
    locacoes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('locacoes.html', locacoes=locacoes)

# Read - Obter uma locação específica
@locacoes_bp.route('/<int:locacao_id>', methods=['GET'])
def read_locacao(locacao_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Locacoes WHERE locacao_id=%s AND ativo=%s', (locacao_id, 1,))
    locacao = cursor.fetchone()
    cursor.close()
    connection.close()
    if locacao:
        return render_template('locacao.html', locacao=locacao)
    else:
        return jsonify({"message": "Locação não encontrada"}), 404

# Update - Atualizar uma locação
@locacoes_bp.route('/<int:locacao_id>', methods=['POST'])
def update_locacao(locacao_id):
    usuario_id = request.form.get('usuario_id')
    veiculo_id = request.form.get('veiculo_id')
    localizacao_id = request.form.get('localizacao_id')
    data_inicio = request.form.get('data_inicio')
    data_fim = request.form.get('data_fim')
    preco_total = request.form.get('preco_total')
    status = request.form.get('status')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE Locacoes SET usuario_id=%s, veiculo_id=%s, localizacao_id=%s, data_inicio=%s, data_fim=%s, preco_total=%s, status=%s WHERE locacao_id=%s',
        (usuario_id, veiculo_id, localizacao_id, data_inicio, data_fim, preco_total, status, locacao_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('locacoes.read_locacoes'))

# soft Delete - atualizar ativo(1) para inativo(0)
@locacoes_bp.route('/delete/<int:locacao_id>', methods=['POST'])
def soft_delete_locacoes(locacao_id):
    ativo = 0

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Locacoes SET ativo=%s WHERE locacao_id=%s', (ativo,locacao_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('locacoes.read_locacoes'))
