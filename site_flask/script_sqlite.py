import sqlite3

connection = sqlite3.connect(r"site_flask\historico_modbus.sqlite")

cursor = connection.cursor()

# cursor.execute("DROP TABLE PARAMETROS")

# cursor.execute(
#     "CREATE TABLE MODBUS(ID INTEGER PRIMARY KEY AUTOINCREMENT,DADO REAL,DATA_HORARIO TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
# )

# cursor.execute(
#     "CREATE TABLE PARAMETROS(ID INTEGER PRIMARY KEY,IP TEXT,PORTA TEXT,ENDERECO TEXT,REGISTRADOR_TENSAO TEXT,REGISTRADOR_CORRENTE TEXT,REGISTRADOR_POTENCIA TEXT)"
# )

# cursor.execute(
#     "INSERT INTO PARAMETROS (ID, IP, PORTA, REGISTRADOR_TENSAO, REGISTRADOR_CORRENTE, REGISTRADOR_POTENCIA) VALUES (?,?,?,?,?,?)",
#     (
#         "1",
#         "127.0.0.1",
#         "501",
#         "40001",
#         "40002",
#         "40003",
#     ),
# )


cursor.execute(
    "INSERT OR REPLACE INTO PARAMETROS (ID, IP, PORTA, ENDERECO, REGISTRADOR_TENSAO, REGISTRADOR_CORRENTE, REGISTRADOR_POTENCIA) VALUES (?,?,?,?,?,?,?)",
    (
        "1",
        "127.0.0.1",
        "501",
        "1",
        "4001",
        "40002",
        "40003",
    ),
)

connection.commit()


cursor.execute("SELECT * FROM PARAMETROS ORDER BY ROWID ASC LIMIT 1")
primeira_linha = cursor.fetchone()
print(primeira_linha)


connection.close()
