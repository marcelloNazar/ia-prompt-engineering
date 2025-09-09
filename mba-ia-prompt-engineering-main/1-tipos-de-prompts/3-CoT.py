# CHAIN OF THOUGHT (CoT) - Cadeia de Pensamento
# Encoraja o modelo a "pensar passo a passo" antes de dar a resposta final
# Muito eficaz para problemas que requerem raciocínio lógico, matemática, ou análise complexa

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# Exemplo SEM Chain of Thought: resposta direta
msg1 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Responda apenas com INFO, AVISO, ou ERRO.
"""

# Exemplo COM Chain of Thought: pede raciocínio passo a passo
msg2 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Pense passo a passo sobre por que isso é INFO, AVISO, ou ERRO. 
No final, dê apenas a resposta final após "Resposta:".
"""


# Exemplo clássico SEM CoT: contagem de letras (modelos frequentemente erram)
msg3 = """
Pergunta: Quantos "r" existem na palavra "morango"?
Responda apenas com o número de "r".
"""

# Exemplo clássico COM CoT: força o modelo a analisar letra por letra
msg4 = """
Pergunta: Quantos "r" existem na palavra "morango"?
Explique passo a passo analisando cada letra em tópicos, apontando os "r" antes de dar a resposta final. 
Dê o resultado final após "Resposta:".
"""

llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)