from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234567",
    "database": "mydb",  # Nome do banco de dados
}

# Função para criar uma conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para listar todos os clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTES")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(clientes)
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para criar um novo cliente
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CLIENTES (Nome, Endereco, Contato) VALUES (%s, %s, %s)",
                       (data['Nome'], data['Endereco'], data['Contato']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Cliente criado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para atualizar um cliente
@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE CLIENTES SET Nome = %s, Endereco = %s, Contato = %s WHERE idCLIENTE = %s",
                       (data['Nome'], data['Endereco'], data['Contato'], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Cliente {id} atualizado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para excluir um cliente
@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM CLIENTES WHERE idCLIENTE = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Cliente {id} excluído com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para listar todos os animais
@app.route('/animais', methods=['GET'])
def get_animais():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ANIMAIS")
        animais = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(animais)
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para criar um novo animal
@app.route('/animais', methods=['POST'])
def criar_animal():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ANIMAIS (Nome, Especie, Data_Nascimento, idCliente) VALUES (%s, %s, %s, %s)",
                       (data['Nome'], data['Especie'], data['Data_Nascimento'], data['idCliente']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Animal criado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para atualizar um animal
@app.route('/animais/<int:id>', methods=['PUT'])
def atualizar_animal(id):
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ANIMAIS SET Nome = %s, Especie = %s, Data_Nascimento = %s, idCliente = %s WHERE idANIMAL = %s",
                       (data['Nome'], data['Especie'], data['Data_Nascimento'], data['idCliente'], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Animal {id} atualizado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para excluir um animal
@app.route('/animais/<int:id>', methods=['DELETE'])
def excluir_animal(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ANIMAIS WHERE idANIMAL = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Animal {id} excluído com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
