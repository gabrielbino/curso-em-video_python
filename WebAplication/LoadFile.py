import pickle
import numpy as np

naive_bayes = pickle.load(open('naivebayes_finalizado.sav', 'rb'))

# Adult - 0, Senior - 1, Adolescent - 2
# Adventurous - 0, Cautious - 1, Psycopath - 2, Normal - 3
# Economy - 0, FamilySedan - 1, SportsCar - 2, Luxury - 3, SuperLuxury - 4

novo_registro = [[1, 1, 1]]
novo_registro = np.asarray(novo_registro)