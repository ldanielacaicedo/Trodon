import matplotlib.pylab as plt
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("sales_data_webstore.csv", sep=';')

# Agrupar por 'Category' y calcular la suma de 'Total Price' para cada categoría
categoria_ventas = df.groupby('Category')['Total Price'].sum()

# Crear un gráfico de barras
plt.figure(figsize=(10, 8))
categoria_ventas.plot(kind='bar', color=['#1f77b4', '#aec7e8'])  # Colores personalizados

# Añadir título y etiquetas
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')

# Mostrar el gráfico
plt.show()
