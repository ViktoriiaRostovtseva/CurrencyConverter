import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    
    return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate is None:
        return "Error: exchange rate not found"
    
    converted_amount = amount * rate
    return f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}"

if __name__ == "__main__":
    print("Currency Converter 🌍")
    base = input("Enter the base currency (e.g., USD): ").upper()
    target = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount: "))

    result = convert_currency(amount, base, target)
    print(result)
