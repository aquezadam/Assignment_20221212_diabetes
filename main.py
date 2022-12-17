# • • • ASSIGNMENT DAY 12

#       1.) Consider the diabetes dataset attached and perform the following operations
# using Pandas library:

import pandas as pd
diabetes_df = pd.read_csv("Diabetes_dataset.csv")

print("MAIN INFO")
main_info = diabetes_df.info()
print("\n")

main_stats = diabetes_df.describe()
print("MAIN STATS")
print(main_stats)
print("\n")


#           1.a) List first 10 and last 8 columns
print("Head and Tail. List first 10 and last 8 columns")
first_ten = diabetes_df.head(10)
print(first_ten)
last_eight = diabetes_df.tail(8)
print(last_eight)
print("\n")


#           1.b)Apply filters of your choice in the columns – pregnancies and age individually
# to extract subset of data and save them as csv files
#                                   **DiabetesPedigreeFunction**
#                                   A function that determines the risk of type 2 diabetes
#                                   based on family history, the larger the function, the higher
#                                   the risk of type 2 diabetes.
print("Applying Filters")
diabetes_df_focus = diabetes_df[["Pregnancies", "Age", "DiabetesPedigreeFunction", "Outcome"]]
diabetes_df_focus.to_csv("Relation Pregnancy_diabetes")
print("Head diabates_db_focus")
print(diabetes_df_focus.head())
print("\n")
list_diabetes = list(diabetes_df_focus["DiabetesPedigreeFunction"])
min_diabetes = min(list_diabetes)
max_diabetes = max(list_diabetes)
print(f"Min_diabates function value is {min_diabetes}. The max is {max_diabetes}")
diabetes_mean = diabetes_df["DiabetesPedigreeFunction"].mean()
diabetes_median = diabetes_df["DiabetesPedigreeFunction"].median()
print(f"The average number for the Diabetes Pedigree Function is {diabetes_mean}")
print(f"The middle number of the Diabetes Pedigree Function is {diabetes_median}")
outcome_data = list(diabetes_df["Outcome"])
print(f"Number of rows in which there is a diabetes diagnosis: {outcome_data.count(1)}.")
print("\n")

#           1.c) Extract the insulin column as a sequence and find out number of ‘0’ s in the
# column
#                                   Insulin: 2 hour serum insulin (mu U/ml).

insulin_data = list(diabetes_df["Insulin"])
print(f"Number of rows in which insulin is 0: {insulin_data.count(0)}.")
print("\n")

#   • • •  ASSIGNMENT DAY 13
#           2.) Consider the diabetes dataset from day 12 assignment section and perform the
#   following operations using Pandas library

#           2.a) Generate the summary stats for the columns and save them into a csv file
focus_stats = diabetes_df_focus.describe(percentiles=[0.1, 0.25, 0.75])
print("df Focus Stats:")
print(focus_stats)
focus_stats.to_csv("Stats - Relation Pregnancy_diabetes.csv")
print("\n")

#           2.b) Create a dashboard with at least 2 charts using streamlit
import plotly.express as px
plot_one = px.histogram(diabetes_df_focus, "DiabetesPedigreeFunction", color="Outcome",
                        color_discrete_sequence=["#b7094c", "#00b4d8"],barmode="group",
                        title="Diabetes factor and outcome of diabetes")
plot_two = px.pie(diabetes_df_focus, "Pregnancies", title="Proportion based on number of pregnancies",
                  color_discrete_sequence=["#800f2f", "#b7094c", "#a01a58", "#892b64", "#723c70", "#5c4d7d", "#455e89", "#2e6f95",
                                            "#1780a1", "#0091ad", "#219ebc","#00b4d8","#48cae4", "#90e0ef", "#ade8f4", "#caf0f8","#f1faee"])
plot_three = px.scatter(diabetes_df_focus, "Age","Pregnancies", color="Outcome", color_continuous_scale=["#ff8fa3","#c9184a"],
                        title="Number of pregnancies by age and diabetes diagnosis (1 = yes, 0 = no)")

#   • • •  ASSIGNMENT DAY 14
#          3.) Try out the missing value and outlier detection on diabetes dataset [optional]
# Write a function to check outlier for each column. Remove outliers.
# Write a function to substitute null values with the mean/median
# write a function to pritn the head of the processed DF
print("PROCESSING INSULIN COLUMN")
min_insulin = diabetes_df["Insulin"].min()
max_insulin = diabetes_df["Insulin"].max()
insulin_mean = diabetes_df["Insulin"].mean()
insulin_median = diabetes_df["Insulin"].median()
q1 = diabetes_df["Insulin"].quantile(0.25)
q3 = diabetes_df["Insulin"].quantile(0.75)
iqr = q3-q1
st_min = q1 - (1.5*iqr)
st_max = q3 + (1.5*iqr)
print(f"Q1 ={q1}, Q3= {q3}, st_max = {st_max}, st_min = {st_min},max_insulin = {max_insulin}, min_insulin = {min_insulin}")
print(f"Insulin stats. Mean = {insulin_mean}. Median = {insulin_median}")

list_insulin_above_stmax = list(diabetes_df["Insulin"])
insulin_below_stmax = diabetes_df[diabetes_df["Insulin"] <= st_max]
print(f"The shape of the df with insulin values below the stmax is: {insulin_below_stmax.shape}")

df_non_insulin_outliers = diabetes_df[(diabetes_df["Insulin"] <= st_max) & (diabetes_df["Insulin"] >= 1)]
print(f"Insulin shape without outliers and without insulin = 0 is {df_non_insulin_outliers.shape}.")
print(df_non_insulin_outliers.head())
print("\n")



# df_non_outliers = df_sans_duplicate[(df_sans_duplicate["km_driven"] < st_max) | (df_sans_duplicate["km_driven"] > st_min)]
# # df = df[(df["column_name"] > compare) operator (df["column_name"] > compare)]
# print(df_non_outliers.shape)

# outcome_data = list(diabetes_df["Outcome"])
# print(f"Number of rows in which there is a diabetes diagnosis: {outcome_data.count(1)}.")



# max_value = df_sans_duplicate["km_driven"].max()
# min_value = df_sans_duplicate["km_driven"].min()
# q1 = df_sans_duplicate["km_driven"].quantile(0.25)
# q3 = df_sans_duplicate["km_driven"].quantile(0.75)
# iqr = q3-q1
# st_max = q3 + (1.5*iqr)
# st_min = q1 - (1.5*iqr)
# print(q1, q3, st_max, st_min,max_value,min_value)
# df_non_outliers = df_sans_duplicate[(df_sans_duplicate["km_driven"] < st_max) | (df_sans_duplicate["km_driven"] > st_min)]
# print(df_non_outliers.shape)

# diabetes_df_focus.loc[diabetes_df["Insulin"] < 0, "Range Description"] = "no data"
# diabetes_df_focus.loc[(diabetes_df["Insulin"] >= 1) & (diabetes_df["Insulin"] <= 25),"Range Description"] = "normal insulin"
# diabetes_df_focus.loc[diabetes_df["Insulin"] > 25, "Range Description"] = "high Insulin"