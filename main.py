import pandas as pd
from script import data

df = data()

print("Columns in the DataFrame:", df.columns)

metropolitan_cities = ["Delhi", "Bangalore"]

df['Citytype'] = df['city'].apply(lambda x: 'Metropolitan' if x in metropolitan_cities else 'Non_Metropolitan')

summary = df.groupby('Citytype')[
    ['purchasefrequency', 'paymentoption', 'browsingtime', 'retailersshopped']
].agg(lambda x: x.mode()[0])

print("Comparison of Online Shopping Behaviors:")
print(summary)
print()
print()
import seaborn as sns
import matplotlib.pyplot as plt

region_mapping = {
    'Delhi': 'North' , 'Bangalore ': 'South'
}

df['Region'] = df['city'].map(region_mapping)

region_summary = df.groupby('Region')[['purchasefrequency', 'paymentoption', 'productinfo']].agg(
    lambda x: x.value_counts().index[0]
)


sns.countplot(data=df, x='Region', hue='paymentoption', palette='viridis')
plt.title('Payment Preferences Across Regions in India')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Payment Option', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

sns.countplot(data=df, x='Region', hue='purchasefrequency', palette='muted')
plt.title('Purchase Frequency Across Regions in India')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Frequency', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
