import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_empleados = pd.read_csv("C:/Users/slmanzano/Desktop/Sara/Talent Camp/Python/Empleados.csv",sep=";",encoding="ISO-8859-1")

# para establecer etiquetas de los ejes
plt.xlabel('EDAD EMPLEADO', c='purple')
plt.ylabel('SALARIO ANUAL EMPLEADO', c='orange')

# con gradiente de color con cmap
plt.subplot()
x_edad = np.array(df_empleados["EDAD"])
y_salario = np.array(df_empleados["SALARIO ANUAL"])
plt.scatter(x_edad,y_salario,color='red')
colores_grado = y_salario # en este caso el nivel de cada punto lo he establecido con el peso
plt.scatter(x_edad, y_salario, c=colores_grado,cmap='Purples') # en cmap metemos un valor de una lista predefinida
plt.colorbar() # para que muestre la barra de color

plt.legend() # muestra las leyendas
plt.show() # lanza el grafico