"""
Configuration globale pour le projet Olist
"""
import os
from pathlib import Path

# ========== CHEMINS ==========
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")

# Fichiers
DB_PATH = os.path.join(DATA_DIR, "olist.db")
requet_PATH = os.path.join(DATA_DIR, "requete.sql")
datetime_col = ["order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"]
# print(BASE_DIR, os.path.exists(BASE_DIR))
# print(DATA_DIR,os.path.exists(DATA_DIR))
# print(DB_PATH,os.path.exists(DB_PATH))
# print(requet_PATH,os.path.exists(requet_PATH))
