# PROMPT CHAINING (Encadeamento de Prompts)
# Quebra uma tarefa complexa em múltiplos prompts sequenciais
# A saída de um prompt se torna entrada do próximo
# Permite usar diferentes modelos para diferentes etapas, otimizando custo e qualidade

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Diferentes modelos para diferentes etapas (otimização de custo/qualidade)
llm1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)  # Extraição de schema
llm2 = ChatOpenAI(model="gpt-5-mini", temperature=0)     # Geração de código Go
llm3 = ChatOpenAI(model="gpt-4o-mini", temperature=0)    # Mensagem de commit


# Passo 1: Especificação -> Schema JSON
spec_to_schema = PromptTemplate.from_template(
    """Você é um engenheiro backend sênior.
Da seguinte especificação de produto, extraia um schema JSON mínimo com campos e tipos.
Retorne apenas JSON. Nenhum comentário.

Escreva todo o código usando blocos de código markdown.  

Especificação:
{spec}
"""
) | llm1 | StrOutputParser()

# Passo 2: Schema JSON -> Rotas e Handlers Go
schema_to_routes = PromptTemplate.from_template(
    """Você é um desenvolvedor Go sênior.
Dado o schema JSON abaixo, projete rotas REST e esboce handlers Go idiomáticos para CRUD.
Mantenha conciso, orientado à produção, e mostre trechos de código.

Escreva todo o código usando blocos de código markdown.  

Schema JSON:
{schema_json}
"""
) | llm2 | StrOutputParser()

# Passo 3: Schema + Rotas -> Mensagem de Commit
commit_message = PromptTemplate.from_template(
    """Você é um desenvolvedor pragmático.
Escreva uma mensagem de commit convencional de uma linha resumindo a nova API baseada no schema e rotas.

Schema:
{schema_json}

Rotas e handlers:
{routes}
"""
) | llm3 | StrOutputParser()


# Especificação inicial em português
spec_text = """Precisamos de uma API de Produtos.
Campos: id (uuid), name (string, obrigatório), description (string), price (float, > 0), stock (int, >= 0).
Devemos suportar listagem com paginação, criar, buscar por id, atualizar, deletar.
"""

# Execução da cadeia de prompts e geração do resultado final
schema_json = spec_to_schema.invoke({"spec": spec_text})
routes = schema_to_routes.invoke({"schema_json": schema_json})
commit = commit_message.invoke({"schema_json": schema_json, "routes": routes})

# Template para salvar o resultado completo
result_content = f"""# Resultado do Encadeamento de Prompts

## SCHEMA (Gerado por GPT-3.5-turbo)
{schema_json}

## ROTAS & HANDLERS (Go) (Gerado por GPT-5-mini)
{routes}

## COMMIT (Gerado por GPT-4o-mini)
{commit}

---
**Pipeline de Modelos:**
- Passo 1: GPT-3.5-turbo (extração de schema)
- Passo 2: GPT-5-mini (geração de código Go)
- Passo 3: GPT-4o-mini (mensagem de commit)  

"""

with open("prompt_chaining_result.md", "w", encoding="utf-8") as f:
    f.write(result_content)

print("Resultado salvo em prompt_chaining_result.md")
