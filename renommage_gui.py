import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk # Assurez-vous d'avoir installé Pillow pour la gestion des images

class TriFichiersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Y2K File Sorter")
        self.root.geometry("600x500")
        
        # Configurer le redimensionnement
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Configuration du style
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'))
        self.style.configure('Category.TLabel', font=('Segoe UI', 10))
        self.style.configure('Action.TButton', font=('Segoe UI', 10), padding=10)
        
        # Définition des chemins des ressources
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        self.icon_path = os.path.join(self.assets_dir, "icon.ico")
        self.logo_path = os.path.join(self.assets_dir, "logo.png")
        
        # Ajout d'un thème plus moderne
        try:
            self.root.tk.call('source', 'azure.tcl')
            self.style.theme_use('azure')
            self.root.iconbitmap('icon.ico')  # Pour l'icône de la fenêtre
        
        except:
            # Fallback vers le thème par défaut
            self.style.theme_use('clam')
            print("Impossible de charger l'icône")
        
        # Variables
        self.dossier_path = tk.StringVar()
        
        # Dictionnaire de tri
        self.categories = {
            "Images_Video": [".jpg", ".jpeg", ".png", ".gif", ".mp4", ".avi", ".mov"],
            "Images": [".bmp", ".tiff", ".svg"],
            "PDF": [".pdf"],
            "Docs": [".doc", ".docx", ".txt"],
        }
        
        # Interface
        self.creer_interface()
    
    def creer_interface(self):
        # Frame principal avec padding et relief
        main_frame = ttk.Frame(self.root, padding="20", relief="ridge")
        main_frame.grid(row=0, column=0, sticky="nsew")  # nsew = North, South, East, West
        
        # Configurer le redimensionnement du main_frame
        main_frame.grid_rowconfigure(5, weight=1)  # Pour la zone de log
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        
        # Ajout du logo
        try:
            if os.path.exists(self.logo_path):
                # Chargez votre image
                logo = Image.open(self.logo_path)
                # Redimensionnez si nécessaire
                logo = logo.resize((64, 64), Image.LANCZOS)
                logo_tk = ImageTk.PhotoImage(logo)
                
                # Créez un label pour afficher le logo
                logo_label = ttk.Label(main_frame, image=logo_tk)
                logo_label.image = logo_tk
                logo_label.grid(row=0, column=0, pady=(0, 10))
                
                # Titre à côté du logo
                header = ttk.Label(main_frame, 
                                text="Y2K File Sorter\nNe laissez pas vos fichiers causer un bug de l'an 2000!", 
                                style='Header.TLabel',
                                justify='center')
                header.grid(row=0, column=1, columnspan=2, pady=(0, 20))
            else:
                raise FileNotFoundError("Logo non trouvé")
        except:
            # Fallback si pas de logo
            header = ttk.Label(main_frame, 
                              text="Y2K File Sorter\nNe laissez pas vos fichiers causer un bug de l'an 2000!", 
                              style='Header.TLabel',
                              justify='center')
            header.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Sélection du dossier avec style amélioré
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 20))
        
        ttk.Label(folder_frame, text="Dossier à trier:", style='Category.TLabel').grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(folder_frame, textvariable=self.dossier_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(folder_frame, text="Parcourir", style='Action.TButton', command=self.choisir_dossier).grid(row=0, column=2)
        
        # Liste des extensions avec style amélioré
        ttk.Label(main_frame, text="Catégories de tri:", style='Header.TLabel').grid(row=2, column=0, columnspan=3, pady=(0, 10), sticky=tk.W)
        
        categories_frame = ttk.Frame(main_frame)
        categories_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
        row = 0
        for categorie, extensions in self.categories.items():
            ttk.Label(categories_frame, text=f"{categorie}:", style='Category.TLabel').grid(row=row, column=0, sticky=tk.W, padx=(20,10))
            ttk.Label(categories_frame, text=", ".join(extensions), style='Category.TLabel').grid(row=row, column=1, sticky=tk.W)
            row += 1
        
        # Bouton de tri stylisé
        ttk.Button(main_frame, text="Lancer le tri", style='Action.TButton', command=self.trier_fichiers).grid(row=4, column=0, columnspan=3, pady=20)
        
        # Zone de log avec style amélioré
        self.log_text = tk.Text(main_frame, height=8, width=60, font=('Consolas', 9))
        self.log_text.grid(row=5, column=0, columnspan=3, pady=5, sticky="nsew")
        self.log_text.configure(bg='#f0f0f0', fg='#333333')
        
        # Scrollbar pour le log
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.log_text.yview)
        scrollbar.grid(row=5, column=3, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
    def choisir_dossier(self):
        dossier = filedialog.askdirectory()
        if dossier:
            self.dossier_path.set(dossier)
    
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def trier_fichiers(self):
        dossier = self.dossier_path.get()
        if not dossier:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier!")
            return
        
        try:
            for fichier in os.listdir(dossier):
                chemin_complet = os.path.join(dossier, fichier)
                
                if os.path.isfile(chemin_complet):
                    try:
                        extension = os.path.splitext(fichier)[1].lower()
                        
                        # Détermine la catégorie
                        categorie = "Autres"
                        for nom_cat, extensions in self.categories.items():
                            if extension in extensions:
                                categorie = nom_cat
                                break
                        
                        # Crée le sous-dossier
                        dossier_categorie = os.path.join(dossier, categorie)
                        os.makedirs(dossier_categorie, exist_ok=True)
                        
                        # Déplace le fichier
                        nouveau_chemin = os.path.join(dossier_categorie, fichier)
                        shutil.move(chemin_complet, nouveau_chemin)
                        
                        self.log(f"✅ {fichier} → {categorie}")
                    except Exception as e:
                        self.log(f"❌ Erreur avec {fichier}: {str(e)}")
            
            self.log("\n✨ Tri terminé avec succès!")
            messagebox.showinfo("Succès", "Le tri des fichiers est terminé!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {str(e)}")

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = TriFichiersApp(root)
    root.mainloop()