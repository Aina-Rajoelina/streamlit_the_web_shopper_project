import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#chargement du fichier category_tree
events = pd.read_csv('C:\\Users\\Lenovo\\Documents\\DATA SCIENTEST\\PROJET E COMMERCE\\events.csv')

#Aperçu des 20 premières lignes
st.write(print(events.head()))


