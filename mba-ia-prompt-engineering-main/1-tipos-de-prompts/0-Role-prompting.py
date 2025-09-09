
# ROLE PROMPTING (Prompting com Papéis)
# Define diferentes "papéis" ou personas para o modelo assumir, modificando seu comportamento e estilo de resposta
# Muito útil para adaptar a linguagem técnica ao público-alvo ou conseguir respostas especializadas

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from utils import print_llm_result
from dotenv import load_dotenv
load_dotenv()

# Papel 1: Professor universitário técnico - respostas formais e detalhadas
system = ("system", 
"""Você é um professor universitário de ciência da computação que é muito técnico e explica 
conceitos com definições formais e pseudocódigo.""")

# Papel 2: Estudante iniciante - respostas simples e acessíveis
system2 = ("system", """Você é um estudante do ensino médio que está começando a aprender programação. 
Você não é muito técnico e prefere explicar conceitos com palavras simples e exemplos.""")

# Pergunta em português
user = ("user", "Explique recursão em 50 palavras.")

chat_prompt = ChatPromptTemplate([system, user])
chat_prompt2 = ChatPromptTemplate([system2, user])
messages = chat_prompt.format_messages()

model = ChatOpenAI(model="gpt-4o")
result = model.invoke(messages)
print_llm_result(str(system), result)

result2 = model.invoke(chat_prompt2.format_messages())
print_llm_result(str(system2), result2)