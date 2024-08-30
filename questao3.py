import json

with open('./calculo do faturamento/faturamento.json') as f:
    dados_faturamento = json.load(f)

faturamentos = [dia["faturamento"] for dia in dados_faturamento if dia["faturamento"] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = len([f for f in faturamentos if f > media_mensal])

print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
