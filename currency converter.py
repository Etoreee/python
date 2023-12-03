currencies = {'USD': 1, 'EUR': 0.9, 'UAH': 36.57, 'GBP': 0.82, 'JPY': 134.86}

def convert(amount, from_currency, to_currency):
    if from_currency not in currencies or to_currency not in currencies:
        return "Невірна валюта!"
    rate = currencies[to_currency] / currencies[from_currency]
    result = round(amount * rate, 2) 
    return f"{amount} {from_currency} = {result} {to_currency}"

print("Доступні валюти:", ", ".join(currencies.keys()))  

amount = float(input("Введіть суму для конвертації: "))
from_currency = input("З якої валюти конвертувати: ").upper()  
to_currency = input("В яку валюту конвертувати: ").upper()

print(convert(amount, from_currency, to_currency))