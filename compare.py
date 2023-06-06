from find_country import list_from_excell_col


found = list_from_excell_col("test.xlsx",["F"])

countries = []
with open("results.txt", "r") as f:
    for line in f:
        countries.append(line.strip())

for i in range(len(countries)):
    if countries[i] == "None" or found[0][i] == None:
        continue
    elif str(countries[i]) == str(found[0][i]):
       continue
    elif countries[i] == "Storbritannien" and found[0][i] == "England":
        continue
    else:
        print(i+2, countries[i], "!=", found[0][i])
