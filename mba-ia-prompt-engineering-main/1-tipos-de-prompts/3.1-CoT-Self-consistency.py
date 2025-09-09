# CHAIN OF THOUGHT + SELF-CONSISTENCY
# Combina CoT com múltiplos caminhos de raciocínio para melhorar a precisão
# O modelo gera várias formas de resolver o mesmo problema e escolhe a resposta mais consistente

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# CoT com Self-Consistency: múltiplos caminhos de raciocínio para problema de performance
msg1 = """
Pergunta: Em um endpoint de API que retorna uma lista de usuários e seus posts, o desenvolvedor escreveu:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts = db.FindPostsByUserID(u.ID)
}

Quantas consultas ao banco de dados este código executará se houver N usuários?

Gere 3 caminhos de raciocínio diferentes passo a passo.
No final, resuma as respostas e escolha a mais consistente, ignorando outliers.
Se houver 3 respostas diferentes, APENAS responda: "Não consigo encontrar uma resposta consistente".
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
print_llm_result(msg1, response1)
