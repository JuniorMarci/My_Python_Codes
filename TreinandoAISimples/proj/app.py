from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Configure sua chave API do Google Generative AI
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input", "")

    # Verificar se a entrada do usuário não está vazia
    if not user_input:
        return jsonify({"error": "Entrada do usuário não pode ser vazia"}), 400



    # Carregar o documento de regras
    doc = genai.upload_file(r"Regras da empresa.txt")

    # Histórico de interação (exemplo básico)
    historico_chat = [
        '''Você é um atendente de uma loja de e-commerce e está falando num chat. As regras são do documento anexo.''',
        doc
    ]

    # Função para fazer perguntas e manter o histórico
    def fazer_pergunta(pergunta, historico):
        # Adicionar a pergunta ao histórico
        historico.append("PERGUNTA: " + pergunta)

        # Gerar a resposta com base no histórico completo
        resposta = model.generate_content(historico)

        # Adicionar a resposta ao histórico
        historico.append("RESPOSTA: " + resposta.text)

        return [historico,resposta.text]





    # Enviar o texto do usuário para o modelo generativo
    #response = model.generate_content([user_input])
    r = fazer_pergunta(user_input,historico_chat)
    historico_chat = r[0]
    response = r[1]

    # Retornar a resposta do modelo para o frontend
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
