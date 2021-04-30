import os

import pandas as pd

product=pd.read_excel('product.xlsx')
def chgetInfo():
    pass
def chget(val):
    product=pd.read_excel('product.xlsx')
    
    return {_:product[_][val] for _ in product.columns}

            
    