import pandas as pd

# open csv
data_df = pd.read_csv("Projects/Starcraft2_MutationWeekAnalysis/mutation_weeks.csv")

# round category counts to two decimals
category_counts = (data_df['Brutal+ Level'].value_counts(normalize=True) * 100).map('{:.1f}%'.format)

print ("Weekly Mutation Brutal+ Difficulty Level Breakdown")
print(category_counts)