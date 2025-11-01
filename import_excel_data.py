#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'importation des données du tableau Excel dans la base de données
"""

import pandas as pd
import sqlite3
import hashlib
from datetime import datetime

DATABASE_PATH = "boulangerie.db"

def init_database():
    """Initialise la base de données avec toutes les tables"""
    print("Initialisation de la base de données...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Table des utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prenom TEXT NOT NULL,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telephone TEXT,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'client',
            entreprise_id INTEGER,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (entreprise_id) REFERENCES entreprises (id)
        )
    ''')
    
    # Table des entreprises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entreprises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            adresse TEXT,
            siren TEXT,
            numero_tva TEXT,
            contact_principal TEXT,
            email TEXT,
            telephone TEXT,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table des produits
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            description TEXT,
            prix REAL NOT NULL,
            categorie TEXT,
            image_url TEXT,
            stock INTEGER DEFAULT 0,
            stock_min INTEGER DEFAULT 5,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table des commandes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT UNIQUE NOT NULL,
            client_id INTEGER NOT NULL,
            date_commande TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            statut TEXT DEFAULT 'en_attente',
            total REAL DEFAULT 0,
            commentaires TEXT,
            FOREIGN KEY (client_id) REFERENCES users (id)
        )
    ''')
    
    # Table des items de commande
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commande_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commande_id INTEGER NOT NULL,
            produit_id INTEGER NOT NULL,
            quantite INTEGER NOT NULL,
            prix_unitaire REAL NOT NULL,
            sous_total REAL NOT NULL,
            FOREIGN KEY (commande_id) REFERENCES commandes (id),
            FOREIGN KEY (produit_id) REFERENCES produits (id)
        )
    ''')
    
    # Table des paiements
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paiements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commande_id INTEGER NOT NULL,
            montant REAL NOT NULL,
            mode_paiement TEXT NOT NULL,
            date_paiement DATE NOT NULL,
            reference TEXT,
            commentaire TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (commande_id) REFERENCES commandes (id)
        )
    ''')
    
    # Table des logs d'activité
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs_activite (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            details TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✓ Base de données initialisée")

def import_clients_from_excel():
    """Importe les clients depuis le fichier Excel"""
    print("Importation des clients...")
    
    file_path = 'TABLEAU COMMANDE CLIENT semaine 09-2025 calculs recettes.xlsm'
    
    try:
        # Lire la feuille Clients
        df_clients = pd.read_excel(file_path, sheet_name='Clients', header=None)
        
        # Les clients sont dans la première colonne à partir de la ligne 2
        clients = []
        for i in range(2, min(20, len(df_clients))):  # Limiter à 20 clients
            client_name = df_clients.iloc[i, 0]
            if pd.notna(client_name) and client_name != "Total":
                clients.append(str(client_name).strip())
        
        # Connexion à la base
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Insérer les clients
        password_hash = hashlib.sha256("password123".encode()).hexdigest()
        
        for client_name in clients:
            # Séparer prénom et nom si possible
            parts = client_name.split()
            if len(parts) >= 2:
                prenom = parts[0]
                nom = " ".join(parts[1:])
            else:
                prenom = client_name
                nom = ""
            
            # Générer un email
            email = f"{prenom.lower().replace(' ', '')}@{nom.lower().replace(' ', '')}.com"
            
            try:
                cursor.execute('''
                    INSERT INTO users (prenom, nom, email, password, role, telephone)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (prenom, nom, email, password_hash, 'client', '05 00 00 00 00'))
                print(f"✓ Client ajouté: {prenom} {nom}")
            except sqlite3.IntegrityError:
                print(f"✗ Client déjà existant: {prenom} {nom}")
        
        conn.commit()
        conn.close()
        print(f"Importation terminée: {len(clients)} clients traités")
        
    except Exception as e:
        print(f"Erreur lors de l'importation des clients: {e}")

def import_produits_from_excel():
    """Importe les produits depuis le fichier Excel"""
    print("Importation des produits...")
    
    file_path = 'TABLEAU COMMANDE CLIENT semaine 09-2025 calculs recettes.xlsm'
    
    try:
        # Lire la feuille Tarifs
        df_tarifs = pd.read_excel(file_path, sheet_name='Tarifs', header=None)
        
        # Les produits sont dans la première colonne à partir de la ligne 3
        produits = []
        for i in range(3, min(50, len(df_tarifs))):  # Parcourir les lignes de produits
            if pd.notna(df_tarifs.iloc[i, 0]):
                nom_produit = str(df_tarifs.iloc[i, 0]).strip()
                prix_unitaire = df_tarifs.iloc[i, 9] if pd.notna(df_tarifs.iloc[i, 9]) else 0
                
                if nom_produit and prix_unitaire > 0:
                    # Déterminer la catégorie
                    if "TRADITION" in nom_produit.upper():
                        categorie = "Pain Tradition"
                    elif "CAMPAGNE" in nom_produit.upper():
                        categorie = "Pain de Campagne"
                    elif "5 GRAINES" in nom_produit.upper():
                        categorie = "Pain aux Graines"
                    elif "SEIGLE" in nom_produit.upper():
                        categorie = "Pain de Seigle"
                    else:
                        categorie = "Autres"
                    
                    produits.append({
                        'nom': nom_produit,
                        'prix': float(prix_unitaire),
                        'categorie': categorie,
                        'description': f"Pain artisanal bio - {nom_produit}"
                    })
        
        # Connexion à la base
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Insérer les produits
        for produit in produits:
            try:
                cursor.execute('''
                    INSERT INTO produits (nom, description, prix, categorie, stock, stock_min)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (produit['nom'], produit['description'], produit['prix'], 
                      produit['categorie'], 100, 10))  # Stock initial
                print(f"✓ Produit ajouté: {produit['nom']} - {produit['prix']}€")
            except sqlite3.IntegrityError:
                print(f"✗ Produit déjà existant: {produit['nom']}")
        
        conn.commit()
        conn.close()
        print(f"Importation terminée: {len(produits)} produits traités")
        
    except Exception as e:
        print(f"Erreur lors de l'importation des produits: {e}")

def create_admin_user():
    """Crée l'utilisateur administrateur"""
    print("Création de l'utilisateur admin...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    password_hash = hashlib.sha256("admin123".encode()).hexdigest()
    
    try:
        cursor.execute('''
            INSERT INTO users (prenom, nom, email, password, role, telephone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ("Admin", "AQUI BIO PAIN", "admin@aquibiopain.com", password_hash, 'admin', "05 56 06 92 00"))
        print("✓ Utilisateur admin créé: admin@aquibiopain.com / admin123")
    except sqlite3.IntegrityError:
        print("✗ Utilisateur admin déjà existant")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("=== IMPORTATION DES DONNÉES EXCEL ===")
    print()
    
    # Initialiser la base de données d'abord
    init_database()
    print()
    
    create_admin_user()
    print()
    
    import_clients_from_excel()
    print()
    
    import_produits_from_excel()
    print()
    
    print("=== IMPORTATION TERMINÉE ===")
    print("Vous pouvez maintenant vous connecter avec:")
    print("Email: admin@aquibiopain.com")
    print("Mot de passe: admin123")