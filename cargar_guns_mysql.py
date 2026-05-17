import pandas as pd
from sqlalchemy import create_engine, URL
from getpass import getpass

# ============================================================
# 1. CARGAR EL CSV
# ============================================================

df = pd.read_csv("guns_n_roses_spotify_dataset.csv")

print("CSV cargado correctamente")
print("Cantidad de filas:", len(df))
print("Columnas:", df.columns)


# ============================================================
# 2. PEDIR CONTRASEÑA DE MYSQL
# ============================================================

password_mysql = getpass("Ingrese la contraseña de MySQL: ")


# ============================================================
# 3. CREAR CONEXIÓN A MYSQL
# ============================================================

url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=password_mysql,
    host="localhost",
    database="data_guns"
)

engine = create_engine(url)


# ============================================================
# 4. CARGAR EL DATAFRAME COMO TABLA SQL
# ============================================================

df.to_sql(
    name="canciones_guns",
    con=engine,
    if_exists="replace",
    index=False
)

print("Dataset cargado correctamente en MySQL")
print("Tabla creada: canciones_guns")