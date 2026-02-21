from flask import Flask, render_template, request, redirect
import mysql.connector


app = Flask(__name__, template_folder='html', static_folder='css')

def conectar_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="", #Insira a senha do Banco de dados local
        database="atividade3bd"
    )

@app.route('/')
def index():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Clube")
    clubes = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Jogador")
    jogadores = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Contrato")
    contratos = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return render_template('index.html', clubes=clubes, jogadores=jogadores, contratos=contratos)


@app.route('/inserir_clube', methods=['POST'])
def inserir_clube():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    comando_sql = "INSERT INTO Clube (nome, cnpj, cidade, estado, data_filiacao) VALUES (%s, %s, %s, %s, %s)"
    valores = (
        request.form['nome'], 
        request.form['cnpj'], 
        request.form['cidade'], 
        request.form['estado'], 
        request.form['data_filiacao']
    )
    cursor.execute(comando_sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')

@app.route('/inserir_jogador', methods=['POST'])
def inserir_jogador():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    comando_sql = """INSERT INTO Jogador 
                     (licenca, posicao, altura, peso, primeiro_nome, sobrenome, data_nascimento, cpf, telefones) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    valores = (
        request.form['licenca'], request.form['posicao'], request.form['altura'], 
        request.form['peso'], request.form['primeiro_nome'], request.form['sobrenome'], 
        request.form['data_nascimento'], request.form['cpf'], request.form['telefones']
    )
    cursor.execute(comando_sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')

@app.route('/inserir_contrato', methods=['POST'])
def inserir_contrato():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    comando_sql = """INSERT INTO Contrato 
                     (id_contrato, id_jogador, id_clube, data_inicio, data_fim, salario, multa) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores = (
        request.form['id_contrato'], request.form['id_jogador'], request.form['id_clube'],
        request.form['data_inicio'], request.form['data_fim'], request.form['salario'], request.form['multa']
    )
    cursor.execute(comando_sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')


@app.route('/atualizar_clube', methods=['POST'])
def atualizar_clube():

    id_clube = request.form['id_clube']
    

    campos_recebidos = {
        'nome': request.form['novo_nome'],
        'cnpj': request.form['novo_cnpj'],
        'cidade': request.form['nova_cidade'],
        'estado': request.form['novo_estado'],
        'data_filiacao': request.form['nova_data_filiacao']
    }
    
    clausulas_set = []
    valores = []
    

    for coluna, valor in campos_recebidos.items():
        if valor.strip():  
            clausulas_set.append(f"{coluna} = %s")
            valores.append(valor)
            

    if len(clausulas_set) == 0:
        return redirect('/')
        

    comando_sql = f"UPDATE Clube SET {', '.join(clausulas_set)} WHERE id_clube = %s"
    valores.append(id_clube)
    

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(comando_sql, tuple(valores))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')


@app.route('/deletar_clube/<int:id>')
def deletar_clube(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Clube WHERE id_clube = %s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')

@app.route('/deletar_jogador/<int:id>')
def deletar_jogador(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Jogador WHERE id_jogador = %s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')

@app.route('/deletar_contrato/<id>')
def deletar_contrato(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Contrato WHERE id_contrato = %s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)