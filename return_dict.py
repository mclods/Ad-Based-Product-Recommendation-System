import pandas as pd

def return_data(index):
    df = pd.read_csv(r'static/dataset/data.csv', encoding='latin-1')
    # print(df.head())
    d = []
    for e in index:
        i = int(e)
        x = df.iloc[i]
        l = {}
        l['index'] = x.id
        l['company'] = x.Company
        l['product'] = x.Product
        l['type'] = x.TypeName
        l['screen_size'] = x.Inches
        l['resolution'] = x.ScreenResolution
        l['cpu'] = x.Cpu
        l['ram'] = x.Ram
        l['memory'] = x.Memory
        l['gpu'] = x.Gpu
        l['op'] = x.OpSys
        l['weight'] = x.Weight
        l['price'] = x.Price_euros
        d.append(l)
    return d


# k = return_data(["20", "34"])
# print(k)