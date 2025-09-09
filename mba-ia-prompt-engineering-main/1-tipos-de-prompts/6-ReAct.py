# REACT (Reasoning and Acting) - Raciocínio e Ação
# Alterna entre "Pensamento" (raciocínio) e "Ação" (passos concretos)
# Simula como um humano resolveria um problema: pensa, age, observa, repete
# Excelente para debugging, troubleshooting e resolução de problemas complexos

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
# ReAct para debugging de API: simula processo de troubleshooting
msg1 = """
Você é um engenheiro backend Go ajudando a debuggar uma REST API. 
Use o raciocínio estilo ReAct: alterne entre "Pensamento:" (seu raciocínio) e "Ação:" (um passo concreto ou verificação que você faria). 
Após cada ação, escreva "Observação:" para capturar o que você encontrou. 
No final, conclua com "Resposta Final:" como sua correção recomendada.

Não invente informações que não foram fornecidas no contexto. Exemplo: se o contexto não fornece logs de erro, não use logs de erro no seu raciocínio.

Contexto: Um usuário relata que o endpoint `POST /products` sempre retorna HTTP 500.  

Aqui está o código do handler para `POST /products`:

```go
func CreateProduct(w http.ResponseWriter, r *http.Request) {
    var product Product
    err := json.NewDecoder(r.Body).Decode(&product)
    if err != nil {
        http.Error(w, "Bad Request", http.StatusBadRequest)
        return
    }

    stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
    if err != nil {
        log.Fatal(err)
    }

    _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
    if err != nil {
        log.Println("Error during Exec:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }

    w.WriteHeader(http.StatusCreated)
}

type Product struct {
    ID          string  `json:"id"`
    Name        string  `json:"name"`
    Description string  `json:"description"`
    Price       string  `json:"price"` 
    Stock       int     `json:"stock"`
}
```
"""

# ReAct para planejamento de viagem: avalia múltiplas variáveis e restrições
msg2 = f"""
Você é um planejador de viagens ajudando uma família a escolher a melhor forma de ir de Orlando para Nova York no próximo mês. 
Use o raciocínio estilo ReAct: alterne entre "Pensamento:" (seu raciocínio) e "Ação:" (um passo como verificar tempo de voo, custos, ou conveniência). 
Após cada ação, escreva "Observação:" com o que você encontrou. 
No final, conclua com "Resposta Final:" como sua recomendação. 

Contexto:  
- A família tem 2 adultos e 2 crianças (idades 5 e 8).  
- Orçamento: máximo $1.000 para transporte (não incluindo hotel).  
- Datas: eles devem chegar em 10 de julho à noite.  
- Opções:  
  - **Voo**: $220 por pessoa ida e volta, voo de 3 horas, mais $80 total em taxas de bagagem.  
  - **Trem**: $150 por pessoa ida e volta, viagem de 20 horas, com WiFi a bordo e camas disponíveis por $50 extra por pessoa.  
  - **Aluguel de carro**: $60/dia, 2 dias dirigindo cada trecho (gasolina + pedágios estimados $250 total). Crianças ficam agitadas em viagens longas.  

Outros detalhes:  
- A escola das crianças termina em 9 de julho ao meio-dia.  
- Os pais preferem não chegar muito cansados, já que têm um casamento de família em 11 de julho pela manhã.  

Comece seu raciocínio agora.
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)

# print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
