import requests
import sys
import json


def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = json.loads(response.text)
    price = float(data['bpi']['USD']['rate'].replace(',', ''))
    return price


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
            

def main():
    if len(sys.argv) == 2:
        if isfloat(sys.argv[1]):
            amount = float(sys.argv[1])
            price = get_price()
            print(f"${(amount * float(price)):,.4f}")
        else:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")



if __name__ == "__main__":
    main()