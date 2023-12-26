import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#create helper function for dataframe

def create_rentals_per_season_df(df):
    rentals_per_season = all_df.groupby('season')['cnt'].sum()
    return rentals_per_season

def create_users_notholiday_and_holiday_df(df):
    users_notholiday_and_holiday = all_df.holiday.value_counts()
    return users_notholiday_and_holiday

all_df = pd.read_csv("https://raw.githubusercontent.com/nurhadimeilana05/Proyek-Analisis-Data-dengan-Python-Dicoding-/main/all_data.csv")

with st.sidebar:
    all_df["dteday"] = pd.to_datetime(all_df["dteday"])
    min_date = all_df["dteday"].min()
    max_date = all_df["dteday"].max()

#create dataframes
rentals_per_season = create_rentals_per_season_df(all_df)
users_notholiday_and_holiday = create_users_notholiday_and_holiday_df(all_df)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/nurhadimeilana05/Proyek-Analisis-Data-dengan-Python-Dicoding-/main/bike-share-logo.png")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Bike Sharing Dashboard')

#Number of Rentals per Season
st.subheader('Number of Rentals per Season')

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    y=rentals_per_season.values,
    x=rentals_per_season.index,
    ax=ax
)

plt.title("Number of Rentals per Season", loc="center", fontsize=15)
plt.ylabel("Number of Rentals")
plt.xlabel("Season")
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

#Number of Users on Holiday and Not Holiday
st.subheader('Number of Users on Holiday and Not Holiday')

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    y=users_notholiday_and_holiday.values,
    x=users_notholiday_and_holiday.index,
    ax=ax
)

plt.title("Number of Users on Holiday and Not Holiday", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)