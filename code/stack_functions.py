import pandas as pd
import numpy as np
from collections import defaultdict
from forex_python.converter import CurrencyRates, CurrencyCodes 
from forex_python.bitcoin import BtcConverter

def convert2USD(cur_name_from: str, amount: float):
    '''
    Use forex_python to convert the currencies found in the dataset into US dollars
    cur_name_from - currency to convert in USD
    amount - float represneting the amount to convert
    '''
    
    if cur_name_from == 'U.S. dollars ($)':
        return amount
    
    if cur_name_from == 'Bitcoin (btc)':
        c = BtcConverter()
        btc_rate = c.get_latest_price('USD')
        return amount*btc_rate
    
    cur_dict = dict(
        AUD = 'Australian dollars (A$)',
        btc = 'Bitcoin (btc)',
        BRL = 'Brazilian reais (R$)',
        GBP = 'British pounds sterling (£)',
        CAD = 'Canadian dollars (C$)',
        CNY = 'Chinese yuan renminbi (¥)',
        EUR = 'Euros (€)',
        INR = 'Indian rupees (?)',
        JPY = 'Japanese yen (¥)',
        MXN = 'Mexican pesos (MXN$)',
        PLN = 'Polish zloty (zl)',
        RUB = 'Russian rubles (?)',
        SGD = 'Singapore dollars (S$)',
        ZAR = 'South African rands (R)',
        SEK = 'Swedish kroner (SEK)',
        CHF = 'Swiss francs',
        USD = 'U.S. dollars ($)'   
    )
    
    cur_code_from = [code for code, name in cur_dict.items() if name == cur_name_from][0]
    c = CurrencyRates()
    return c.convert(cur_code_from,'USD', amount)


def getChoices(quest_series):
    '''
    get all unique responses to a categorical question (series example df['DevType'])
    dictIdx: list observation indices in which each choice is found 
    '''
    dictIdx = defaultdict(list)
    
    for idx, choice in enumerate(quest_series):
        if isinstance(choice, str):
            list_choice = [x.lstrip() for x in choice.split(';')]
            for x in list_choice:
                dictIdx[x].append(idx)
    
    return dictIdx
