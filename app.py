# Main app page (sets up navigation and routing)

import streamlit as st
from multiapp import MultiApp
from components import summarize, forecast
import webbrowser

# Set up MultiApp feature (allows for multiple pages)
app = MultiApp()

st.set_page_config(page_title="Diplomatic ML App", page_icon="⬛", layout='centered', initial_sidebar_state="collapsed")

st.markdown("""
# Machine Learning Tools
Use our custom built Machine Learning Models to ease the educational process and increase efficiency 
""")

# if st.button('Return to Dashboard'):
#     webbrowser.open('https://diplomatica.vercel.app/dashboard', new=0)

st.markdown('<button style="border-color: black; border-radius: 10;" ><a style="-webkit-appearance: button; -moz-appearance: button; appearance: button; text-decoration: none; color: initial;" href="https://diplomatica.vercel.app/dashboard" target="_blank">Return to Dashboard</a></button>', unsafe_allow_html=True)

# st.markdown('[Return to Dashboard](https://diplomatica.vercel.app/dashboard)', unsafe_allow_html=True)

# Other pages
app.add_app("NLP Article Summary", summarize.app)
app.add_app("Forecast and Analyze Data", forecast.app)

# The main app
app.run()