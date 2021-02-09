import pandas as pandas

#Read the csv file
df = pd.read_csv('..Resources/cities.csv')

#Save to file
dfto_html('data.html'. index=False)

#Assign to string
table = df.to_html()
print(table)