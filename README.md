# 🥖 SARL AQUI BIO PAIN - Application de Gestion

## 🎯 **PRÉSENTATION**

Application web complète de gestion pour **SARL AQUI BIO PAIN**, boulangerie artisanale bio située à Lormont (33). Cette solution professionnelle permet de gérer l'intégralité de l'activité commerciale : clients, produits, commandes, paiements, facturation et analyses.

## ✨ **FONCTIONNALITÉS PRINCIPALES**

### 🔐 **Authentification & Sécurité**
- Système de connexion sécurisé par rôles (Admin/Client)
- Sessions protégées avec hachage SHA-256
- Interface adaptée selon les permissions

### 🥖 **Gestion Produits Complète**
- **47 produits artisanaux bio** importés du catalogue réel
- Catégories : Pain Tradition, Campagne, 5 Graines, Seigle, Complet, Semi-Complet, Épeautre, Brioche
- Gestion des stocks avec alertes automatiques
- Prix réels de la boulangerie

### 👥 **Gestion Clients B2B**
- **18 clients professionnels** importés (Biocoop, Naturalia, AMAP, écoles...)
- Gestion des entreprises avec SIREN/TVA
- Historique des commandes par client
- Analyse du chiffre d'affaires par client

### 🛒 **Workflow Commandes Avancé**
- Cycle de vie complet : En attente → Confirmée → En préparation → Prête → Livrée → Payée
- Numérotation automatique des commandes
- Calculs automatiques des totaux
- Gestion des modifications et annulations

### 💰 **Module Financier Professionnel**
- **Enregistrement des paiements** (espèces, carte, chèque, virement)
- **Génération de factures PDF** avec en-tête SARL AQUI BIO PAIN
- Suivi des commandes impayées
- Statistiques financières temps réel

### 📊 **Exports & Business Intelligence**
- **Exports Excel formatés** (commandes, clients, produits)
- **Rapports PDF automatiques** (mensuel, ventes)
- **Analyses graphiques** (évolution CA, top produits)
- **Historiques détaillés** avec filtres avancés

### ⚙️ **Administration Système**
- **Logs d'activité** complets avec filtres
- **Sauvegarde/Restauration** de la base de données
- **Gestion des utilisateurs** (création, modification, rôles)
- **Paramètres configurables** de l'entreprise

## 🚀 **INSTALLATION & LANCEMENT**

### Prérequis
```bash
# Python 3.8+
# Environnement conda/miniconda recommandé
```

### Installation
```bash
# 1. Cloner ou télécharger le projet
cd boulangerie_app

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Importer les données réelles (optionnel)
python import_excel_data.py

# 4. Lancer l'application
streamlit run streamlit_app.py
```

### Accès
- **URL :** http://localhost:8501
- **Admin :** admin@aquibiopain.com / admin123
- **Clients :** Comptes créés pour chaque client réel

## 🏢 **INFORMATIONS ENTREPRISE**

**SARL AQUI BIO PAIN**
- **Adresse :** Zone d'activité des docks maritimes, Quai Carriet, 33310 LORMONT
- **SIREN :** 490 057 155 RCS Bordeaux
- **TVA :** FR 95490057155
- **Certification :** Ecocert FR-BIO-1
- **Activité :** Boulangerie artisanale bio

## 📋 **DONNÉES IMPORTÉES**

### Clients B2B (18)
- Delice Bio, Merci la Terre, SIO BIO (Le Haillan, Pessac)
- Biocoop (Latresne, Bouliac, Argonne)
- Naturalia (Le Bouscat, St Christoly)
- AMAP (La Bastide, Caudéran)
- Écoles (Bègles, Sainte Eulalie)
- Et autres partenaires...

### Produits Artisanaux (47)
- **Pain Tradition** : Boules, baguettes, pains 400g...
- **Pain de Campagne** : Tourtes, batards, boules...
- **Pain 5 Graines** : Baguettes, batards, moulés...
- **Pain de Seigle** : Moulés, tourtes...
- **Pain Complet/Semi-Complet** : Tous formats
- **Épeautre & Petit Épeautre**
- **Brioches** artisanales

## 💻 **ARCHITECTURE TECHNIQUE**

### Stack Technologique
- **Frontend :** Streamlit (Python)
- **Backend :** SQLite (7 tables relationnelles)
- **PDF :** ReportLab
- **Excel :** OpenPyXL
- **Styling :** CSS personnalisé thème boulangerie

### Base de Données
```sql
Tables : users, entreprises, produits, commandes, 
         commande_items, paiements, logs_activite
```

### Sécurité
- Hachage des mots de passe SHA-256
- Sessions sécurisées
- Contrôle d'accès par rôles
- Logs d'audit complets

## 📈 **UTILISATION PROFESSIONNELLE**

Cette application est **prête pour la production** et permet de :

1. **Gérer quotidiennement** les commandes clients
2. **Suivre les stocks** et anticiper les ruptures
3. **Facturer automatiquement** avec documents PDF
4. **Analyser les performances** commerciales
5. **Exporter les données** pour la comptabilité
6. **Administrer le système** en toute sécurité

## 🔄 **ÉVOLUTIONS POSSIBLES**

- Interface mobile responsive
- Notifications push/email
- API REST pour intégrations
- Module de planification production
- Gestion multi-magasins
- Tableau de bord temps réel

## 📞 **SUPPORT**

Application développée sur mesure pour SARL AQUI BIO PAIN.
Interface intuitive conçue pour les équipes de boulangerie.

---

**🥖 SARL AQUI BIO PAIN - Solution complète de gestion boulangerie artisanale** 

*Lormont, Nouvelle-Aquitaine - Depuis 2025*

## 🎨 Thème

L'application conserve le thème "boulangerie" avec :
- Couleurs chaleureuses (bruns, beiges)
- Images de pain en arrière-plan
- Interface intuitive et professionnelle

## 🔒 Sécurité

- Mots de passe hashés (SHA-256)
- Sessions sécurisées avec Streamlit
- Base de données SQLite locale

## 📊 Base de données

Tables principales :
- `users` : Utilisateurs et administrateurs
- `entreprises` : Informations des entreprises clientes
- `produits` : Catalogue des produits
- `commandes` : Commandes clients
- `commande_items` : Détails des commandes

## 🔧 Personnalisation

- Modifiez les couleurs dans `.streamlit/config.toml`
- Adaptez les styles CSS dans la fonction `load_css()`
- Ajoutez de nouvelles pages dans `streamlit_app.py`

## 📱 Déploiement

Pour déployer en production, utilisez :
- Streamlit Cloud
- Heroku
- Docker + serveur web

## 📝 Licence

Projet éducatif - Mission 2