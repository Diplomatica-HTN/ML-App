# Main app page (sets up navigation and routing)

import streamlit as st
from multiapp import MultiApp
from components import summarize, forecast

# Set up MultiApp feature (allows for multiple pages)
app = MultiApp()

st.set_page_config(page_title="Diplomatic ML App", page_icon="⬛", layout='centered', initial_sidebar_state="collapsed")

st.markdown("""
# Machine Learning Tools
Use our custom built Machine Learning Models to ease the educational process and increase efficiency 
""")



# Other pages
app.add_app("NLP Article Summary", summarize.app)
app.add_app("Forecast and Analyze Political Data", forecast.app)

# The main app
app.run()