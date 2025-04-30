import os
import shutil

# 📁 Ton dossier à organiser
dossier = "C:/Users/jokr/Pictures/"

# 📂 Dictionnaire de tri par extension
categories = {
    "Images_Video": [".jpg", ".jpeg", ".png", ".gif", ".mp4", ".avi", ".mov"],
    "Images": [".bmp", ".tiff", ".svg"],
    "PDF": [".pdf"],
    "Docs": [".doc", ".docx", ".txt"],
}

# 🔁 Parcourt tous les fichiers
for fichier in os.listdir(dossier):
    chemin_complet = os.path.join(dossier, fichier)
    
    if os.path.isfile(chemin_complet):
        try:
            extension = os.path.splitext(fichier)[1].lower()

            # ➕ Détermine la catégorie
            categorie = "Autres"
            for nom_cat, extensions in categories.items():
                if extension in extensions:
                    categorie = nom_cat
                    break

            # 📁 Crée le sous-dossier si besoin
            dossier_categorie = os.path.join(dossier, categorie)
            os.makedirs(dossier_categorie, exist_ok=True)

            # 🔄 Déplace uniquement (sans renommer)
            nouveau_chemin = os.path.join(dossier_categorie, fichier)
            shutil.move(chemin_complet, nouveau_chemin)

            print(f"{fichier} → {categorie}/{fichier}")
        except Exception as e:
            print(f"Erreur lors du traitement de {fichier}: {str(e)}")

print("✅ Tous les fichiers ont été triés.")
