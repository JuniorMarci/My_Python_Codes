import google.generativeai as genai
import os

# Configurar a chave de API
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

# Carregar o documento de regras
doc = genai.upload_file(r"C:\Users\marcio.junior\Downloads\PR.txt")

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

    # Exibir a resposta
    print("Resposta:", resposta.text)

    return historico

# Pergunta inicial
pergunta_inicial = 'Consegue detalhar melhor?'
historico_chat = fazer_pergunta(pergunta_inicial, historico_chat)

# Pergunta de follow-up com base na resposta anterior
#pergunta_follow_up = 'COnsegue detalhar melhor?'
#historico_chat = fazer_pergunta(pergunta_follow_up, historico_chat)
