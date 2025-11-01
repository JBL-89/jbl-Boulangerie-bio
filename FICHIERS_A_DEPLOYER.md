# 📁 LISTE EXACTE DES FICHIERS À TÉLÉCHARGER POUR LE DÉPLOIEMENT

## 🎯 **FICHIERS OBLIGATOIRES (6 fichiers minimum)**

### ✅ **À la racine du projet :**
```
1. streamlit_app.py          ← Application principale
2. requirements.txt          ← Dépendances Python  
3. README.md                 ← Description du projet
```

### ✅ **Dossier .streamlit/ :**
```
4. .streamlit/config.toml    ← Configuration Streamlit
5. .streamlit/secrets.toml   ← Paramètres secrets
```

### ✅ **Dossier static/ complet :**
```
6. static/images/            ← Toutes les images produits
   ├── pain1.avif
   ├── pain2.avif  
   ├── pain3.avif
   ├── compagne.webp
   ├── complet.jpg
   ├── croi.webp
   ├── tradi.jpg
   └── choco.jpg
```

---

## 📋 **FICHIERS OPTIONNELS (mais recommandés)**

```
7. create_test_data.py       ← Pour créer les données de test
8. import_excel_data.py      ← Pour importer vos données Excel
9. .gitignore               ← Fichiers à ignorer
```

---

## 🚫 **FICHIERS À NE PAS TÉLÉCHARGER**

```
❌ *.db                     ← Base de données (sera recréée automatiquement)
❌ __pycache__/             ← Cache Python
❌ venv/                    ← Environnement virtuel
❌ *.pyc                    ← Fichiers compilés Python
❌ *.log                    ← Fichiers de log
❌ Dockerfile               ← Pas nécessaire pour Streamlit Cloud
❌ docker-compose.yml       ← Pas nécessaire pour Streamlit Cloud
❌ deploy.bat               ← Script Windows local
❌ deploy.sh                ← Script Linux local
```

---

## 📁 **STRUCTURE FINALE SUR GITHUB**

Votre repository GitHub doit ressembler à ça :

```
boulangerie-aqui-bio-pain/
├── streamlit_app.py
├── requirements.txt  
├── README.md
├── create_test_data.py
├── import_excel_data.py
├── .gitignore
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
└── static/
    └── images/
        ├── pain1.avif
        ├── pain2.avif
        ├── pain3.avif
        ├── compagne.webp
        ├── complet.jpg
        ├── croi.webp
        ├── tradi.jpg
        └── choco.jpg
```

---

## 🎯 **MÉTHODE SIMPLE : TOUT SÉLECTIONNER SAUF...**

**Plus simple :** Sélectionnez TOUS vos fichiers SAUF :
- ❌ Le fichier `boulangerie_streamlit.db`
- ❌ Le dossier `__pycache__` (s'il existe)
- ❌ Le dossier `venv` (s'il existe)

**Le reste, prenez tout !** 📦

---

## 📏 **TAILLE APPROXIMATIVE**

- **Fichiers code :** ~200 KB
- **Images :** ~2-5 MB  
- **Total :** Moins de 10 MB

**Parfait pour GitHub gratuit !** ✅

---

## 🚀 **ÉTAPES SIMPLIFIÉES**

1. **Ouvrir votre dossier projet**
2. **Sélectionner tout SAUF *.db et __pycache__**
3. **Faire glisser sur GitHub**
4. **Déployer sur Streamlit Cloud**

**C'est tout !** 🎉