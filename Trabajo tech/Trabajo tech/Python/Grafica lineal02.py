import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("sales_data_webstore.csv", sep=';')
plt.figure(figsize=(20,12))
categoria_ventas = df.groupby('Payment Method') ['Total Price'].sum()
categoria_ventas.plot(kind='line')
plt.xlabel('Categoria')
plt.ylabel('Ventas')
plt.title('Total ventas por categoria')
plt.show()
