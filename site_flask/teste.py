import sqlite3

connection = sqlite3.connect(r"site_flask\historico_modbus.sqlite")

cursor = connection.cursor()

# cursor.execute("DROP TABLE MODBUS")

cursor.execute("SELECT DADO,DATA_HORARIO FROM MODBUS")


tabela = cursor.fetchall()
connection.close()

dados = []
estampas = []
for linha in tabela:
    dados.append(linha[0])
    estampas.append(linha[1])

print(dados, type(estampas[0]))

connection.close()
