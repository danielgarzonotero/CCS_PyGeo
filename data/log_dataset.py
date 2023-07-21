
#%%

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

column_index = 6
df = pd.read_csv('ccs_dataset_modified_log.csv')

plt.hist(df.iloc[:, column_index], bins=100, color="lightblue") 
plt.xlabel('Values log(CCS) (CCS in Å^2)')
plt.ylabel('Frequency')
plt.title('Peptides with [ox].M are not included', size=9)
plt.suptitle('Histogram CCS - Meier et al. Dataset')


data_mean = np.mean(df.iloc[:, column_index])
data_std = np.std(df.iloc[:, column_index])


plt.text(0.95, 0.85, f"Mean: {data_mean:.2f} \nStd: {data_std:.2f}", 
         transform=plt.gca().transAxes, ha='right', color='black',
         bbox=dict(facecolor='white', edgecolor='grey', boxstyle='round,pad=0.5'))

plt.show()
# %%
""" column_index = 6  
df = pd.read_csv("ccs_dataset_modified.csv")
plt.hist(df.iloc[:, column_index], bins=10) 
plt.xlabel('Values CCS')
plt.ylabel('Frequency')
plt.title('Histogram CCS')
plt.show()




column_title = df.columns[column_index]

print("Título de la columna número 6:", column_title)
column_title = 'log(ccs)'
df = df.rename(columns={df.columns[column_index]: column_title})
df.iloc[:, column_index] = df.iloc[:, column_index].apply(lambda x: math.log(x))
df.to_csv("ccs_dataset_modified_log.csv", index=False)

plt.hist(df.iloc[:, column_index], bins=10)
plt.xlabel(' Values Log (CCS)')
plt.ylabel('Frequency')
plt.title('Histogram of Log(CCS)')
plt.show()
 """