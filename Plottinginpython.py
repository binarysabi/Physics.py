import pandas as pd
import matplotlib.pyplot as plt

# Importing data from excelsheet
df = pd.read_excel('exampledata.xlsx')

# plotting the individual datapoints
plt.scatter(df['Mass'], df['Y_Linear'], color='blue', label='Datapoints')

plt.title('Linear Data from Excel')
plt.xlabel('X-values')
plt.ylabel('Y-values')
plt.legend()
plt.show()