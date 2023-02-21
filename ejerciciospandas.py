import pandas as pd
data = pd.read_csv("./empleados.csv")



#filtrar epleados que solo sean analista 1

analistas1=data[data["cargo"]=='analista1']
print(analistas1)

#filtrar epleados que solo sean analista 2

analistas2=data[data["cargo"]=='analista2']
print(analistas2)

#Filtrar empleados en general que tengan menos de 30 años


filtro1=data[data["edad"]<30]
print(filtro1)


#Filtrar empleados en general que tengan mas de 50 años

filtro2=data[data["edad"]>50]
print(filtro2)

#¿Cuál es el promedio de salario de un analista 1?
filtropromedio=data["salario"].mean()

print("\n")
print (filtropromedio)



