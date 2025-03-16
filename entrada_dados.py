from datetime import datetime

formato_data = "%d-%m-%Y"
CATEGORIAS = {"E": "Entrada", "D": "Despesas"}

def obter_data(prompt, permitir_padrao = False):
    data_str = input(prompt) 
    if permitir_padrao and not data_str:
        return datetime.today().strftime(formato_data)

    try:
        data_valida = datetime.strptime(data_str, formato_data)
        return data_valida.strftime(formato_data)
    except ValueError:
        print("Formato de data inválida. Por favor coloque uma data no formato dd-mm-aa.")
        return obter_data(prompt, permitir_padrao)
    

def obter_quantia():
    try:
        quantia = float(input("Informe uma quantia: "))
        if quantia <= 0:
            raise ValueError("A quantia não pode ser zero nem um número abaixo de zero.")
        return quantia 
    except ValueError as e:
        print(e)
        return obter_quantia()

def obter_categoria():
    categoria = input("Informe a categoria ('E' para Entrada e 'D' para Despesas/Saídas): ").upper()
    if categoria in CATEGORIAS:
        return CATEGORIAS[categoria]
    
    print("Categoria inválida. Por favor 'E' para Entrada e 'D' para Despesas/Saídas")
    return obter_categoria()

def obter_descricao():
    return input("Adicione uma descrição(Opcional): ")