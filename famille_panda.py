#! usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd

famille_panda = [
    [100, 5, 20, 80], # mère
    [50, 2.5, 10, 40], # enfant
    [100, 5, 20, 80], # papa
]

famille_panda_numpy = np.array(famille_panda) # manip série de données
famille_panda_df = pd.DataFrame(famille_panda_numpy,
                                index = ['maman', 'bebe', 'papa'],
                                columns = ['pattes', 'poil', 'queue', 'ventre']) # Pandas (manip DataFrame)
pandas_80 = famille_panda_df[famille_panda_df["ventre"] == 80] # masque pour filtrer les données


def main():
    print('##### Test numpy pandas #####')
    print(famille_panda_numpy)
    print(famille_panda_numpy[2,0]) # papa
    print(famille_panda_numpy[:,0]) # tous
    print('##### Tableau pandas #####')
    print(famille_panda_df) #DataFrame
    print('##### Accès colonne ventre #####')
    print(famille_panda_df.ventre)
    print('##### Itération avec iterrows #####')
    for ligne in famille_panda_df.iterrows():
        index_ligne = ligne[0]
        contenue_ligne = ligne[1]
        print("Voici le panda %s :" % index_ligne)
        print(contenue_ligne)
        print("------------------")
    print("##### Conditions et iloc/loc options")
    print(famille_panda_df.iloc[2]) # Avec iloc(), indexation positionnelle
    print(famille_panda_df.loc["papa"])
    print("------------------")
    print(famille_panda_df["ventre"] == 80)
    print(pandas_80)
    print(pandas_others)


main()