Réalisé sur Python 3.7.4


Dans le fichier "BinPacking_XFit_start_to_code.py", nous avons codé 7 heuristiques de résolutions du BPP :
-	Next Fit
-	First Fit
-	Best Fit
-	Worst Fit
-	Almost Worst Fit
-	First Fit Decreasing
-	Best Fit Decreasing

Afin de tester ces heuristiques, nous utilisons 85 instances randomisés qui sont présentes dans le dossier "Random_tests" de notre archive.
Les solutions exactes de ces instances sont présentes dans le fichier "Solution_exactes.txt".
Nous manipulons ces fichiers avec le module OS de Python pour réaliser les tests et afficher les résultats.
Chaque colonne de la matrice affichée en résultat correspond à une heuristique, dans l'ordre qui est précisé dans le code.
Chaque ligne de la matrice correspond à une instance testée.
Nous affichons, dans cet ordre, la matrice des solutions (nombre de boites) puis la matrice des erreurs d'approximation (comme définie dans le code).
La fonction Main réalise ces tests avec affichage à l'exécution.
