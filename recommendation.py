import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def laptop_recommendation(ind, list_index=[]):
    df = pd.read_csv(r'static\dataset\data.csv', encoding='latin-1')
    df1 = pd.read_csv(r'static\dataset\data.csv', encoding='latin-1')

    if len(list_index) == 0:
        list_index.append(str(random.randrange(0, 1302, 1)))
        # print(list_index)

    # df = pd.read_csv('laptops - Copy.csv', encoding='latin-1')
    # df1 = pd.read_csv('laptops - Copy.csv', encoding='latin-1')

    # df.drop(df.columns[[0]],inplace=True,axis=1)
    # df1.drop(df1.columns[[0]],inplace=True,axis=1)

    # df.id = df.index
    # df1.id = df1.index

    # print(df.id)

    df.drop(['Company', 'Product'], inplace=True, axis=1)

    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    # print(df.head())
    # print(df.columns)
    # print(np.sum(df['TypeName']=='Gaming'))

    # df1 = pd.read_excel('Model Data.xlsx',sheet_name=None)

    def combine_features(row):
        s = str(row[1])
        for i in range(2, len(row)):
            s1 = str(row[i])
            s = s + ' ' + s1
            # s=u' '.join((s, str(row[i]).encode('utf-8')))

        return s

    df['combined_features'] = df.apply(combine_features, axis=1)
    df1['combined_features'] = df1.apply(combine_features, axis=1)
    # print(df.iloc[0].combined_features)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])

    sim_matrix = cosine_similarity(count_matrix)

    similar_laptops = []
    for x in list_index:
        laptop_index = int(x)
        sim = list(enumerate(sim_matrix[laptop_index]))
        similar_laptops.extend(sim)

    similar_laptops = list(set(similar_laptops))
    # print(similar_laptops)

    # similar_laptops = list(similar_laptops)

    # laptop_index = int(sys.argv[1])
    # laptop_index = int(ind)
    # print(df[df.id == laptop_index].index)
    # print('laptop selected')
    # print(df1.iloc[laptop_index].combined_features)

    # similar_laptops = list(enumerate(sim_matrix[laptop_index]))
    # print(similar_laptops)

    sorted_similar_laptops = sorted(similar_laptops, key=lambda x: x[1], reverse=True)[1:]
    # print(sorted_similar_laptops)

    i = 0
    laptop_list = []

    # print("\nTop Recommendations: \n")
    for element in sorted_similar_laptops:

        if df1.iloc[element[0]].Company == "Dell":
            print(f"{i + 1}:{df1.iloc[element[0]].combined_features}\nMatching percentage:{element[1] * 100}%\n")
            # laptop_list.append(df1.iloc[element[0]].combined_features)
            l = {}
            l['index'] = df1.iloc[element[0]].id
            l['company'] = df1.iloc[element[0]].Company
            l['product'] = df1.iloc[element[0]].Product
            l['type'] = df1.iloc[element[0]].TypeName
            l['screen_size'] = df1.iloc[element[0]].Inches
            l['resolution'] = df1.iloc[element[0]].ScreenResolution
            l['cpu'] = df1.iloc[element[0]].Cpu
            l['ram'] = df1.iloc[element[0]].Ram
            l['memory'] = df1.iloc[element[0]].Memory
            l['gpu'] = df1.iloc[element[0]].Gpu
            l['op'] = df1.iloc[element[0]].OpSys
            l['weight'] = df1.iloc[element[0]].Weight
            l['price'] = df1.iloc[element[0]].Price_euros
            laptop_list.append(l)
            i = i + 1

        if i > 9:
            break

    # print(sim_matrix)
    return laptop_list

# k=(laptop_recommendation("79",["2","7","9","1"]))
# k=(laptop_recommendation("79"))
# print(k)