
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Task 1/2. Load into panda and get descriptive stats

boston_df = pd.read_csv('boston1.csv')


print(boston_df.describe())


# Task 3/4. Run to load some different graphs

# plt.figure()
# sns.distplot(boston_df['CHAS'], rug=True)
# plt.xlabel('CHAS')
# plt.ylabel('Frequency')
# plt.show()
#
# plt.figure()
# sns.distplot(np.log1p(boston_df['CHAS']), rug=True)
# plt.xlabel('CHAS')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure()
# sns.distplot(boston_df['INDUS'], rug=True)
# plt.xlabel('INDUS')
# plt.ylabel('Frequency')
# plt.show()


# Task 5. Pair-wise and heatmap

# sns.pairplot(boston_df)
# plt.show()
#
# cmap = sns.diverging_palette(220, 10, as_cmap=True)
# sns.heatmap(boston_df.corr(), square=True, linewidths=.5,
#             vmin=-1.0, vmax=1.0, cmap=cmap, annot=False)
# plt.show()