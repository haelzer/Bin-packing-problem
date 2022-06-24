import os
from os import listdir
from os.path import isfile, join
import numpy as np


def import_config(nom_fichier):
    fichier = open(nom_fichier, "r")
    l = fichier.readline()
    n = int(l)
    l = fichier.readline()
    c = int(l)
    weight=[]
    for i in range(n):
        l = fichier.readline()
        weight.append(int(l))
    fichier.close()
    return (n, c, weight)


# NextFit - Complexité en O(n)
def nextfit(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    res = 1
    rem = c
    for _ in range(n): # O(n)
        if rem >= weight[_]:
            rem = rem - weight[_]
        else:
            res += 1
            rem = c - weight[_]
    return res

# First Fit - Complexité en O(n^2)
def firstfit(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    indice_ouverture = -1
    rem = [c]*n
    for _ in range(n): # O(n^2)
        check,k=False,0
        while (not check) and (k<indice_ouverture) : # O(n)
            if rem[k] >= weight[_]:
                rem[k]-= weight[_]
                check=True
            else :
                k+=1
        if not check:
            indice_ouverture+=1
            rem[indice_ouverture]-=weight[_]
    return (indice_ouverture+1)

# Best Fit - Complexité en O(n^2)
def bestfit(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    rem = [c]*n
    indice_ouverture=-1
    for _ in range(n): # O(n^2)
        convenables=[] # Liste des boites convenables
        for k in range(indice_ouverture): # O(n)
            if rem[k] >= weight[_]:
                convenables.append(k)
        if convenables==[]: # O(1)
            indice_ouverture+=1
            rem[indice_ouverture]-= weight[_]
        else : # O(n)
            i_min,min_poids=convenables[0],rem[convenables[0]]
            for boite in convenables: # O(n)
                if rem[boite] < min_poids:
                    i_min,min_poids=boite,rem[boite]
            rem[i_min]-= weight[_]
    return (indice_ouverture+1)

# Worst Fit - Complexité en O(n^2)
def worstfit(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    rem = [c]*n
    indice_ouverture=-1
    for _ in range(n): # O(n)
        convenables=[] # Liste des boites convenables
        for k in range(indice_ouverture): # O(n)
            if rem[k] >= weight[_]:
                convenables.append(k)
        if convenables==[]: # O(1)
            indice_ouverture+=1
            rem[indice_ouverture]-= weight[_]
        else : # O(n)
            i_max,max_poids=convenables[0],rem[convenables[0]]
            for boite in convenables: # O(n)
                if rem[boite] > max_poids:
                    i_max,max_poids=boite,rem[boite]
            rem[i_max]-= weight[_]
    return (indice_ouverture+1)

# Almost Worst Fit - Complexité en O(n^2)
def almostworstfit(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    rem = [c]*n
    indice_ouverture=-1
    for _ in range(n): # O(n^2)
        convenables=[] # Liste des boites convenables
        for k in range(indice_ouverture): # O(n)
            if rem[k] >= weight[_]:
                convenables.append(k)
        p=len(convenables) # O(n)
        if p==0: # O(1)
            indice_ouverture+=1
            rem[indice_ouverture]-= weight[_]
        elif p==1: # O(n)
            i_max,max_poids=convenables[0],rem[convenables[0]]
            for boite in convenables: #O(n)
                if rem[boite] > max_poids:
                    i_max,max_poids=boite,rem[boite]
            rem[i_max]-= weight[_]
        else : # O(n)
            i_max,max_poids=convenables[0],rem[convenables[0]]
            i_max_second=convenables[1]
            if rem[i_max]>max_poids:
                i_max,i_max_second,max_poids=i_max_second,i_max,rem[i_max_second]
            for l in range(2,p): #O(n)
                if rem[convenables[l]] > max_poids:
                    i_max,max_poids,i_max_second=convenables[l],rem[convenables[l]],i_max
            rem[i_max_second]-= weight[_]
    return (indice_ouverture+1)

# First Fit Decreasing - Complexité en O(n^2)
def ffd(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    w=sorted(weight)[::-1] # O(n*log(n))
    indice_ouverture = -1
    rem = [c]*n
    for _ in range(n): # O(n^2)
        check,k=False,0
        while (not check) and (k<indice_ouverture) : # O(n)
            if rem[k] >= w[_]:
                rem[k]-= w[_]
                check=True
            else :
                k+=1
        if not check:
            indice_ouverture+=1
            rem[indice_ouverture]-=w[_]
    return (indice_ouverture+1)

# Best Fit Decreasing - Complexité en O(n^2)
def bfd(weight, c):
    n=len(weight) # O(n)
    if (n==0):
        return 0
    w=sorted(weight)[::-1] # O(n*log(n))
    rem = [c]*n
    indice_ouverture=-1
    for _ in range(n): # O(n^2)
        convenables=[]
        for k in range(indice_ouverture): # O(n)
            if rem[k] >= w[_]:
                convenables.append(k)
        if convenables==[]:
            indice_ouverture+=1
            rem[indice_ouverture]-= w[_]
        else :
            i_min,min_poids=convenables[0],rem[convenables[0]]
            for boite in convenables:
                if rem[boite] < min_poids:
                    i_min,min_poids=boite,rem[boite]
            rem[i_min]-= w[_]
    return (indice_ouverture+1)

def main():
    #weight = [2, 5, 4, 7, 1, 3, 8]
    #c = 10
    #c=11
    fichiers = [f for f in listdir("Random_tests") if isfile(join("Random_tests", f))]
    n=len(fichiers)
    solutions_approchées=np.zeros((n,7))
    solutions_exactes=np.loadtxt('Solutions_exactes.txt')[0:n]
    os.chdir(os.getcwd()+'/Random_tests')
    print(os.getcwd())
    for k in range(n) :
        elem=fichiers[k]
        print("\nFichier :"+elem)
        [_, c, weight] = import_config(elem)
        print("Our data == capacity :", c, "weights :", weight, "\n")
        solutions_approchées[k][0]=(nextfit(weight,c))
        solutions_approchées[k][1]=(firstfit(weight,c))
        solutions_approchées[k][2]=(bestfit(weight,c))
        solutions_approchées[k][3]=(worstfit(weight,c))
        solutions_approchées[k][4]=(almostworstfit(weight,c))
        solutions_approchées[k][5]=(ffd(weight,c))
        solutions_approchées[k][6]=(bfd(weight,c))
        print("Number of bins required in Next Fit :",nextfit(weight, c))
        print("Number of bins required in First Fit :",firstfit(weight, c))
        print("Number of bins required in Best Fit :",bestfit(weight, c))
        print("Number of bins required in Worst Fit :",worstfit(weight, c))
        print("Number of bins required in Almost Worst Fit :",almostworstfit(weight, c))
        print("Number of bins required in First Fit Decreasing :",ffd(weight, c))
        print("Number of bins required in Best Fit Decreasing :", bfd(weight, c))
    print("\n Voici le tableau des solutions approchées sur nos tests randomisés :")
    print(solutions_approchées)
    erreur_approx=solutions_approchées
    for k in range(n):
        for i in range(7):
            erreur_approx[k][i]-=solutions_exactes[k]
    print("\n Voici le tableau des erreurs d'approximation (nombre de boites en trop) de nos heuristiques sur nos tests randomisés: ")
    print(erreur_approx)
    print("\n Voici la moyenne d'erreur de nos méthodes d'approximations :")
    print("\n Next Fit : "+ str(np.average(abs(erreur_approx)[:,0])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n First Fit : "+ str(np.average(abs(erreur_approx)[:,1])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n Best Fit : "+ str(np.average(abs(erreur_approx)[:,2])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n Worst Fit : "+ str(np.average(abs(erreur_approx)[:,3])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n Almost Worst Fit : "+ str(np.average(abs(erreur_approx)[:,4])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n First Fit Decreasing : "+ str(np.average(abs(erreur_approx)[:,5])) + " erreurs en moyenne sur les 85 essais randomisés")
    print("\n Best Fit Decreasing : "+ str(np.average(abs(erreur_approx)[:,6])) + " erreurs en moyenne sur les 85 essais randomisés")
    
    
    
if __name__ == "__main__":
    main()