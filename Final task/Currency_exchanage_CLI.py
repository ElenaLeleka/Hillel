#API NBU: https://bank.gov.ua/ua/open-data/api-dev
#Format of request: https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20220327&json
#Earliest date when possible request - https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=19960106&json

import sys
import datetime
import requests
from requests.exceptions import HTTPError, ConnectionError 
import help_strings

def print_formatted(message):
    print(">")
    print ('-'*14)
    print(message)
    print ('='*14)

def print_exchange_rate(currency_str, rate_str):
    print_formatted(f"{currency_str}\n\n{rate_str}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_formatted(help_strings.MAIN_HELP_STRING)
        exit()

    currency_code = ''
    if len(sys.argv) >= 2:
        currency_code = sys.argv[1]
        if len(currency_code) >3:
            print_formatted(
                f"{currency_code}\n\n"+
                f"Currency code cannot be longer than 3 characters: {currency_code} \n"+
                "For a list of supported currency codes see:\n"+
                "\thttps://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json\n   (json field 'cc')"
            )
            exit()
    
    requested_date = datetime.datetime.now()

    if len(sys.argv) >=3:
        try:
            requested_date = datetime.datetime.fromisoformat(sys.argv[2])
        except Exception as err:
            print_formatted("Invalid date: " + sys.argv[2])
            exit()

        if requested_date <= datetime.datetime.fromisoformat("1996-01-05"):
            print_formatted(
                f"Date provided: {requested_date} \n"+
                "is earlier than the date from which exchange rates are available (1996-01-06 for USD)."+
                "For other currencies availability start dates may be even later."
            )
            exit()
 
    date_str = requested_date.strftime("%Y%m%d")

    request_URL = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code.upper()}&date={date_str}&json"

    try:
        #Sometimes API does return an error, changing of User-Agent helps.        
        # headers = {
        #      'User-Agent': 'Mozilla/4.0 (Windows NT 11.0; rv:91.0) Firefox/78.0'
        # }
        # rate_json = requests.get(request_URL, headers = headers)

        rate_json = requests.get(request_URL)
        
        if("Request unsuccessful." in rate_json.text):
            print("Request unsuccessfull. Please try later (e.g. in 1-3 minutes).")
            exit()

    except HTTPError as http_err:
        print_formatted(f'HTTP error occurred: {http_err}')
        exit()
    except ConnectionError  as connect_err:
        print_formatted(f'Connection error occurred (please ensure that site https://bank.gov.ua is reachable from this machine): \n {connect_err}')  # Python 3.6
        exit()
    except Exception as err:
        print_formatted(f'System Error: {err}')
        exit()

    if len(rate_json.json()) == 0:
        print_formatted("Invalid currency: "+currency_code)
        exit()

    received_rate_json = rate_json.json()[0]
    print_exchange_rate(received_rate_json['cc'], received_rate_json['rate'])
