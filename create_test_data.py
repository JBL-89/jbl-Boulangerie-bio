#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour créer des commandes d'exemple avec les vraies données
"""

import sqlite3
import random
from datetime import datetime, timedelta

DATABASE_PATH = "boulangerie.db"

def create_sample_orders():
    """Crée des commandes d'exemple pour tester l'application"""
    print("Création de commandes d'exemple...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Récupérer les clients et produits
    clients = cursor.execute("SELECT id, prenom, nom FROM users WHERE role='client'").fetchall()
    produits = cursor.execute("SELECT id, nom, prix FROM produits").fetchall()
    
    if not clients or not produits:
        print("❌ Aucun client ou produit trouvé. Exécutez d'abord import_excel_data.py")
        return
    
    # Créer 10 commandes d'exemple
    for i in range(10):
        # Choisir un client aléatoire
        client = random.choice(clients)
        
        # Date de commande (derniers 30 jours)
        date_commande = datetime.now() - timedelta(days=random.randint(0, 30))
        
        # Statut aléatoire
        statuts = ['confirmee', 'en_preparation', 'prete', 'livree', 'payee']
        statut = random.choice(statuts)
        
        # Numéro de commande
        numero = f"CMD{date_commande.strftime('%Y%m%d')}{i+1:03d}"
        
        # Créer la commande
        cursor.execute('''
            INSERT INTO commandes (numero, client_id, date_commande, statut, total)
            VALUES (?, ?, ?, ?, ?)
        ''', (numero, client[0], date_commande, statut, 0))
        
        commande_id = cursor.lastrowid
        
        # Ajouter 2-5 produits aléatoires
        nb_produits = random.randint(2, 5)
        total_commande = 0
        
        for _ in range(nb_produits):
            produit = random.choice(produits)
            quantite = random.randint(1, 10)
            prix_unitaire = produit[2]
            sous_total = quantite * prix_unitaire
            total_commande += sous_total
            
            cursor.execute('''
                INSERT INTO commande_items (commande_id, produit_id, quantite, prix_unitaire, sous_total)
                VALUES (?, ?, ?, ?, ?)
            ''', (commande_id, produit[0], quantite, prix_unitaire, sous_total))
        
        # Mettre à jour le total de la commande
        cursor.execute('UPDATE commandes SET total = ? WHERE id = ?', (total_commande, commande_id))
        
        # Si la commande est payée, ajouter un paiement
        if statut == 'payee':
            mode_paiement = random.choice(['especes', 'carte_bancaire', 'cheque', 'virement'])
            cursor.execute('''
                INSERT INTO paiements (commande_id, montant, mode_paiement, date_paiement)
                VALUES (?, ?, ?, ?)
            ''', (commande_id, total_commande, mode_paiement, date_commande.date()))
        
        print(f"✓ Commande {numero} créée pour {client[1]} {client[2]} - {total_commande:.2f}€ ({statut})")
    
    conn.commit()
    conn.close()
    print(f"✅ {len(range(10))} commandes d'exemple créées !")

def create_sample_entreprises():
    """Crée quelques entreprises d'exemple"""
    print("Création d'entreprises d'exemple...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    entreprises = [
        {
            'nom': 'Biocoop Latresne',
            'adresse': '123 Avenue de la Paix\n33270 Latresne',
            'siren': '123456789',
            'numero_tva': 'FR12123456789',
            'email': 'contact@biocoop-latresne.fr',
            'telephone': '05 56 20 30 40'
        },
        {
            'nom': 'Naturalia Saint-Christoly',
            'adresse': '17 rue du Père Louis Jabrun\n33000 Bordeaux',
            'siren': '987654321',
            'numero_tva': 'FR12987654321',
            'email': 'bordeaux@naturalia.fr',
            'telephone': '05 56 44 55 66'
        }
    ]
    
    for entreprise in entreprises:
        try:
            cursor.execute('''
                INSERT INTO entreprises (nom, adresse, siren, numero_tva, email, telephone)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (entreprise['nom'], entreprise['adresse'], entreprise['siren'], 
                  entreprise['numero_tva'], entreprise['email'], entreprise['telephone']))
            print(f"✓ Entreprise créée: {entreprise['nom']}")
        except sqlite3.IntegrityError:
            print(f"✗ Entreprise déjà existante: {entreprise['nom']}")
    
    conn.commit()
    conn.close()
    print("✅ Entreprises d'exemple créées !")

def update_some_clients_with_entreprises():
    """Associe quelques clients avec des entreprises"""
    print("Association clients-entreprises...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Récupérer les entreprises
    entreprises = cursor.execute("SELECT id, nom FROM entreprises").fetchall()
    
    if entreprises:
        # Associer quelques clients
        clients_a_associer = [
            ('Biocoop', 'Latresne'),
            ('Naturalia', 'St')
        ]
        
        for entreprise in entreprises:
            for client_pattern in clients_a_associer:
                if client_pattern[0] in entreprise[1] or client_pattern[1] in entreprise[1]:
                    cursor.execute('''
                        UPDATE users SET entreprise_id = ? 
                        WHERE prenom LIKE ? OR nom LIKE ?
                    ''', (entreprise[0], f'%{client_pattern[0]}%', f'%{client_pattern[1]}%'))
                    print(f"✓ Clients associés à {entreprise[1]}")
    
    conn.commit()
    conn.close()
    print("✅ Associations clients-entreprises terminées !")

if __name__ == "__main__":
    print("=== CRÉATION DE DONNÉES DE TEST ===")
    print()
    
    create_sample_entreprises()
    print()
    
    update_some_clients_with_entreprises()
    print()
    
    create_sample_orders()
    print()
    
    print("=== DONNÉES DE TEST CRÉÉES ===")
    print("Vous pouvez maintenant tester l'application avec des données réalistes !")
    print("URL: http://localhost:8501")
    print("Connexion: admin@aquibiopain.com / admin123")