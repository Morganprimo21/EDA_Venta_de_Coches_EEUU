import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA USA Cars", layout="wide")

sns.set(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.figsize': (10, 6), 'axes.titlesize': 8, 'axes.labelsize': 7, 'xtick.labelsize': 6, 'ytick.labelsize': 6})

file_path = "C:\\Users\\morga\\ia\\eda1\\Usa_cars_datasets.csv"
df = pd.read_csv(file_path)

if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

df['year'] = pd.to_numeric(df['year'], errors='coerce')

columns_available = df.columns

st.title("Análisis Exploratorio de Datos: Vehículos en USA")

option = st.selectbox(
    "Seleccione el análisis que desea realizar:",
    ["Distribución de Precios", 
     "Vehículos por Estado", 
     "Precio Promedio por Año", 
     "Precio Promedio por Marca",
     "Colores de Coches Más Vendidos"]
)

col1, col2 = st.columns([1, 1])

if option == "Distribución de Precios":
    with col1:
        st.header("Distribución de Precios")
        fig, ax = plt.subplots()
        sns.histplot(df['price'], bins=20, kde=True, color='skyblue', ax=ax)
        ax.set_title('Distribución de Precios')
        ax.set_xlabel('Precio ($)')
        ax.set_ylabel('Frecuencia')
        st.pyplot(fig)

    with col2:
        st.markdown("""
        - Los precios de la mayoría de los vehículos se concentran entre 10,000  y  20,000 dolares , indicando un mercado accesible para coches usados.
        - Una menor cantidad de vehículos se encuentra en rangos más altos, sugiriendo la presencia de coches de lujo o nuevos.
        - En Estados Unidos, el mercado de coches usados domina las ventas debido a su accesibilidad económica para una amplia gama de compradores.
        - Los precios más altos se relacionan con vehículos nuevos, eléctricos o de marcas de lujo, como Tesla y Porsche.
        """)

elif option == "Vehículos por Estado":
    with col1:
        st.header("Vehículos por Estado")
        vehicles_by_state = df['state'].value_counts().reset_index()
        vehicles_by_state.columns = ['state', 'count']
        fig, ax = plt.subplots()
        sns.barplot(data=vehicles_by_state.head(10), x='count', y='state', palette='viridis', ax=ax)
        ax.set_title('Vehículos por Estado (Top 10)')
        ax.set_xlabel('Cantidad')
        ax.set_ylabel('Estado')
        st.pyplot(fig)

    with col2:
        st.markdown("""
        - Los estados con mayor cantidad de vehículos en venta son California, Texas y Florida.
        - Estos estados también representan grandes centros económicos y áreas de alta densidad poblacional.
        - California y Texas tienen grandes mercados debido a su tamaño y economía diversificada. California, por ejemplo, tiene una fuerte presencia de marcas eléctricas como Tesla.
        - Florida, con su población de jubilados, muestra una alta rotación de vehículos, lo que alimenta el mercado de coches usados.
        """)

elif option == "Precio Promedio por Año":
    with col1:
        st.header("Precio Promedio por Año (Desde 2000)")
        df_filtered = df[df['year'] >= 2000]
        average_price_by_year = df_filtered.groupby('year')['price'].mean().sort_index().reset_index()
        average_price_by_year.columns = ['year', 'average_price']
        fig, ax = plt.subplots()
        sns.lineplot(data=average_price_by_year, x='year', y='average_price', marker='o', color='green', ax=ax)
        ax.set_title('Precio Promedio por Año (Desde 2000)')
        ax.set_xlabel('Año')
        ax.set_ylabel('Precio Promedio ($)')
        st.pyplot(fig)

    with col2:
        st.markdown("""
        - Los precios promedio de vehículos más nuevos son consistentemente más altos debido al menor desgaste y depreciación.
        - Se observa un comportamiento errático alrededor de 2008-2010, coincidiendo con la crisis financiera global, que afectó significativamente la demanda y los precios de los vehículos.
        - La depreciación de los coches influye directamente en su valor: los coches más antiguos tienden a perder valor rápidamente.
        - Eventos económicos, como la recesión de 2008, aumentaron la demanda de vehículos usados más baratos, afectando el mercado de modelos nuevos.
        """)

elif option == "Precio Promedio por Marca":
    with col1:
        st.header("Precio Promedio por Marca")
        price_by_brand = df.groupby('brand')['price'].mean().sort_values(ascending=False).reset_index()
        price_by_brand.columns = ['brand', 'average_price']
        fig, ax = plt.subplots()
        sns.barplot(data=price_by_brand.head(10), x='average_price', y='brand', palette='coolwarm', ax=ax)
        ax.set_title('Precio Promedio por Marca (Top 10)')
        ax.set_xlabel('Precio Promedio ($)')
        ax.set_ylabel('Marca')
        st.pyplot(fig)

    with col2:
        st.markdown("""
        **Marcas Principales**:
        - Marcas premium como Porsche, Tesla y BMW dominan en precios más altos.
        - Marcas populares y asequibles como Ford y Chevrolet tienen precios promedio moderados.

        **Explicación Contextual**:
        - Las marcas premium reflejan un enfoque en lujo, innovación y prestigio. Tesla, por ejemplo, lidera en coches eléctricos con precios altos debido a la percepción de tecnología avanzada.
        - Marcas como Ford y Chevrolet se centran en vehículos accesibles, como camionetas y SUVs, ampliamente adoptados en zonas rurales y suburbanas.
        """)

elif option == "Colores de Coches Más Vendidos":
    with col1:
        st.header("Colores de Coches Más Vendidos")
        

        color_counts = df['color'].value_counts().reset_index()
        color_counts.columns = ['Color', 'Cantidad']
        top_colors = color_counts.head(10)
        
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('beige')  
        
        color_palette = {
            'white': '#9b59b6', 'black': '#34495e', 'red': '#e74c3c', 
            'blue': '#3498db', 'grey': '#7f8c8d', 'silver': '#bdc3c7',
            'green': '#27ae60', 'yellow': '#f1c40f', 'brown': '#8e44ad',
            'purple': '#9b59b6', 'orange': '#e67e22', 'gold': '#f39c12'
        }
        colors = [color_palette.get(color.lower(), '#95a5a6') for color in top_colors['Color']]
        
        # Bar chart
        bars = ax.bar(top_colors['Color'], top_colors['Cantidad'], color=colors, edgecolor='black')
        ax.set_title('Distribución de Colores de Coches Más Vendidos (Top 10)')
        ax.set_xlabel('Color')
        ax.set_ylabel('Cantidad')
        ax.set_xticklabels(top_colors['Color'], rotation=45, ha='right')

        # Añadir etiquetas en cada barra
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                        textcoords="offset points",
                        ha='center', va='bottom')

       
        st.pyplot(fig)


    with col2:
        st.markdown("""
        - Los colores más vendidos son generalmente neutrales como blanco, negro y gris.
        - Los colores vibrantes, como el rojo o azul, son populares en segmentos específicos como deportivos.
        - Los colores neutros son populares por su versatilidad y facilidad para revender el vehículo.
        - Los colores llamativos son preferidos por compradores que buscan destacarse, especialmente en vehículos deportivos.
        """)