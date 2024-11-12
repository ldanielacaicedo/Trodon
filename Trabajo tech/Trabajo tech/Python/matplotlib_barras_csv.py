import matplotlib.pyplot as pit
import pandas as pd

df = pd.read_csv ("services_data_webstore_semicolon.csv", sep= ';')

categoria_ventas = df.groupby (['Payment Method', 'Country']).size () .unstack ()

plt.figure(figsize=(10,6))
categoria_ventas.plot (kind= 'bar', stacked=true)
plt.xlabel('Metodo de pago')
plt.ylabel('Cantidad de paises')
plt.title('Cantidad de ventas por servicio y Pais')
plt.show()