import geopandas as gpd

data = gpd.read_file('C:\Users\kalil\OneDrive\desktop\geop.shp')

print(data.head())
print(data.info())
print(data.isnull().sum())

data = data.drop(['coluna1', 'coluna2'], axis=1)
data['coluna_valores_ausentes'] = data['coluna_valores_ausentes'].fillna(data['coluna_valores_ausentes'].median())
data = data[data['região'] == 'região_de_interesse']
data['data_coluna'] = pd.to_datetime(data['data_coluna'])
data['coluna_num._normalizada'] = (data['coluna_num.'] - data['coluna_num.'].min()) / (data['coluna_num.'].max() - data['coluna_num.'].min())

data.to_file('C:\Users\kalil\OneDrive\desktop\MassDagpd.shp')
