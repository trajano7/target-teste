# Questao 3
# Versao do Python: 3.10.12

import json

def getFaturamentoInfo(data):
  nonZeroData = list(filter(lambda v: v['valor'] > 0, data))
  lowestValue = min(nonZeroData, key=lambda v: v['valor'])
  greaterValue = max(nonZeroData, key=lambda v: v['valor'])
  
  values = [v['valor'] for v in nonZeroData]
  average = sum(values) / len(values)
  days = len(list(filter(lambda value: value > average, values)))
  
  print(f"O menor faturamento foi de {lowestValue['valor']:,.2f}, no dia {lowestValue['dia']}.")
  print(f"O maior faturamento foi de {greaterValue['valor']:,.2f}, no dia {greaterValue['dia']}.")
  print(f"Em {days} dias, o valor de faturamento diário foi maior que a média mensal de {average:,.2f}.")

def readJSON(fileName):
  with open(fileName, 'r') as file:
    data = json.load(file)
    
  return data

getFaturamentoInfo(readJSON("faturamento.json"))