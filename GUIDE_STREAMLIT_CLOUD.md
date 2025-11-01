# 🚀 Guide Pas à Pas - Déploiement Streamlit Cloud

## 📋 **ÉTAPE 1 : Créer un compte GitHub**

1. **Aller sur GitHub :**
   - Ouvrir https://github.com dans votre navigateur
   - Cliquer sur "Sign up" (en haut à droite)

2. **Créer votre compte :**
   - Username : `aquibiopain` ou `sarl-aqui-bio-pain`
   - Email : Votre email professionnel
   - Mot de passe : Choisir un mot de passe fort
   - Vérifier votre email

3. **Créer un nouveau repository :**
   - Cliquer sur le bouton vert "New" ou "+"
   - Repository name : `boulangerie-aqui-bio-pain`
   - Description : `Application de gestion pour SARL AQUI BIO PAIN`
   - ✅ Public (gratuit)
   - ✅ Add a README file
   - Cliquer "Create repository"

---

## 📤 **ÉTAPE 2 : Uploader votre code**

### **Option A : Via l'interface web (Simple)**

1. **Dans votre repository GitHub :**
   - Cliquer "uploading an existing file"

2. **Sélectionner vos fichiers :**
   ```
   ✅ streamlit_app.py
   ✅ requirements.txt
   ✅ create_test_data.py
   ✅ import_excel_data.py
   ✅ .streamlit/config.toml
   ✅ .streamlit/secrets.toml
   ✅ static/ (dossier complet)
   ✅ .gitignore
   ✅ README.md
   ✅ Tous les fichiers .md
   
   ❌ NE PAS uploader :
   ❌ *.db (fichiers base de données)
   ❌ __pycache__/
   ❌ *.pyc
   ```

3. **Commit :**
   - Message : "Initial upload - SARL AQUI BIO PAIN app"
   - Cliquer "Commit changes"

### **Option B : Via Git (si vous connaissez)**

```bash
git clone https://github.com/votre-username/boulangerie-aqui-bio-pain.git
# Copier tous vos fichiers dans le dossier
git add .
git commit -m "Initial upload - SARL AQUI BIO PAIN app"
git push
```

---

## 🚀 **ÉTAPE 3 : Déployer sur Streamlit Cloud**

1. **Aller sur Streamlit Cloud :**
   - Ouvrir https://share.streamlit.io
   - Cliquer "Continue with GitHub"
   - Autoriser l'accès à votre compte GitHub

2. **Créer une nouvelle app :**
   - Cliquer "New app"
   - Repository : Sélectionner `boulangerie-aqui-bio-pain`
   - Branch : `main`
   - Main file path : `streamlit_app.py`
   - App URL : Laisser par défaut ou personnaliser

3. **Configurer les secrets (IMPORTANT) :**
   - Cliquer "Advanced settings"
   - Dans "Secrets", copier le contenu de votre fichier `.streamlit/secrets.toml`
   - Modifier les valeurs sensibles :

```toml
[email]
smtp_email = "votre.email@gmail.com"
smtp_password = "votre_mot_de_passe_application_gmail"

[admin]
default_password = "VotreMotDePasseSecurise2025!"
```

4. **Déployer :**
   - Cliquer "Deploy!"
   - Attendre 2-3 minutes...

---

## ✅ **ÉTAPE 4 : Configuration finale**

1. **Accéder à votre app :**
   - URL fournie par Streamlit Cloud
   - Exemple : `https://aquibiopain-boulangerie-aqui-bio-pain-streamlit-app-abc123.streamlit.app`

2. **Première connexion :**
   - Aller sur votre URL
   - Tester la page publique
   - Se connecter avec : `admin@aquibiopain.com` / votre mot de passe

3. **Initialiser les données :**
   - Si la base est vide, utiliser l'admin pour importer les données
   - Ou modifier le code pour auto-créer les données de test

---

## 🔧 **ÉTAPE 5 : Personnalisation**

1. **Domaine personnalisé (optionnel) :**
   - Dans Streamlit Cloud → Settings
   - Custom domain : `app.aquibiopain.com`

2. **Configuration email :**
   - Créer un mot de passe d'application Gmail
   - Mettre à jour les secrets Streamlit

---

## 🎉 **RÉSULTAT FINAL**

Votre application sera disponible 24h/24 sur internet !

**URL d'exemple :** 
`https://boulangerie-aqui-bio-pain-abc123.streamlit.app`

**Fonctionnalités actives :**
- ✅ Page publique e-commerce
- ✅ Gestion des commandes
- ✅ Administration complète
- ✅ Exports PDF/Excel
- ✅ Notifications email
- ✅ Interface mobile

---

## 🆘 **Aide en cas de problème**

### Erreurs courantes :

1. **"Module not found" :**
   - Vérifier `requirements.txt`
   - Ajouter les modules manquants

2. **"Database not found" :**
   - L'app crée automatiquement la DB
   - Vérifier les secrets de configuration

3. **"Email error" :**
   - Configurer les secrets email
   - Utiliser un mot de passe d'application Gmail

### Support :
- Documentation : https://docs.streamlit.io
- Community : https://discuss.streamlit.io

---

## 🎯 **CHECKLIST FINALE**

- [ ] Compte GitHub créé
- [ ] Repository créé avec le bon nom
- [ ] Fichiers uploadés (sans .db)
- [ ] Streamlit Cloud connecté
- [ ] App déployée avec succès
- [ ] Secrets configurés
- [ ] Tests de l'application OK
- [ ] Email configuré
- [ ] Données importées

**🚀 Votre boulangerie est maintenant en ligne !**