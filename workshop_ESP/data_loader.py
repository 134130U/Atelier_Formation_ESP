"""
Module de chargement des données depuis SQLite
"""
import pandas as pd
import sqlite3
from config import DB_PATH

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



        return dfs, pd.DataFrame(cleaning_stats)

    except Exception as e:
        if 'conn' in locals():
            conn.close()
        raise Exception(f"Erreur lors du chargement : {e}")

def load_single_table(table_name):
    """
    Charge une seule table (utile pour debug)
    """
    conn = sqlite3.connect(str(DB_PATH))
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
