brief_26_journee-integration

Ce repository contient des fichier .yml qui permet de créer des pipelines sur github et gitlab.

Les pipelines ont deux étapes :
 - une étape de lint avec la librairie flake8 qui permet de voir si le code est écrit correctement, le lint est configuré pour ne pas tester les fichiers dans le dossier crypto_app pour juste regarder les erreurs d'écriture dans les fichiers de tests.
 - une étape de test avec la librairie pytest qui permet de lancer les tests sur différents algorythmes

L'étape de lint sur github ne donne pas d'erreur sur la pipeline si il y a des erreurs d'écriture, il liste juste toutes les ces dans la pipeleine. 
L'étape de lint sur gitlab donne une erreur sur la pipeline lorsqu'il y a des erreurs d'écriture.
Grâce à l'ajout de 'allow_failure: true' dans le fichier .yml, lorsqu'il y a des erreur d'écriture dans le code la pipeleine aurat le statut passed avec warning.

Prochaines étapes : 
J'ai modifié le code du .yml pour gitlab afin de générer un rapport des erreurs d'écritures. 
Je n'ai pas pu tester ce changement car les pipelines gitlab ne se lancent plus au moment où j'ai voulu le faire.
J'ai commancé à modifier le .yml pour github aussi pour de générer un rapport des erreurs d'écritures. 
Je n'ai pas le temps de finaliser les tests afin vérifier et de récupérer ce fichier texte. 


