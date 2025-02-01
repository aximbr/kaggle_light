import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import math
api = KaggleApi()
api.authenticate()
import pandas as pd

MAX_DS = 20
MAX_PAGE = math.ceil(MAX_DS/20)
KEYWORD = 'Computer Science'

datasets = []
for i in range(MAX_PAGE):
    datasets = datasets + api.datasets_list(search=KEYWORD, page=i)
                
df = pd.DataFrame(datasets)
#df.to_csv('kaggle_ds_list.csv')
print(df.head())

