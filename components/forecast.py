import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    st.markdown('## Forecast and Analyze Data')

    st.markdown("""
    Visualize social data and extrapolate new information
    """)

    full_gdp = pd.read_csv('data/gdp.csv')
    full_gdp = full_gdp.drop(columns='Unnamed: 0')

    full_imports = pd.read_csv('data/imports.csv')
    full_imports = full_imports.drop(columns='Unnamed: 0')

    full_pop = pd.read_csv('data/population.csv')
    full_pop = full_pop.drop(columns='Unnamed: 0')

    fig1 = px.line(full_gdp, x='Year', y='GDP', color='Country', title='GDP over Time')
    fig2 = px.line(full_imports, x='Year', y='Imports of Goods and Services (% GDP)', color='Country', title='Imports of Goods and Services over Time')    
    fig3 = px.line(full_pop, x='Year', y='Population', color='Country', title='Population over Time')

    section = st.radio('Sections',('Graphs', 'Predictions'))
    if section == 'Graphs':
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
        st.plotly_chart(fig3)
    else:
        st.write("### 2022 Predicted Metrics")
        st.write("""
        **Linear Regression**
        - GDP (Canada): `$1.5` Trillion
        - GDP (Australia): `$1.2` Trillion
        - Imported Goods (Canada): `30%` of GDP
        - Imported Good (Australia): `18%` of GDP
        - Population (Canada): `39` Million
        - Population (Australia): `27` Million
        """)