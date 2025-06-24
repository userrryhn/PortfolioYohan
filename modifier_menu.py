
import os

# Nouveau bloc HTML pour remplacer l'ancien menu Présentation
new_presentation_block = """
<div class="dropdown">
    <button class="dropbtn">Présentation</button>
    <div class="dropdown-content">
        <a href="index.html">Présentation générale</a>
        <a href="apprenti.html">Apprenti</a>
        <a href="entreprise.html">Entreprise</a>
    </div>
</div>
"""

# Marqueurs pour trouver l'ancien bloc
start_marker = '<div class="presentation-dropdown">'
end_marker = '</div>'

# Parcourir tous les fichiers HTML du dossier
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Trouver et remplacer le bloc ancien
        if start_marker in content:
            start_index = content.find(start_marker)
            end_index = content.find(end_marker, start_index) + len(end_marker)
            old_block = content[start_index:end_index]
            content = content.replace(old_block, new_presentation_block)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Menu mis à jour dans : {filename}")
        else:
            print(f"ℹ️ Aucun menu 'Présentation' trouvé dans : {filename}")
