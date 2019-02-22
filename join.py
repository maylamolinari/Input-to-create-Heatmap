import pandas as pd
import os

xls = pd.ExcelFile('excel.xlsx')

exchanges = xls.sheet_names

print('Esses sao todos os sheets do arquivo:')
print(exchanges)

listings = []

for exchange in exchanges:
	listing=pd.read_excel(xls, sheet_name=exchange, usecols="A,B")
#	listing['exchange'] = exchange # Add reference column
	listings.append(listing) # add dataframe to list

merged_reduce=reduce(lambda x, y: pd.merge(x, y, on='GeneName', how='outer'), listings)

print('Resultado:')
print(merged_reduce)

writer = pd.ExcelWriter('output.xlsx')
merged_reduce.to_excel(writer,'Results')
writer.save()

print('Tabela salva em output.xlsx')

