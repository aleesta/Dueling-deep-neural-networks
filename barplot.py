import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Il tuo dataset
data = {
    'Oliveira': [31979, 102, 5444, 135, 1948, None, 220, 404, 118, 216, None],
    'VirusShare': [8919, 2490, 908, 510, 218, 524, 165, 115, None, None, None],
    'Catak': [1001, 1001, 379, 1001, 1001, 1001, None, None, 891, None, 832],
    'VirusSample': [6153, 2367, 222, 447, None, 441, 102, None, None, None, None]
}

index = ["Trojan", "Virus", "Adware", "Backdoor", "Downloader", "Worms", "Agent", "Ransomware", "Dropper", "Riskware", "Spyware"]

df = pd.DataFrame(data, index=index)

# Trasforma il DataFrame per il bar plot
df_melted = df.reset_index().melt('index')

# Creazione del bar plot
plt.figure(figsize=(10,6))
bar_plot = sns.barplot(x='index', y='value', hue='variable', data=df_melted)
plt.title('')
plt.xlabel('Malware Family')
plt.ylabel('Logarithmic Scale')
plt.xticks(rotation=90)

# Imposta l'asse y su scala logaritmica
bar_plot.set_yscale('log')

plt.show()
