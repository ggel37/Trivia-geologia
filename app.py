from Flask import Flask, render_template, request

app = Flask(__name__)

preguntas = [
    {
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": ["Venus", "Mercurio", "Marte", "Júpiter"],
        "respuesta": "Mercurio"
    },
    {
        "pregunta": "¿Cuál es el continente más grande?",
        "opciones": ["África", "Europa", "Asia", "América"],
        "respuesta": "Asia"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del planeta?",
        "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
        "respuesta": "Pacífico"
    },
    {
        "pregunta": "¿Qué tipo de roca se forma a partir del enfriamiento del magma?",
        "opciones": ["Sedimentaria", "Metamórfica", "Ígnea", "Orgánica"],
        "respuesta": "Ígnea"
    },
    {
        "pregunta": "¿Cómo se llama el movimiento de las placas tectónicas?",
        "opciones": ["Tectónica de placas", "Erosión", "Sedimentación", "Meteorización"],
        "respuesta": "Tectónica de placas"
    }
]


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    puntaje = 0

    if request.method == "POST":

        for i, pregunta in enumerate(preguntas):
            respuesta_usuario = request.form.get(f"pregunta{i}")

            if respuesta_usuario == pregunta["respuesta"]:
                puntaje += 1

        resultado = f"Obtuviste {puntaje} de {len(preguntas)} respuestas correctas."

    return render_template(
        "index.html",
        preguntas=preguntas,
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=5000)