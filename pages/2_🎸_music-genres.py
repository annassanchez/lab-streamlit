import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f"""# These are the results by music genres
These are the 10 top most streamed music genres:
""")

top_genres = sc.info_genre(tracks)
st.dataframe(top_genres)

chart = tracks['chart'].unique().tolist()
chart_input = st.selectbox(f'Choose which playlist you want to analyze', chart)

st.markdown(f"""
Let's see the evolution of the `valence`, `danceability` and `energy` in the given period:
""")

column = st.selectbox('Choose the variable to see the evolution', ['energy', 'danceability', 'valence'])



si.music_lineplot(tracks, chart_input, top_genres['music_genre'].tolist(), column)
st.image(f'imagenes/lineplot_genre_{column}.png')

genre = st.selectbox('Select a genre to see the results', top_genres['music_genre'].tolist())

chart_type = st.selectbox('Choose the visualization type', ['boxplot', 'violinplot'])
si.general_chart_genres(tracks, chart_input, [genre], column, chart_type)
st.image(f'imagenes/genres_{chart_type}_{column}.png')

st.markdown(f"""
Let's see the `key` and `mode` in the given period:
""")

si.genre_kde(tracks, chart_input, [genre], 'key_mapped')
st.image(f'imagenes/genres_kde_key_mapped.png')
si.genre_kde(tracks, chart_input, [genre], 'mode_mapped')
st.image(f'imagenes/genres_kde_mode_mapped.png')