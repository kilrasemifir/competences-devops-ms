### Equipe
Une equipe représente un ensemble de [personnes](#personne).

### Personne
Une personne représente un utilisateur ayant des [compétence](#compétence)s et appartenant à une ou plusieurs [équipes](#equipe).
Chaque eéquipe posséde une liste de compétences qui lui est propre.

### Compétence
Une [compétence](#compétence) représente une connaissance. Elle est représenté par un nom. Les personnes peuvent avoir un niveau de [compétence](#compétence) pour chaque [compétence](#compétence).
Exemple:
- Développer avec Python
- utiliser docker
- Flask
- Developpement en Java
- Kubernetess

### Niveau de compétence.
Un niveau de [compétence](#compétence) représente la connaissance d'une personne pour une [compétence](#compétence) donnée. Elle va de 0 a 20 avec les régles suivantes:
0. Inconnue
1. Connait de nom mais pas son but
2. Connait son but mais ne connait pas de cas d'utilisations
3. Connait son principe général vaguement.
4. Connait son principe général et son principe de fonctionnement mais ne l'a jamais vu en action
5. A deja vu comment utiliser la [compétence](#compétence) de maniere basique
6. Sait utiliser la [compétence](#compétence).
7. Connait la base de l'utilisation de la [compétence](#compétence) mais a besoin d'aide.
8. Connait les bases de la [compétence](#compétence).
9. Peut faire des
10. Autonomie pour les bases
11. Autonomie et connaissance sur les élements principaux de la [compétence](#compétence).
12. Connaissance général de la [compétence](#compétence).
13. Connaissance de la [compétence](#compétence) poussé.
14. Connaissance des élements avancé de la [compétence](#compétence).
15. Autonomie sur la [compétence](#compétence)
16. Expert sur la [compétence](#compétence). Connait tout ses conceptes.
17. Expert sur la [compétence](#compétence). Peut  l'utiliser a son plein potentiel.
18. Expert sur la [compétence](#compétence). La connait et peut appliquer l'ensemble des conseptes lié a elle.
19. Connait tout sur la [compétence](#compétence). Pourrait la recréer de A a Z
20. Créateur de la [compétence](#compétence)
Les personnes peuvent definir elles même en fonction de leurs recentis leurs niveau de compétence.

### Niveau de la personne
Le niveau de la personne correspond a la somme des niveaux de compétence d'une personne.

### Adminisatrateur
Un administrateur peut ajouter, supprimer ou modifier de nouvelles compétences.

### Propriétaire
Un propriétaire peut gérer l'ensemble des élements d'une équipe.