# SKELETON OF THOUGHT (SoT) - Esqueleto de Pensamento
# Primeiro cria um "esqueleto" (estrutura) da resposta, depois expande cada parte
# Étil para respostas estruturadas, documentação, ou quando precisa de uma resposta bem organizada

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# SoT para explicação técnica: estrutura antes de expandir
msg1 = """
Você é um engenheiro backend sênior. Um desenvolvedor júnior perguntou como otimizar consultas SQL para melhor performance. 
Siga a abordagem Skeleton of Thought: 

Passo 1: Gere apenas o esqueleto da sua resposta em 3-5 tópicos concisos. 
Passo 2: Expanda cada tópico em uma explicação clara e detalhada com exemplos. 
Certifique-se de que a resposta final seja estruturada e fácil de seguir.
"""

# SoT para documentação formal: ADR estruturado
msg2 = f"""
Você é um arquiteto de software. Quero que você produza um Architecture Decision Record (ADR) sobre escolher PostgreSQL em vez de MongoDB. 

Siga a abordagem Skeleton of Thought:
Passo 1: Primeiro, produza apenas o esqueleto do ADR como títulos de seções (ainda sem explicações). 
Use a estrutura padrão de ADR com 5 seções: Contexto, Decisão, Alternativas Consideradas, Consequências, Referências. 
Passo 2: Após mostrar o esqueleto, expanda cada seção com conteúdo claro e detalhado. 
Mantenha o ADR final profissional, estruturado e fácil de ler.
"""

# SoT para planejamento de API: estrutura técnica detalhada
msg3 = f"""
Você é um desenvolvedor Go sênior. Quero que me ajude a planejar uma REST API para gerenciar produtos em Go.

Siga a abordagem Skeleton of Thought:

Passo 1: Produza apenas o esqueleto da solução em 6-8 tópicos concisos. 
O esqueleto deve cobrir: definição do modelo de dados em Go (structs), escolha do framework HTTP ou net/http, roteamento, handlers, validações, camada de banco de dados, tratamento de erros, e estrutura do projeto. Não expanda ainda.

Passo 2: Expanda cada tópico com detalhes técnicos claros, exemplos e melhores práticas Go. 
Inclua trechos de código de exemplo em Go (structs, handlers, routes) e considerações sobre pacotes (ex: chi, ou net/http), tratamento de erros idiomático em Go, e como organizar o projeto em pacotes (handlers, models, db). 
Use linguagem concisa e profissional.

A API deve implementar operações CRUD para produtos com os campos: id, name, description, price, stock.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)