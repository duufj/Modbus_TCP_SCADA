import sqlite3

from flask import (
    Flask,
    Response,
    request,
    render_template,
    stream_with_context,
)
import json
import time

app = Flask(__name__)


def get_db_ultima_linha():
    conn = sqlite3.connect("historico_modbus.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MEDIDOR_1 ORDER BY id DESC LIMIT 1")
    ultima_linha = cursor.fetchone()
    # print(ultima_linha)
    # id, tensao, timestamp = ultima_linha
    # print(id, tensao, timestamp)
    conn.close()
    return ultima_linha


def get_db_parametros():
    conn = sqlite3.connect("historico_modbus.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PARAMETROS ORDER BY ROWID ASC LIMIT 1")
    linha_parametros = cursor.fetchone()
    conn.close()
    return linha_parametros


def set_db_parametros(parametros):
    conn = sqlite3.connect("historico_modbus.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO PARAMETROS (ID, IP, PORTA, ENDERECO, REGISTRADOR_TENSAO, REGISTRADOR_CORRENTE, REGISTRADOR_POTENCIA) VALUES (?,?,?,?,?,?,?)",
        (
            1,
            parametros[0],
            parametros[1],
            parametros[2],
            parametros[3],
            parametros[4],
            parametros[5],
        ),
    )
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")

    # if request.method == "POST":
    #     parametros_novos = [
    #         request.form.get("ip"),
    #         request.form.get("porta"),
    #         request.form.get("endereco"),
    #         request.form.get("registrador_tensao"),
    #         request.form.get("registrador_corrente"),
    #         request.form.get("registrador_potencia"),
    #     ]

    #     set_db_parametros(parametros_novos)

    # (
    #     id,
    #     ip,
    #     porta,
    #     endereco,
    #     registrador_tensao,
    #     registrador_corrente,
    #     registrador_potencia,
    # ) = get_db_parametros()

    # return render_template(
    #     "index.html",
    #     ip=ip,
    #     porta=porta,
    #     endereco=endereco,
    #     registradores=[registrador_tensao, registrador_corrente, registrador_potencia],
    # )


@app.route("/configuracoes", methods=["GET", "POST"])
def configuracoes():
    if request.method == "POST":
        parametros_novos = [
            request.form.get("ip"),
            request.form.get("porta"),
            request.form.get("endereco"),
            request.form.get("registrador_tensao"),
            request.form.get("registrador_corrente"),
            request.form.get("registrador_potencia"),
        ]

        set_db_parametros(parametros_novos)

    (
        id,
        ip,
        porta,
        endereco,
        registrador_tensao,
        registrador_corrente,
        registrador_potencia,
    ) = get_db_parametros()

    return render_template(
        "configuracoes.html",
        ip=ip,
        porta=porta,
        endereco=endereco,
        registradores=[registrador_tensao, registrador_corrente, registrador_potencia],
    )


@app.route("/graph")
def graph():
    return render_template("graph.html")


@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")


@app.route("/biblioteca")
def biblioteca():
    return render_template("biblioteca.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/chart-data")
def chart_data():
    def generate_random_data():
        while True:
            id, tensao, corrente, potencia, timestamp = get_db_ultima_linha()
            json_data = json.dumps(
                {
                    "time": timestamp,
                    "value": tensao,
                    # "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    # "value": random.random() * 100,
                }
            )
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(
        stream_with_context(generate_random_data()), mimetype="text/event-stream"
    )
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


@app.route("/chart-data2")
def chart_data2():
    def generate_random_data2():
        while True:
            id, tensao, corrente, potencia, timestamp = get_db_ultima_linha()
            json_data = json.dumps(
                {
                    "time": timestamp,
                    "value": corrente,
                    # "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    # "value": random.random() * 100,
                }
            )
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(
        stream_with_context(generate_random_data2()), mimetype="text/event-stream"
    )
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


@app.route("/chart-data3")
def chart_data3():
    def generate_random_data3():
        while True:
            id, tensao, corrente, potencia, timestamp = get_db_ultima_linha()
            json_data = json.dumps(
                {
                    "time": timestamp,
                    "value": potencia,
                    # "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    # "value": random.random() * 100,
                }
            )
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(
        stream_with_context(generate_random_data3()), mimetype="text/event-stream"
    )
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
