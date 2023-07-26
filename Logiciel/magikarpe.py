import tkinter as tk

def display_python_info():
    python_info = """
Python est un langage de programmation puissant, polyvalent et facile à apprendre. 
Il est largement utilisé dans le développement web, l'intelligence artificielle, l'analyse de données, l'automatisation, 
et bien plus encore. Grâce à sa syntaxe claire et élégante, Python permet d'écrire du code lisible et maintenable.

L'interpréteur Python et sa vaste bibliothèque standard sont disponibles gratuitement pour toutes les principales plateformes. 
Vous pouvez télécharger Python à partir du site officiel : https://www.python.org/downloads/

Python est idéal pour les débutants en programmation grâce à sa simplicité et à sa facilité d'utilisation. 
Cependant, il est également utilisé par de nombreuses grandes entreprises et organisations pour développer des applications et 
des projets complexes.

Python prend en charge la programmation orientée objet, fonctionnelle et impérative. 
Il dispose de nombreuses bibliothèques tierces qui facilitent le développement de divers types d'applications.

Enfin, Python est largement utilisé dans le domaine de l'apprentissage automatique et de l'intelligence artificielle, 
avec des bibliothèques populaires telles que TensorFlow, PyTorch et Scikit-learn.
    """
    info_window = tk.Toplevel(root)
    info_window.title("Python")

    label = tk.Label(info_window, text=python_info, font=("Helvetica", 12), justify="left", padx=20, pady=20)
    label.pack()

def display_code_to_complete():
    code_to_complete = """
Complétez le code ci-dessous pour afficher 'Bonjour, Python !'

message = '...., '
langage = '....'
print(...... + .....)

Complétez le code ci-dessous pour afficher la somme de deux nombres entiers

def addition(a, b):
     Votre code ici
    return sum
    """
    code_window = tk.Toplevel(root)
    code_window.title("Code à compléter (Python)")

    code_text = tk.Text(code_window, font=("Courier", 12), padx=20, pady=20)
    code_text.insert("1.0", code_to_complete)
    code_text.pack()

    def save_code():
        completed_code = code_text.get("1.0", "end-1c")
        with open("completed_code.py", "w") as file:
            file.write(completed_code)
        code_window.destroy()

    save_button = tk.Button(code_window, text="Sauvegarder", command=save_code, font=("Helvetica", 12))
    save_button.pack()


root = tk.Tk()
root.title("Mon Logiciel")


button_python = tk.Button(root, text="Python", command=display_python_info, font=("Helvetica", 16))
button_python.pack(side="top", padx=10, pady=10)

button_code_to_complete = tk.Button(root, text="Code à compléter (Python)", command=display_code_to_complete, font=("Helvetica", 16))
button_code_to_complete.pack(side="top", padx=10, pady=10)


def display_python_info():
    python_info = """
Ruby est un langage de programmation interprété, orienté objet et axé sur la simplicité et la productivité. 
Il a été créé dans les années 1990 par Yukihiro Matsumoto, plus connu sous le nom de "Matz". Ruby est conçu 
pour être agréable à lire et à écrire, avec une syntaxe élégante et expressive qui favorise la lisibilité du code.

Les principales caractéristiques de Ruby comprennent :

    Programmation orientée objet : Tout en Ruby est un objet, 
    y compris les nombres, les chaînes, les tableaux et les fonctions. Le langage encourage 
    la programmation orientée objet en fournissant des mécanismes tels que les classes, les objets et l'héritage.

    Typage dynamique : Ruby est un langage à typage dynamique, ce qui signifie que les types des variables sont déterminés 
    à l'exécution et peuvent changer pendant l'exécution du programme.

    Méta-programmation : Ruby est souvent appelé "langage de programmation de programmation" 
    en raison de ses puissantes capacités de méta-programmation. Il permet de créer des classes et des méthodes à la volée, 
    de modifier le comportement d'objets existants et de créer des DSL (Domain Specific Languages).

    Bibliothèque standard riche : Ruby est livré avec une vaste bibliothèque standard qui offre une large gamme de fonctionnalités, 
    y compris la manipulation de fichiers, les opérations réseau, la gestion de threads, la génération de code HTML et bien plus encore.

Ruby est utilisé dans de nombreux domaines, notamment le développement web, la création d'applications d'entreprise, 
l'automatisation de tâches, la création de jeux et le développement d'outils système. Il est également largement utilisé 
dans le développement web grâce à des frameworks populaires tels que Ruby on Rails, qui permettent de créer rapidement des 
applications web puissantes et évolutives.

Vous pouvez télécharger Ruby à partir du site officiel : https://www.ruby-lang.org/en/downloads/
    """
    info_window = tk.Toplevel(root)
    info_window.title("Python")

    label = tk.Label(info_window, text=python_info, font=("Helvetica", 12), justify="left", padx=20, pady=20)
    label.pack()





button_python = tk.Button(root, text="Ruby", command=display_python_info, font=("Helvetica", 16))
button_python.pack(side="top", padx=10, pady=10)

def display_code_to_complete():
    code_to_complete = """
afficher un message de bienvenue'

........ "Bienvenue dans le monde de Ruby!"

Déclaration d'une variable et affichage

nom = "Alice"
puts "....., .{...}."

Utilisation d'une boucle pour afficher des nombres de 1 à 5
(_.._).____ do |.|
  ___ i
___


    """
    code_window = tk.Toplevel(root)
    code_window.title("Code à compléter (Ruby)")

    code_text = tk.Text(code_window, font=("Courier", 12), padx=20, pady=20)
    code_text.insert("1.0", code_to_complete)
    code_text.pack()

    def save_code():
        completed_code = code_text.get("1.0", "end-1c")
        with open("completed_code.py", "w") as file:
            file.write(completed_code)
        code_window.destroy()

    save_button = tk.Button(code_window, text="Sauvegarder", command=save_code, font=("Helvetica", 12))
    save_button.pack()



















button_code_to_complete = tk.Button(root, text="Code à compléter (Ruby)", command=display_code_to_complete, font=("Helvetica", 16))
button_code_to_complete.pack(side="top", padx=10, pady=10)








root.mainloop()

