# Esse código refere-se ao mestre cuja a função é acessar as informações do dispositivo (medidor)
# TCP-CLIENTE
# MODBUS MESTRE

#!/usr/bin/env python
# scripts/examples/simple_tcp_client.py
import socket
from time import sleep
from umodbus import conf
from umodbus.client import tcp
from salva_dados_modbus import salva_dados_bd
import sqlite3

# Configuração das informações do dispositivo físico

# endereco_escravo = 1
# registrador_tensao = 40001
# registrador_corrente = 40002
# registrador_potencia = 40003

conn = sqlite3.connect(r"site_flask\historico_modbus.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM PARAMETROS ORDER BY ROWID ASC LIMIT 1")
linha_parametros = cursor.fetchone()
conn.close()

ip = linha_parametros[1]
porta = int(linha_parametros[2])
endereco_escravo = int(linha_parametros[3])
registrador_tensao = int(linha_parametros[4])
registrador_corrente = int(linha_parametros[5])
registrador_potencia = int(linha_parametros[6])

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, porta))

# Returns a message or Application Data Unit (ADU) specific for doing
# Modbus TCP/IP.

leitura_tensao = tcp.read_holding_registers(
    slave_id=endereco_escravo, starting_address=registrador_tensao - 40001, quantity=3
)

leitura_corrente = tcp.read_holding_registers(
    slave_id=endereco_escravo, starting_address=registrador_corrente - 40001, quantity=1
)

leitura_potencia = tcp.read_holding_registers(
    slave_id=endereco_escravo, starting_address=registrador_potencia - 40001, quantity=1
)

respostas_leitura_medidor = []  # [tensao, corrente, potência]

# Response depends on Modbus function code. This particular returns the
# amount of coils written, in this case it is.

while True:
    resposta_leitura_tensao = tcp.send_message(leitura_tensao, sock)
    resposta_leitura_corrente = tcp.send_message(leitura_corrente, sock)
    resposta_leitura_potencia = tcp.send_message(leitura_potencia, sock)

    print("resposta leituras: ", resposta_leitura_tensao)

    # respostas_leitura_medidor = [str(resposta_leitura_tensao[0]),str(resposta_leitura_corrente[0]) ,str(resposta_leitura_potencia[0]) ]

    salva_dados_bd(
        str(resposta_leitura_tensao[0]),
        str(resposta_leitura_corrente[0]),
        str(resposta_leitura_potencia[0]),
    )
    sleep(1)

sock.close()
