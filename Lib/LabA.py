import pandas as pd

df = pd.read_csv('bankruptcy_data_set.csv')
# Task 1
#print(df)


# Task 2
df1 = df.drop(columns='Company')
#print(df1)
#print(df1.shape)

# Task 3
df2 = df1.dropna()
#print(df2)
#print(df2.shape)

# Task 4
New1= df2.loc[:,'WC/TA'] + df2.loc[:,'RE/TA']
New2= df2.loc[:,'EBIT/TA'] * df2.loc[:,'S/TA']

# Task 5
df3=pd.concat([df2,New1,New2],axis=1)
#print(df3)

# Task 6
six1 = df3.loc[10:20]
#print(six1)
six2 = df3.iloc[:,[0,1,2,3]]
#print(six2)
six3 = df3[['WC/TA','EBIT/TA']]
#print(six3)
six4 = df3.loc[df3['RE/TA'] < -20]
#print(six4)
six5 = df3.loc[(df3['RE/TA'] < -20) & (df3['Bankrupt'] == 0.0)]
#print(six5)
six6 = df3.loc[(df3['RE/TA'] < -20) & (df3['Bankrupt'] == 0.0), ['WC/TA','EBIT/TA']]
print(six6)
#done