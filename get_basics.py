from monzo.monzo import Monzo # Add link to source
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns #for the nicer default styles
from secret_string import *

def clean_df_for_pie(df):
    df = df[df.amount<0] #only take outgoings
    df  = df.groupby('category').sum() #reduce to cat type
    df = df*-1 #change sign
    return df

## get data off Monzo
client = Monzo(secret_string) 
account_id = client.get_first_account()['id'] 
transactions = client.get_transactions(account_id)['transactions']

## convert the interesting subset into a df
col = ['amount','include_in_spending','notes','category']
df = pd.DataFrame(data=transactions)[col]

dfx = clean_df_for_pie(df)
dfx = dfx[dfx.index!='entertainment'] # dominate catergory
plt.pie(dfx.amount,labels=dfx.index)