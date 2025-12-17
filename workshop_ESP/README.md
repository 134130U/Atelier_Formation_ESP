
## Comment Exécuter le Projet

### 1. Prérequis

- Python 3.8+
- Git

### 2. Installation

1.  **Clonez le dépôt :**
    ```bash
    git clone https://github.com/134130U/Atelier_Formation_ESP.git
    cd Atelier_Formation_ESP
    ```

2.  **Créez un environnement virtuel et activez-le :**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Installez les bibliothèques requises :**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Exécutez le Pipeline ETL

Avant de lancer le tableau de bord, vous devez exécuter le script ETL pour traiter les données. Cela générera le fichier `olist_prepared_data.csv` requis par le tableau de bord.

```bash
python workshop_ESP/ETL.py
```

### 4. Lancez le Tableau de Bord

Une fois le processus ETL terminé, vous pouvez démarrer l'application Dash.

```bash
python workshop_ESP/dashboard_olist.py
```

L'application sera disponible à l'adresse [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

## Fichiers Clés

- `workshop_ESP/ETL.py` : Le script pour le pipeline d'Extraction, Transformation et Chargement (ETL).
- `workshop_ESP/dashboard_olist.py` : Le fichier principal de l'application de tableau de bord Dash.
- `workshop_ESP/config.py` : Fichier de configuration pour les chemins et les paramètres.
- `workshop_ESP/data/olist.db` : La base de données SQLite contenant les données brutes.
- `workshop_ESP/data/requete.sql` : La requête SQL utilisée pour extraire les données de la base de données.
