# Projet de gestion des [compétence](#compétence)s en microservice

## Présentation
Ce projet à pour but de créer une application complette pour gérer les [compétence](#compétence)s d'une equipe.
Une équipe est composé de personne. Chaque personne posséde un niveau de [compétence](#compétence)s entre 0 et 20.

## Thesaurus

vers le [Thesaurus](./Thesaurus.md)

## Les besoins
Une personne peut voir la liste de l'ensemble des compétences de ses équipe.
Une personne peut definir son niveau de compétence pour une compétence allant de 0 a 20.

Un administrateur peut créer une nouvelle compétence pour une équipe.
Un administrateur peut supprimer une nouvelle compétence pour une équipe.
Un administrateur peut modifier le nom et la description d'une compétence.
Un administrateur est lié a une équipe. Il peut modifier les compétences pour cette équipe.


## Les bounded contexts
* contexte personne: Contexte contenant la gestion des personnes.
* contexte compétences: Contexte contenant la gestion des compétences et leurs niveaux
* contexte équipe: Gestions des informations de l'équipe.

## Solution technique
Pour répondre à ses besoins, nous proposont la solution suivante:

### Le services
* services des compétences: gestion de la liste des compétences.
    * CRUD
* services des personnes et leurs niveaux de compétences: gestion des personnes et de leurs niveaux de compétences.
    * CRUD
* services des équipes: gestion des équipes.
    * CRUD
* services des utilisateurs: gestion des utilisateurs et de l'authentification.
    * Oauth2
    * CRUD
* service frontend
    * React