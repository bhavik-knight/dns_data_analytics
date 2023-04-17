import pandas as pd

df1_dummy = {
    "serial_id": ["1", "2", "3", "4", "5"],
    "sale_month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": ["12300", "25100", "17800", "20100", "21000"],
}


df2_dummy = {
    "serial_id": ["6", "7", "8", "9", "10"],
    "sale_month": ["Jun", "Jul", "Aug", "Sep", "Oct"],
    "sales": ["25000", "23700", "24600", "24000", "23950"],
}


df3_dummy = {
    "sales_threshold": ["No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
    "bonus_threshold": ["No", "Yes", "No", "No", "No", "Yes", "No", "Yes", "Yes", "No"],
}


# create all 3 data frames
df1 = pd.DataFrame(data=df1_dummy)
df2 = pd.DataFrame(data=df2_dummy)
df3 = pd.DataFrame(data=df3_dummy)

# concate the two dataframe df1 & df2
df4_wrong = pd.concat([df1, df2])

# concate with unique ID
df4 = pd.concat([df1, df2], ignore_index=True)
print(df4)
print(80 * "-")

# concate df3 with new dataframe: df4
df5 = pd.concat([df4, df3])
print(df5)
print(80 * "-")

# concate on a column that is common (here it is ID)
df6 = pd.concat([df4, df3], axis=1)
print(df6)
