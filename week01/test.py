import matplotlib.pyplot as plt
import seaborn as sns
import pandas

df = pandas.read_csv('Housing.csv')
cleaned_df = df.drop_duplicates()
cleaned_df = cleaned_df.dropna()
columns = ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
columns2 = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]

#============>histogram plots<============

fig1, axs = plt.subplots(2, 3, figsize=(15, 8))
axs = axs.flatten()

for i, col in enumerate(columns):
	sns.histplot(df[col], bins=20, kde=True, ax=axs[i])
    
plt.tight_layout()
plt.savefig("plot.png") 
plt.close(fig1)

#============>boxplots<============

fig2, axs2 = plt.subplots(2, 3, figsize=(15, 8))
axs2 = axs2.flatten()

for i, col in enumerate(columns):
	sns.boxplot(data=df, x=col, ax=axs2[i])


plt.tight_layout()
plt.savefig("plot2.png") 
plt.close(fig2)

# #============>plot pie charts<============

fig3, axs3 = plt.subplots(3, 3, figsize=(15, 15))
axs3 = axs3.flatten()

for i, col in enumerate(columns2):
	counts = df[col].value_counts()
	axs3[i].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
	axs3[i].set_title(f'Pie Chart of {col.capitalize()}')

fig3.delaxes(axs3[7])
fig3.delaxes(axs3[8])
plt.tight_layout()
plt.savefig("plot3.png")
plt.close(fig3)
