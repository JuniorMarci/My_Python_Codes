import google.generativeai as genai
import os
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")
# Correct file path
doc = genai.upload_file(r"C:\Users\marcio.junior\Downloads\PR.txt")
pergunta = 'Posso pagar com pix?'
response = model.generate_content(['''
Você é um atendente de uma loja de e-commerce e está falando num chat. As regras são do documento anexo.
''', doc,"PERGUNTA: "+pergunta])
print(response.text)
