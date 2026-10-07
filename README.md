# 2048 Game by Nico

Ma version du célèbre jeu de réflexion **2048**, codée en **Python** avec **Pygame**.

> 🧠 **Projet réalisé entièrement à la main, sans aucune IA générative.**
> Il date de 2020 : c'est l'un de mes premiers projets de programmation. Le code est publié tel quel, dans son état d'origine.

![Visuel du jeu](visuel%20du%20jeu.png)

---

## 🎯 Principe du jeu

Le plateau est une grille de **4 × 4** cases. À chaque coup, toutes les tuiles glissent dans la direction choisie :

- deux tuiles de même valeur qui se rencontrent **fusionnent** en une seule tuile de valeur double (2 + 2 → 4, 4 + 4 → 8, …) ;
- chaque fusion ajoute la valeur de la nouvelle tuile au **score** ;
- après chaque coup valide, une nouvelle tuile (**2** ou, plus rarement, **4**) apparaît sur une case vide.

Le but : atteindre la tuile **2048** ! On peut ensuite continuer à jouer pour faire grimper le score.
La partie est perdue lorsque la grille est pleine et qu'aucune fusion n'est plus possible.

## 🎮 Commandes

| Action | Contrôle |
|---|---|
| Lancer une partie | Clic sur le bouton **Jouer** |
| Déplacer les tuiles | Flèches du clavier ⬆️ ⬇️ ⬅️ ➡️ |
| Recommencer après une défaite | Clic sur le bouton **Rejouer** |
| Quitter (et sauvegarder le meilleur score) | Fermer la fenêtre |

## ✨ Fonctionnalités

- Grille 4 × 4 avec gestion complète des déplacements et des fusions dans les quatre directions (une tuile ne peut fusionner qu'une seule fois par coup).
- **Score** en temps réel et **meilleur score** affiché à l'écran.
- **Sauvegarde du meilleur score** dans le fichier `Best score.txt` (à la fin d'une partie ou à la fermeture du jeu), avec le message *« Best score battu ! »* lorsqu'il est dépassé.
- **Couleurs des tuiles générées par un algorithme** : la couleur de chaque tuile est calculée à partir de sa valeur, en faisant varier progressivement les composantes RVB à chaque puissance de 2.
- Taille de police adaptée automatiquement au nombre de chiffres de la tuile (jusqu'à 5 chiffres).
- Message **« Gagné ! »** lorsque la tuile 2048 est atteinte.
- Détection de fin de partie, écran **GAME OVER** semi-transparent et bouton **Rejouer**.
- Icône de fenêtre personnalisée.

## 📁 Contenu du dépôt

| Fichier | Description |
|---|---|
| `2048_Game_by_Nico.py` | Code source complet du jeu |
| `2048_Game_by_Nico.exe` | Version exécutable Windows (aucune installation de Python requise) |
| `2048.png` | Icône de la fenêtre du jeu |
| `2048P.png` | Logo affiché sur l'écran principal |
| `2048 (1).ico` | Icône de l'exécutable |
| `Best score.txt` | Fichier de sauvegarde du meilleur score |
| `visuel du jeu.png` | Capture d'écran du jeu |

## 🚀 Lancer le jeu

### Option 1 — Exécutable Windows

Double-cliquer sur `2048_Game_by_Nico.exe`.
Les images (`2048.png`, `2048P.png`) doivent se trouver dans le même dossier que l'exécutable.

### Option 2 — Depuis le code source

**Prérequis :** Python 3 et la bibliothèque Pygame.

```bash
pip install pygame
```

Puis, **depuis le dossier du projet** (les images et le fichier de score sont chargés avec des chemins relatifs) :

```bash
python 2048_Game_by_Nico.py
```

> ℹ️ Le jeu utilise la police système **Cambria** (présente par défaut sous Windows). Sur un autre système, Pygame utilisera une police de remplacement.

## 🛠️ Technologies

- **Python 3**
- **Pygame** — affichage, gestion des événements clavier / souris et rendu du texte
- Modules standards `random` et `os`

## 👤 Auteur

**Nicolas Brault** (Nico) — projet personnel réalisé en 2020, sans IA générative.
