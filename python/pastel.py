import matplotlib.pylab as plt
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("sales_data_webstore.csv", sep=';')

# Agrupar por 'Category' y calcular la suma de 'Total Price' para cada categoría
categoria_ventas = df.groupby('Category')['Total Price'].sum()

# Crear un gráfico de pastel
plt.figure(figsize=(10, 8))
categoria_ventas.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='tab20')

# Añadir título
plt.title('Porcentaje de ventas por Categoría')

# Mostrar el gráfico
plt.ylabel('')  # Eliminar la etiqueta 'y' que aparece por defecto
plt.show()
