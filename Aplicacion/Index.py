import json
import folium
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

from PIL                      import Image
from plotly                   import express as px
from folium.plugins           import MarkerCluster
from streamlit_folium         import folium_static
from matplotlib.pyplot        import figimage
from distutils.fancy_getopt   import OptionDummy

st.set_page_config(page_title='Proyecto-JQ - home',
                    layout="wide", 
                    page_icon=':peach:',
                    initial_sidebar_state="expanded")
                    