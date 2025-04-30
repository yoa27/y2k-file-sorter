# Y2K File Sorter 🗄️

Un trieur de fichiers moderne avec une interface graphique inspirée du style Y2K (bug de l'an 2000). Cette application permet d'organiser automatiquement vos fichiers par catégories selon leurs extensions.



## 🌟 Fonctionnalités

- Interface graphique moderne avec thème Y2K
- Tri automatique des fichiers par catégories
- Support des formats les plus courants :
  - Images et Vidéos (.jpg, .jpeg, .png, .gif, .mp4, .avi, .mov)
  - Images spéciales (.bmp, .tiff, .svg)
  - Documents PDF (.pdf)
  - Documents texte (.doc, .docx, .txt)
- Log en temps réel des opérations
- Gestion des erreurs avec messages explicites

## 📋 Prérequis

- Python 3.8 ou supérieur
- Bibliothèques requises :
  - tkinter (inclus avec Python)
  - Pillow (PIL)

## 🚀 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/y2k-file-sorter.git
cd y2k-file-sorter
```

2. Installez les dépendances :
```bash
pip install Pillow
```

3. Lancez l'application :
```bash
python renommage_gui.py
```

## 📁 Structure des dossiers

```
y2k-file-sorter/
│
├── renommage_gui.py     # Programme principal
├── assets/             # Ressources graphiques
│   ├── icon.ico        # Icône de l'application
│   └── logo.png        # Logo de l'interface
│
└── README.md           # Documentation
```

## 🎯 Utilisation

1. Lancez l'application
2. Cliquez sur "Parcourir" pour sélectionner le dossier à trier
3. Vérifiez les catégories de tri dans l'interface
4. Cliquez sur "Lancer le tri"
5. Suivez la progression dans la zone de log

## 🗂️ Catégories de tri

- **Images_Video** : .jpg, .jpeg, .png, .gif, .mp4, .avi, .mov
- **Images** : .bmp, .tiff, .svg
- **PDF** : .pdf
- **Docs** : .doc, .docx, .txt
- **Autres** : Tous les autres types de fichiers

## 🛠️ Personnalisation

Vous pouvez modifier les catégories de tri en éditant le dictionnaire `categories` dans le fichier `renommage_gui.py`.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request


## ✨ Crédits

- Interface inspirée du bug de l'an 2000 (Y2K)
- Développé avec ❤️ par [yoa27]

## 📧 Contact

- GitHub : [@yoa27](https://github.com/yoa27)


