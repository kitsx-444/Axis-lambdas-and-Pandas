# axis tells pandas which direction to apply the function.
# axis=0:  apply column by column (default)
# axis=1: apply row by row

import pandas as pd

df_01 = pd.read_csv('performance_02.csv')
df_02 = pd.read_csv('sentiment_01.csv')

new_df = df_01.merge(df_02)

new_df['Signal'] = new_df.apply(lambda x: 'Buy' if x['Pips'] > 0 and x['Sentiment'] == 'Bullish' else 'Sell' if x['Pips'] < 0 and x['Sentiment'] == 'Bearish' else 'Hold', axis=1)

buys = new_df[new_df['Signal'] == 'Buy']

print(new_df)
print('\n',buys)
