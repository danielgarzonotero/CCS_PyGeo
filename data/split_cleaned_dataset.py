#%%%
import pandas as pd
import random

df = pd.read_csv('data/ccs_dataset_modified.csv')


total_rows = len(df)
target_rows = 10000

if total_rows > target_rows:
    
    rows_to_drop = total_rows - target_rows

    
    rows_to_drop_indices = random.sample(range(total_rows), rows_to_drop)

    df = df.drop(rows_to_drop_indices)

df.to_csv('data/ccs_dataset_reduced_10000.csv', index=False)



# %%
''' import pandas as pd
df = pd.read_csv('ccs_dataset_reduced_10000.csv') '''
# %%
