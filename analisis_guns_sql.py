import pandas as pd

# Cargamos el CSV en un DataFrame
df = pd.read_csv("guns_n_roses_spotify_dataset.csv")

# Mostramos las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Mostramos los nombres de las columnas
print("\nColumnas del dataset:")
print(df.columns)

# Mostramos información general del DataFrame
print("\nInformación general:")
df.info()

# Consultas básicas tipo SQL con Pandas
print("\nCantidad total de canciones:")
print(len(df))

print("\nCantidad de álbumes únicos:")
print(df["album"].nunique())

print("\nCantidad de canciones por álbum:")
print(df["album"].value_counts())

print("\nCanciones más largas:")
print(
    df[["cancion", "album", "duracion_min"]]
    .sort_values(by="duracion_min", ascending=False)
    .head(10)
)

print("\nDuración promedio por álbum:")
print(
    df.groupby("album")["duracion_min"]
    .mean()
    .sort_values(ascending=False)
)