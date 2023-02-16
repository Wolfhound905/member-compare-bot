import pandas as pd

file1 = ''
file2 = ''

# Everything below this line can be ignored

df1 = pd.read_csv(file1, sep=',', header=0, names=['guild_id', 'member_id', 'tag'], engine='python')
df2 = pd.read_csv(file2, sep=',', header=0, names=['guild_id', 'member_id', 'tag'], engine='python')

# we want the output to just be user_id,tag
merged_df = pd.merge(df1, df2, on=['member_id'], how='inner')
merged_df = merged_df[['member_id', 'tag_x']]
merged_df.columns = ['member_id', 'tag']

#write the result to a new csv file
merged_df.to_csv('common_members.csv', index=False)

# uncommon_members will be the members that are in file1 but not in file2 and vice versa
uncommon_members = pd.concat([df1, df2]).drop_duplicates(subset=['member_id'], keep=False)
uncommon_members.to_csv('uncommon_members.csv', index=False)



