import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Declaración de las listas con los datos de cada red social
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]

# Matriz / Lista de listas
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# Creación del DataFrame (Corregido)
# a cada columna le ponemos un nombre
df_redes_sociales = pd.DataFrame(lista_redes_sociales,
                       columns=["Nombre", "Cantidad", "Es_FB", "Año"])

print(df_redes_sociales)
# Creamos el archivo CSV y Lo guardamos en csv
# df_redes_sociales.to_csv("Redessociales.csv", index=False)
# Crear graficas de lineas 
# donde x es "Nombre",en el eje horizontal
# donde y es "Cantidad",en el eje Vertical
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title ("Grafica redes sociales 0093")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Crear una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.show()
# Grafica de barras
plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title ("Redes sociales 0093")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# obtener la grafica de barras de manera descendete
# De la mas grande a la mas pequeña
df_rs_ordenarla = df_redes_sociales.sort_values("Cantidad",ascending =False)
plt.bar(df_rs_ordenarla["Nombre"],df_rs_ordenarla["Cantidad"])
plt.show()
# Coloreando la grafica
df_rs_ordenarla = df_redes_sociales.sort_values("Cantidad",ascending =False)
plt.bar(df_rs_ordenarla["Nombre"],df_rs_ordenarla["Cantidad"],
        color =["b","g","c","m","y","r"])
plt.show()

# plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],
        labels = df_redes_sociales["Nombre"])
plt.show()