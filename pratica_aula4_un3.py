import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df)#, estimator=sum, errorbar=None, hue='time', palette='Set2', legend=False)
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')
plt.show()