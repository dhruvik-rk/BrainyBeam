# # Use pandas' pivot and pivot_table functions to perform advanced data reshaping operations.


import pandas as pd

data = {
    'Date': ['1-12-2024', '1-12-2024', '1-12-2024', '1-12-2024',
             '2-12-2024', '2-12-2024', '2-12-2024', '2-12-2024'],
    'Region': ['North', 'North', 'South', 'South', 'North', 'North', 'South', 'South'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [150, 200, 180, 210, 120, 220, 200, 240]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

print("Pivot Function : ===========================================")
#task 1: pivot function ===========================================
p_df = df.pivot(index=['Date', 'Region'], columns='Product', values='Sales')
        #reset index for easy readability
p_df = p_df.reset_index()
print("pivot function : ")
print(p_df)

print("\nPivot Table : ===========================================")
#task 2: pivot_table ===========================================
pt_df = pd.pivot_table(df, values='Sales', 
                                index=['Date', 'Region'], 
                                columns='Product', 
                                aggfunc='sum', 
                                fill_value=0)

        #reset index for easy readability
pt_df = pt_df.reset_index()
print("\npivot table : ")
print(pt_df)

#region wise sales
agg_sales_by_region = df.groupby(['Region', 'Product']).agg({'Sales': 'sum'}).reset_index()
print("\nregion wise total sales:")
print(agg_sales_by_region)

#combile: pivot and agg df
concatenated_df = pd.concat([pt_df, agg_sales_by_region], axis=1)
        #drop duplicate column
concatenated_df = concatenated_df.loc[:, ~concatenated_df.columns.duplicated()]
        #print df
print("\nfinal result: ")
print(concatenated_df)