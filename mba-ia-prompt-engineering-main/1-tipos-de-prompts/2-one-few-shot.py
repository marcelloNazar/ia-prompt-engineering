# ONE-SHOT / FEW-SHOT PROMPTING (Prompt com Poucos Exemplos)
# Fornece um ou mais exemplos para o modelo aprender o padrão esperado
# Muito eficaz para tarefas de classificação, formatação específica ou quando zero-shot não funciona bem

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# ONE-SHOT: Um exemplo para ensinar o padrão
msg1 = """
EXEMPLO:
Pergunta: Qual é a capital da França?
Resposta: Paris

Pergunta: Qual é a capital do Brasil?
Resposta: 
"""

# ONE-SHOT: Classificação de severidade de logs com um exemplo
msg2 = """
Exemplo:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERRO

Agora classifique:
Entrada: "Uso de disco em 85%."
Saída:
"""


# FEW-SHOT: Múltiplos exemplos para melhor precisão na classificação
msg3 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERRO  

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: AVISO

Exemplo 3:
Entrada: "Tempo de resposta do banco está acima do limite em 30ms"
Saída: AVISO  

Exemplo 4:
Entrada: "Usuário logado com sucesso."
Saída: INFO  

Agora classifique:
Entrada: "Tempo de resposta da API está acima do limite."
Saída:
"""

# FEW-SHOT com muitos exemplos: Demonstra casos ambíguos e edge cases
msg4 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERRO  

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: AVISO  

Exemplo 3:
Entrada: "Usuário logado com sucesso."
Saída: INFO  

Exemplo 4:
Entrada: "Arquivo não encontrado: config.yaml"
Saída: ERRO  

Exemplo 5:
Entrada: "Alto uso de memória detectado: 75%"
Saída: AVISO  

Exemplo 6:
Entrada: "Job em background finalizado"
Saída: INFO  

Exemplo 7:
Entrada: "Tentando novamente requisição ao gateway de pagamento"
Saída: ERRO  

Exemplo 8:
Entrada: "Uso de disco em 90%"
Saída: ERRO   // ambíguo: poderia ser AVISO  

Exemplo 9:
Entrada: "Latência da API está acima do limite"
Saída: AVISO  

Exemplo 10:
Entrada: "Backup agendado concluído"
Saída: INFO  

Exemplo 11:
Entrada: "Pouco espaço em disco: 15% restante"
Saída: AVISO  

Exemplo 12:
Entrada: "Pouco espaço em disco: 5% restante"
Saída: ERRO   // ambíguo: AVISO ou ERRO?  

Exemplo 13:
Entrada: "Aquecimento de cache concluído"
Saída: INFO  

Exemplo 14:
Entrada: "Timeout de conexão, tentando novamente..."
Saída: AVISO   // ambíguo: poderia ser ERRO  

Exemplo 15:
Entrada: "Falha de autenticação para usuário admin"
Saída: ERRO  

Agora classifique:
Entrada: "Uso de CPU está em 95%."
Saída:
"""

# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model
llm = ChatOpenAI(model="gpt-3.5-turbo")
response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)