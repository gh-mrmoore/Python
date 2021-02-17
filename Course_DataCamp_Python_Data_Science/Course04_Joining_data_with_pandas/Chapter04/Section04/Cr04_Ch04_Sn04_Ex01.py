#print(ur_wide.head())

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name=['month'], value_name='unempl_rate')

#print(ur_tall)

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

#print(ur_tall)

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by=['date'])

#print(ur_sorted)

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()