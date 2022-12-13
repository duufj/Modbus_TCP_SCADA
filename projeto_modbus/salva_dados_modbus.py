import sqlite3


# import datetime


def salva_dados_bd(tensao, corrente, potencia):

    connection = sqlite3.connect(r"site_flask\historico_modbus.sqlite")  # ,
    # detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
    # )

    cursor = connection.cursor()

    # currentDateTime = datetime.datetime.now()

    # cursor.execute(
    #     "INSERT INTO MODBUS (DADO,DATA_HORARIO) VALUES (?,?)", (tensao, currentDateTime)
    # )

    cursor.execute(
        "INSERT INTO MEDIDOR_1 (TENSAO,CORRENTE,POTENCIA) VALUES (?,?,?)",
        (
            tensao,
            corrente,
            potencia,
        ),
    )

    connection.commit()

    cursor.close()

    connection.close()

    print(
        f"\ntensao '{tensao}'salvo com sucesso",
        f"\nCorrente '{corrente}'salvo com sucesso",
        f"\nPotencia '{potencia}'salvo com sucesso",
    )

    # Big_endian = True

    # if Big_endian:
    #     primeiro_bloco = bin(int(tensao) << 16)
    #     print(primeiro_bloco)
    #     primeiro_bloco_hex = hex(int(tensao) << 16)
    #     print(primeiro_bloco_hex)

    #     segundo_bloco = bin(int(corrente))
    #     print(segundo_bloco)
    #     segundo_bloco_hex = hex(int(corrente))
    #     print(segundo_bloco_hex)

    #     bloco_resultante = (int(tensao) << 16) | int(corrente)
    #     print(bloco_resultante)
    #     print(hex(bloco_resultante))
    # else:
    #     primeiro_bloco = bin(int(corrente) << 16)
    #     print(primeiro_bloco)
    #     primeiro_bloco_hex = hex(int(tensao) << 16)
    #     print(primeiro_bloco_hex)

    #     segundo_bloco = bin(int(corrente))
    #     print(segundo_bloco)
    #     segundo_bloco_hex = hex(int(corrente))
    #     print(segundo_bloco_hex)

    #     bloco_resultante = (int(tensao) << 16) | int(corrente)
    #     print(bloco_resultante)
    #     print(hex(bloco_resultante))

    # primeiro_bloco = primeiro_bloco << 16
    # print(primeiro_bloco)

    # hex(int(corrente))

    # hex(int(tensao) << 16) or hex(int(corrente))
