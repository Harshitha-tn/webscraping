
import pandas as pd
filename = 'inspirational_quotes.csv'

df = pd.read_csv(filename,encoding='ISO-8859-1')


print(df)
for index, row in df.iterrows():
    print(f"Theme: {row['theme']}")
    print(f"Quote: {row['lines']}")
    print(f"Author: {row['author']}")
    print(f"URL: {row['url']}")
    print(f"Image URL: {row['img']}")
    print('-' * 50)  
