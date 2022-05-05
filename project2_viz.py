import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
sns.set()

imdb = pd.read_csv('imdb.csv')
people = pd.read_csv('people.csv')

st.title('Visualisations et indicateurs')
st.write('Le résultat de nos analyses sur l\'industrie du film')

