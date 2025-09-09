# ZERO-SHOT PROMPTING (Prompt Sem Exemplos)
# O modelo responde diretamente sem receber exemplos prévios de como deve responder
# Funciona bem para tarefas simples ou quando o modelo já tem conhecimento suficiente sobre o domínio

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()

# Exemplo 1: Pergunta direta e simples
msg1 = "Qual é a capital do Brasil?"

# Exemplo 2: Extração de intenção do usuário - mais complexo mas sem exemplos
msg2 = """
Encontre a intenção do usuário no seguinte texto: 
Estou procurando um restaurante na região de São Paulo que tenha boa avaliação para comida japonesa.
"""

# Exemplo 3: Pergunta com instrução específica de formato de resposta
msg3 = "Qual é a capital do Brasil? Responda apenas com o nome da cidade."



llm = ChatOpenAI(model="gpt-3.5-turbo")
response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)