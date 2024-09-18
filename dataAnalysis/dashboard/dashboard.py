import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_air_quality_station_df(df):
    """
    Create a dataframe with aggregated air quality data per station.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing air quality data.

    Returns:
    pandas.DataFrame: The resulting dataframe with aggregated air quality data per station.
    """
    # Membuat tren kualitas udara per kota
    air_quality_station = df.groupby('station').agg({
        'PM2.5': 'mean',
        'PM10': 'mean',
        'SO2': 'mean',
        'NO2': 'mean',
        'CO': 'mean',
        'O3': 'mean'
    }).reset_index()

    # Tambahkan kolom kualitas udara buruk
    # Semakin kecil nilai bad_air_quality, maka semakin baik kualitas udaranya
    air_quality_station['bad_air_quality'] = (
        air_quality_station['PM2.5']
        + air_quality_station['PM10']
        + air_quality_station['SO2']
        + air_quality_station['NO2']
        + air_quality_station['CO']
        - air_quality_station['O3']
        ) / 6

    # Urutkan data dari kualitas udara terbaik
    air_quality_station.sort_values('bad_air_quality', ascending=True, inplace=True)

    # Drop kolom-kolom yang tidak diperlukan
    air_quality_station.drop(['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], axis=1, inplace=True)

    # Reset index
    air_quality_station.reset_index(drop=True, inplace=True)

    return air_quality_station

def create_average_air_quality_df(df):
    """
    Create a dataframe with average air quality data per month.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing air quality data.

    Returns:
    pandas.DataFrame: The resulting dataframe with average air quality data per month.
    """
    # Karena data yang ada sangat banyak, kita akan mengambil data rata-rata per bulan
    average_air_quality = df.groupby('datetime').agg({
        'PM2.5': 'mean',
        'PM10': 'mean',
        'SO2': 'mean',
        'NO2': 'mean',
        'CO': 'mean',
        'O3': 'mean'
    }).reset_index()

    # Buat kolom kualitas udara buruk
    # Semakin kecil nilai bad_air_quality_station, maka semakin baik kualitas udaranya
    average_air_quality['bad_air_quality'] = (
        average_air_quality['PM2.5']
        + average_air_quality['PM10']
        + average_air_quality['SO2']
        + average_air_quality['NO2']
        + average_air_quality['CO']
        - average_air_quality['O3']
        ) / 6

    # Ubah tipe data datetime dan karena datanya banyak, kita akan mengambil data rata-rata per bulan
    average_air_quality = average_air_quality.resample('M', on='datetime').mean().reset_index()
    average_air_quality['datetime'] = average_air_quality['datetime'].astype('datetime64[ns]').dt.strftime('%Y-%m')

    # Buang data yang tidak diperlukan
    average_air_quality.drop(['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], axis=1, inplace=True)

    return average_air_quality

def create_average_quality_station_df(df):
    """
    Create a dataframe with average air quality data per station and month.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing air quality data.

    Returns:
    pandas.DataFrame: The resulting dataframe with average air quality data per station and month.
    """
    # Karena data yang ada sangat banyak, kita akan mengambil data rata-rata per bulan serta menggabungkan data menjadi satu kolom "trend"
    average_air_quality_station = df.groupby(['station', 'datetime']).agg({
        'PM2.5': 'mean',
        'PM10': 'mean',
        'SO2': 'mean',
        'NO2': 'mean',
        'CO': 'mean',
        'O3': 'mean'
    }).reset_index()

    # Buat kolom kualitas udara buruk
    # Semakin kecil nilai bad_air_quality_station, maka semakin baik kualitas udaranya
    average_air_quality_station['bad_air_quality'] = (
        average_air_quality_station['PM2.5']
        + average_air_quality_station['PM10']
        + average_air_quality_station['SO2']
        + average_air_quality_station['NO2']
        + average_air_quality_station['CO']
        - average_air_quality_station['O3']
        ) / 6

    # Buang data yang tidak diperlukan
    average_air_quality_station.drop(['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], axis=1, inplace=True)

    # Dapatkan rata-rata kualitas udara per bulan
    average_air_quality_station = average_air_quality_station.groupby(['station']).resample('M', on='datetime').mean().reset_index()

    average_air_quality_station['datetime'] = average_air_quality_station['datetime'].astype('datetime64[ns]').dt.strftime('%Y-%m')

    return average_air_quality_station

def create_geoanalysis_data_df(df, average_air_quality_station):
    """
    Create a geoanalysis dataframe by aggregating and resampling the given dataframe.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing the data to be analyzed.
    average_air_quality_station (pandas.DataFrame): The dataframe containing the average air quality data per station.

    Returns:
    pandas.DataFrame: The geoanalysis dataframe with aggregated and resampled data.

    """
    # Buat data geoanalisis
    geoanalysis_data = df.groupby(['station', 'datetime']).agg({
        'WSPM' : 'mean',
        'TEMP': 'mean',
        'PRES': 'mean',
        'DEWP': 'mean',
    }).reset_index()

    # Ratakan data menjadi per bulan
    geoanalysis_data = geoanalysis_data.groupby(['station']).resample('M', on='datetime').mean().reset_index()

    geoanalysis_data['datetime'] = geoanalysis_data['datetime'].astype('datetime64[ns]').dt.strftime('%Y-%m')

    # Gabungkan data geoanalysis dengan data kualitas udara per kota
    geoanalysis_air_quality = geoanalysis_data.merge(average_air_quality_station, on=['station', 'datetime'], how='left')

    return geoanalysis_air_quality

df = pd.read_csv('./dashboard/data.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df.reset_index(inplace=True)

min_date = df['datetime'].min()
max_date = df['datetime'].max()

with st.sidebar:
    st.title('Air Quality Dashboard')
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date, max_value=max_date, value=[min_date, max_date]
    )
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

main_df = df[(df['datetime'] >= start_date) & (df['datetime'] <= end_date)]

air_quality_station = create_air_quality_station_df(main_df)
average_air_quality = create_average_air_quality_df(main_df)
average_air_quality_station = create_average_quality_station_df(main_df)
geoanalysis_data = create_geoanalysis_data_df(main_df, average_air_quality_station)

st.header('Tren Kualitas Udara di Kota Beijing :mask:')

st.subheader('Peringkat Kualitas Udara Kota Beijing')
col1, col2 = st.columns(2)

with col1:
    st.write('Kota-kota dengan kualitas udara terbaik')
    st.dataframe(air_quality_station.head(3))

with col2:
    st.write('Kota-kota dengan kualitas udara terburuk')
    st.dataframe(air_quality_station.tail(3))

st.subheader('Tren Kualitas Udara Buruk di China')
colors = sns.color_palette('rainbow', len(air_quality_station['station'].tolist()))

fig, ax = plt.subplots(figsize=(30, 16))
sns.lineplot(data=average_air_quality, x='datetime', y='bad_air_quality', palette=colors, ax=ax, linewidth=10)
ax.set_xlabel('Bulan', fontsize=35)
ax.set_ylabel('Kualitas Udara Buruk', fontsize=35)
ax.tick_params(axis='x', labelsize=0)
ax.tick_params(axis='y', labelsize=35)
ax.grid(True)
st.pyplot(fig)

st.subheader('Tren Kualitas Udara Buruk di Kota-Kota China')
st.write('Klik pada stasiun untuk melihat tren kualitas udara di stasiun tersebut.')
tabs = st.tabs(air_quality_station['station'].tolist())

for i, tab in enumerate(tabs):
    with tab:
        fig, ax = plt.subplots(figsize=(30, 16))
        sns.lineplot(data=average_air_quality_station[average_air_quality_station['station'] == air_quality_station['station'][i]], x='datetime', y='bad_air_quality', palette=colors, ax=ax, linewidth=10)
        ax.set_xlabel('Bulan', fontsize=35)
        ax.set_ylabel('Kualitas Udara Buruk', fontsize=35)
        ax.tick_params(axis='x', labelsize=0)
        ax.tick_params(axis='y', labelsize=35)
        ax.grid(True)
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=35)
        st.pyplot(fig)

st.subheader('Analisis Geospasial')
st.write('Klik pada kolom geografis untuk melihat korelasi dengan kualitas udara buruk.')

tabs = st.tabs(['Kecepatan Angin', 'Suhu', 'Tekanan Udara', 'Titik Embun'])

for i, tab in enumerate(tabs):
    with tab:
        fig, ax = plt.subplots(figsize=(30, 16))
        sns.scatterplot(data=geoanalysis_data, x='bad_air_quality', y=geoanalysis_data.columns[i+2], hue='station', palette=colors, ax=ax, s=500)
        ax.set_xlabel('Kualitas Udara Buruk', fontsize=35)
        ax.set_ylabel(geoanalysis_data.columns[i+2], fontsize=35)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=35)
        ax.grid(True)
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=35)
        st.pyplot(fig)

st.caption("Dibuat oleh Jonathan Immanuel, 2024, [Github](https://github.com/andreasjonathanimm)")