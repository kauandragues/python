import requests
from decimal import Decimal, getcontext, ROUND_HALF_UP  #para usar com dinheiro, float às vezes dá problema
import datetime
import csv

#configurar o decimal para usar arredondamento padrão
#diz para o decimal arredondar 4.669 -> 4.67 ou 4.662 -> 4.66
#esse é o arredondamento padrão de valores monetários
getcontext().rounding = ROUND_HALF_UP 

#solicitar valor em reais do usuário
def solicitar_valor():
    valor_str = input("Digite o valor em reais: R$ ")
    return Decimal(valor_str)

#solicitar data do valor do usuário
def solicitar_data():
    data_input = input("Digite a data da cotação (DD/MM/AAAA): ")
    data_datetime = datetime.datetime.strptime(data_input, "%d/%m/%Y")
    data_formatada = data_datetime.strftime("%m-%d-%Y")  # formato exigido pela API
    return data_formatada

#consultar a cotação de uma única moeda
def consultar_cotacao(moeda: str, data: str):
    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?"
        f"@moeda='{moeda}'&@dataCotacao='{data}'&$format=json"
    )

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json().get("value", [])

        if dados:
            return Decimal(str(dados[0]["cotacaoVenda"]))
        else:
            print(f"Cotação não encontrada para {moeda} em {data}.")
            return None
    except Exception as e:
        print(f"Erro ao consultar {moeda}: {e}")
        return None

#consultar cotações das moedas, converter e salvar
def consultar_cotacao_moedas(valor: Decimal, data: str):
    moedas = ["USD", "EUR", "JPY"]
    resultados = []

    for moeda in moedas:
        cotacao = consultar_cotacao(moeda, data)
        if cotacao:
            convertido = (valor / cotacao).quantize(Decimal("0.01"))
            print(f"{moeda}: Cotação de venda = {cotacao}\n Valor convertido = {convertido} {moeda}")

            resultados.append({
                "moeda": moeda,
                "cotacao_venda": cotacao,
                "valor_convertido": convertido
            })

    #salvar no arquivo CSV
    if resultados:
        with open("cotacoes.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["moeda", "cotacao_venda", "valor_convertido"])
            escritor.writeheader()
            escritor.writerows(resultados)
        print("\nCotações salvas em 'cotacoes.csv'")
    else:
        print("\nNenhuma cotação disponível para salvar.")

#chamadas das funções
def main():
    valor = solicitar_valor()
    data = solicitar_data()
    consultar_cotacao_moedas(valor, data)

#executa o programa
main()