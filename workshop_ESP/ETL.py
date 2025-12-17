"""
Module de chargement des données depuis SQLite
"""
import pandas as pd
import sqlite3
from config import DB_PATH, requet_PATH

def load_data():
    """
    Charge toutes les tables depuis la base SQLite

    Returns:
        dict: Dictionnaire contenant tous les DataFrames
        pd.DataFrame: Rapport de nettoyage
    """
    print("\n📥 COLLECTE DES DONNÉES")
    print("="*60)

    # Vérifier l'existence de la base
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Base de données non trouvée : {DB_PATH}")

    try:
        conn = sqlite3.connect(str(DB_PATH))
        print("\nChargement des tables:")
        print("-" * 40)
        df = pd.read_sql_query(requet_PATH, conn)
        return df

    except Exception as e:
        if 'conn' in locals():
            conn.close()
        raise Exception(f"Erreur lors du chargement : {e}")

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df_fact["order_purchase_timestamp"] = pd.to_datetime(df_fact["order_purchase_timestamp"])
    df_fact["order_month"] = df_fact["order_purchase_timestamp"].dt.to_period("M").astype(str)

    df_fact["total_price"] = df_fact["price"] + df_fact["freight_value"]

    df_fact["delivery_time"] = (
            pd.to_datetime(df_fact["order_delivered_customer_date"])
            - df_fact["order_purchase_timestamp"]
    ).dt.days

    df_fact['delivery_vs_estimate'] = (
            pd.to_datetime(df_fact['order_delivered_customer_date']) -
            pd.to_datetime(df_fact['order_estimated_delivery_date'])
    ).dt.days
    df_fact["order_weekday"] = df_fact["order_purchase_timestamp"].dt.day_name()
    df_fact["order_weekday_num"] = df_fact["order_purchase_timestamp"].dt.weekday
    df_fact["order_quater"] = df_fact["order_purchase_timestamp"].dt.quarter
    df_fact["order_year"] = df_fact["order_purchase_timestamp"].dt.year
    df_fact["order_hour"] = df_fact["order_purchase_timestamp"].dt.hour