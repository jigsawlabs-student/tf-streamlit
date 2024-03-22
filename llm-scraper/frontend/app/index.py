import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from view_functions import *

df = find_positions()
st.dataframe(df)

