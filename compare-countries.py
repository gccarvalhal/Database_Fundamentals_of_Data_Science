import pandas as pd

DATA_FOLDER = "../1 Download Files"

df_list = []
for i in range(2015, 2020):

    df = pd.read_csv(DATA_FOLDER + f'/{i}.csv')

    if i in [2015, 2016]:
        columns_list = ['Country','Happiness Score']
    elif i == 2017:
        columns_list = ['Country','Happiness.Score']
    else:
        columns_list = ['Country or region','Score']

    df = df[columns_list]
    df.columns = ['Country', 'Score']
    df['year'] = i
    df_list.append(df)

dataset = pd.concat(df_list)
# print(dataset.head())

countries = pd.read_csv(DATA_FOLDER + "/countries of the world.csv")
world_country_list = countries['Country'].str.strip().unique()


countries_to_correct = []
for c in dataset['Country'].sort_values().unique():
    if c not in world_country_list:
        countries_to_correct.append(c)

print("List of countries to correct/delete:", countries_to_correct)
