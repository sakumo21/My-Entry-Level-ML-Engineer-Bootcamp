import pandas

df = pandas.read_csv('Housing.csv')
cleaned_df = df.drop_duplicates()
cleaned_df = cleaned_df.dropna()

columns = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]

for col in columns:
    print(f"Value Counts for {col}")
    print(cleaned_df[col].value_counts())
    print()
