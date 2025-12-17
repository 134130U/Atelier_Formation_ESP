"""
Module de chargement des données depuis SQLite
"""
import pandas as pd
import sqlite3
import os
from config import DB_PATH, requet_PATH, DATA_DIR

def load_data():
    print("\n COLLECTE DES DONNÉES")
    print("="*60)

    # Vérifier l'existence de la base
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Base de données non trouvée : {DB_PATH}")

    try:
        conn = sqlite3.connect(DB_PATH)
        print("\nChargement des tables:")
        print("-" * 40)
        with open(requet_PATH, "r", encoding="utf-8") as f:
            sql_query = f.read()
        df = pd.read_sql_query(sql_query, conn)
        print(f'Chargement réussi avec {len(df)} lignes')
        return df

    except Exception as e:
        if 'conn' in locals():
            conn.close()
        raise Exception(f"Erreur lors du chargement : {e}")

def transform_load_data(df: pd.DataFrame) -> pd.DataFrame:
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

    df["total_price"] = df["price"] + df["freight_value"]

    df["delivery_days"] = (
            pd.to_datetime(df["order_delivered_customer_date"])
            - df["order_purchase_timestamp"]
    ).dt.days

    df["delivery_vs_estimate"] = (
            pd.to_datetime(df["order_delivered_customer_date"]) -
            pd.to_datetime(df["order_estimated_delivery_date"])
    ).dt.days
    df["order_weekday"] = df["order_purchase_timestamp"].dt.day_name()
    df["order_weekday_num"] = df["order_purchase_timestamp"].dt.weekday
    df["order_quater"] = df["order_purchase_timestamp"].dt.quarter
    df["order_year"] = df["order_purchase_timestamp"].dt.year
    df["order_hour"] = df["order_purchase_timestamp"].dt.hour
    df.to_csv(os.path.join(DATA_DIR, "olist_prepared_data.csv"), index=False)
    print(f"Data have been well processed and saved to {DATA_DIR}")
    return f"Data have been well processed and saved to {DATA_DIR}"

if __name__ == "__main__":
    df = load_data()
    transform_load_data(df)