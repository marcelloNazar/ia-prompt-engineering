# TREE OF THOUGHT (ToT) - Árvore de Pensamento
# Explora múltiplas "ramificações" de raciocínio simultaneamente
# Util para problemas complexos que se beneficiam de múltiplas perspectivas e comparação de alternativas

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# ToT para debug de performance: explora múltiplas causas possíveis
msg1 = """
Você é um engenheiro de software sênior. 
Um usuário relata que uma requisição à API no endpoint `/users` está demorando 5 segundos para responder, o que é muito lento. 
Pense de forma Tree of Thought: 
- Gere pelo menos 3 diferentes causas possíveis para esta latência. 
- Para cada causa, raciocine passo a passo sobre quão provável ela é e como você a verificaria. 
- Então compare as ramificações e escolha a mais plausível como hipótese primária. 
- Termine com uma ação recomendada para debuggar ou corrigir o problema.
"""

# ToT para design de arquitetura: compara múltiplas opções arquiteturais
msg2 = f"""
Você está projetando um serviço que processa milhões de imagens diariamente. 
Pense de forma Tree of Thought: 
- Gere pelo menos 3 opções de arquitetura diferentes. 
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade. 
- Compare as opções. 
- Escolha o melhor trade-off e explique por que é superior às outras.
- Termine com "Resposta Final: " + a opção escolhida.
"""

# ToT com restrição de output: apenas a resposta final concisa
msg3 = f"""
Você está projetando um serviço que processa milhões de imagens diariamente. 
Pense de forma Tree of Thought: 
- Pense em pelo menos 3 opções de arquitetura diferentes. 
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade. 
- Compare as opções. 
- Escolha o melhor trade-off e explique por que é superior às outras.
- Termine com "Resposta Final: " + a opção escolhida com 6 palavras ou menos.

- RESPONDA APENAS COM A RESPOSTA FINAL, SEM NENHUM OUTRO TEXTO.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
# response3 = llm.invoke(msg3)

# print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
# print_llm_result(msg3, response3)