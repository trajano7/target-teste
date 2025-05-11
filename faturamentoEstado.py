# Questao 4
# Versao do Python: 3.10.12

data = [
    {"estado": "SP", "faturamento": 67836.43},
    {"estado": "RJ", "faturamento": 36678.66},
    {"estado": "MG", "faturamento": 29229.88},
    {"estado": "ES", "faturamento": 27165.48},
    {"estado": "Outros", "faturamento": 19849.53}
]

def invoicingStatistic():
  amount = sum([v['faturamento'] for v in data])
  
  for item in data:
    print(f"Percentual de representação do {item['estado']}: {(item['faturamento']/amount)*100:,.3f}%")
  
invoicingStatistic()