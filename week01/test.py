import matplotlib.pyplot as plt
import seaborn as sns
import pandas

df = pandas.read_csv('Housing.csv')
cleaned_df = df.drop_duplicates()
cleaned_df = cleaned_df.dropna()

obj_col = cleaned_df.select_dtypes(include=['object']).columns

for col in obj_col:
    cleaned_df[col] = cleaned_df[col].astype('category')

cleaned_df[obj_col] = cleaned_df[obj_col].apply(lambda x: x.cat.codes)
cleaned_df = pandas.get_dummies(cleaned_df, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'], dtype=int)
cleaned_df.to_csv("Housing_with_new_feature.csv", index=False)