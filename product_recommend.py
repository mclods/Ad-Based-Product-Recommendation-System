import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def product_recommendation(list_index=[]):
    if len(list_index) == 0:
        list_index.append(str(random.randrange(0, 1302, 1)))

    df = pd.read_csv(r'static\dataset\prod_list.csv')

    # print(type(df.iloc[1].product))

    def combine_features(row):
        s = str(row[1])
        for i in range(2, len(row)):
            s1 = str(row[i])
            s = s + ' ' + s1
            # s=u' '.join((s, str(row[i]).encode('utf-8')))
        return s

    df['combined_features'] = df.apply(combine_features, axis=1)
    # print(df.iloc[0].combined_features)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])

    sim_matrix = cosine_similarity(count_matrix)

    similar_products = []
    for x in list_index:
        product_index = int(x)
        sim = list(enumerate(sim_matrix[product_index]))
        similar_products.extend(sim)

    similar_products = list(set(similar_products))

    sorted_similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)[1:]
    # print(sorted_similar_products)

    i = 0
    product_list = []
    temp_list = []

    # print("\nTop Recommendations: \n")
    for element in sorted_similar_products:

        s1 = list(df.iloc[element[0]])
        if (s1[1] not in temp_list):
            l = {}
            l['index'] = s1[0]
            l['product'] = s1[1]
            l['price'] = s1[2]
            product_list.append(l)
            temp_list.append(s1[1])
            i = i + 1

        if i > 4:
            break

    # print(sim_matrix)
    # print(product_list)
    return product_list

# k=(product_recommendation(["17"]))
# print(k)