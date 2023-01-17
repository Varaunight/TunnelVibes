import pandas as pd

# load excel sheet
df = pd.read_excel('edge_cons.xlsx')

# sort dataframe by pair columns
df.sort_values(by=['First', 'Second'], inplace=True)

# remove duplicate pairs
df.drop_duplicates(subset=['First', 'Second'], inplace=True)

# create new column with flipped pairs
df['flipped_pair'] = df[['Second', 'First']].apply(lambda x: ' '.join(x), axis=1)

# sort dataframe by flipped pair column
df.sort_values(by=['flipped_pair'], inplace=True)

# remove duplicate flipped pairs
df.drop_duplicates(subset=['flipped_pair'], inplace=True)

# drop flipped_pair column
df.drop(columns=['flipped_pair'], inplace=True)

# save cleaned dataframe to new excel sheet
df.to_excel('edges.xlsx', index=False)




