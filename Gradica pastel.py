import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
df = pd.read_csv("sales_data_webstore.csv", sep=';')

# Agrupar por 'Product' y 'Country', y contar la cantidad de ocurrencias
producto_pais = df.groupby(['Product', 'Country']).size().reset_index(name='Count')

# Crear una tabla con la suma de ocurrencias por país
producto_pais_total = producto_pais.groupby('Country')['Count'].sum().reset_index()

# Crear el gráfico de pastel para mostrar la distribución de productos por país
plt.figure(figsize=(10, 8))

# Crear gráfico de pastel basado en las sumas por país
plt.pie(producto_pais_total['Count'], labels=producto_pais_total['Country'], autopct='%1.1f%%', startangle=140)

# Título
plt.title('Distribución de ventas por País')

# Mostrar el gráfico
plt.show()
