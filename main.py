names=['Adam','Juliusz','Jan','Czesław']
last_names=['Mickiewicz','Słowacki','Brzechwa','Miłosz']
years=[1855,1849,1966,2004]
print(len(list(zip(names,last_names,years))))

for i in list(zip(names,last_names,years)):
    print(f"autor: {i[0]} {i[1]} zmarł: {i[2]}")