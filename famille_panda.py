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

def main():
    print(famille_panda_numpy)
    print(famille_panda_numpy[2,0]) # papa
    print(famille_panda_numpy[:,0]) # tous
    print()
    print(famille_panda_df) #DataFrame

main()