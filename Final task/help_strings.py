MAIN_HELP_STRING = """
    Usage:
        python Currency_exchange_CLI.py <currency code> <date>
        
        will print currency code exchange rate to Ukrainian Hryvna (UAH) for currency for current date (if no date specified) or for specific date if specified
        
        <currency code> is 3 letter currency code as specified in ISO 4217 standard: https://www.iso.org/iso-4217-currency-codes.html
        Note: not all codes are accepted, see below a note on provider of data

        <date> date in ISO format - YYYY-MM-DD. Optional. If not provided current date is used. Information on exchange rates is not available on all dates, see below a note on provider of data.upper()

        Example: 
            python Currency_exchange_CLI.py USD 1996-01-20

        Provider of data: National Bank of Ukraine (https://bank.gov.ua/)
        For more information see their API help page: https://bank.gov.ua/ua/open-data/api-dev

        For a list of currencies supported see - https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json
        "cc" field of the returned json provides currency codes supported as of 28Mar2022.upper()
        USD data is available starting 1996-01-06 for other currencies availability dates may differ.
"""
