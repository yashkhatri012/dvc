import pandas as pd 
import os
data= {
    'name' :[ 'yash', 'theone'],
    'age' :[ '19', '20']
}
df =pd.DataFrame(data)

new_row_loc= {'name': 'Gf1' , 'age':' 20'}
df.loc[len(df.index)] = new_row_loc
new_row_loc2= {'name': 'Gf2' , 'age':' 21'}
df.loc[len(df.index)] = new_row_loc2
data_dir= 'data'
os.makedirs(data_dir, exist_ok=True)
file_path= os.path.join(data_dir,'sample.csv')

df.to_csv(file_path, index=False)
print(f"csv file saved to {file_path}")

