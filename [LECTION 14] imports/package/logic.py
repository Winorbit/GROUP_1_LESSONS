from . settings import *
from requests import get


def get_currency(currency:str, currency_type:str):
	url = f"{root_url}/{currency}/{currency_type}"
	res = get(url)
	if res.status_code == 200:
		return res.json()
	else:
		raise Exception(f"Request to {url} failed with code {res.status_code}")