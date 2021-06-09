import requests
import settings

class Courses:
    currency_root_urls = settings.bank_root_urls

    def __init__(self, country=None):
        self.country = country.lower()

    def get_today_currencies(self):
        root_url = self.currency_root_urls[f"{self.country}_root_url"]

        if self.country == "rb":
            url = f"{root_url}?periodicity=0"
        if self.country == "uk":
            url = f"{root_url}exchange?json"

        try:
            res = requests.get(url)
            today_currencies = res.json()
            return today_currencies
        except Exception:
            raise Exception(f"Something wrong with request: {res}")

    def today_currency_by_abbr(self, money_abbr=""):
        today_currencies = self.get_today_currencies()

        for curr in today_currencies:
            if self.country == "rb":
                if curr["Cur_Abbreviation"] == money_abbr:
                    return curr
                if self.country == "uk":
                    if curr["cc"] == money_abbr:
                        return curr
"""

currency = Courses(country="UK")

curr = currency.today_currency_by_abbr(money_abbr="USD")

print(curr)
"""
