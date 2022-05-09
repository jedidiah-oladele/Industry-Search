import streamlit as st
import pandas as pd
import random


# Load data
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('data.csv')
df = load_data()


#st.set_page_config(layout='wide')
st.markdown("<h1 style='text-align:center'>Project Idea Generator</h1>", unsafe_allow_html=True)


def get_random():
    random_row = df.iloc[random.randint(0, len(df)-1)]
    st.markdown(f"##### Sector: {random_row['Sector']}")
    st.markdown(f"##### Industry: {random_row['Industry']}")
    
    description_expander = st.expander('About')
    description_expander.write(random_row['Industry_description'])
    description_expander.write(f"[Read more]({random_row['Industry_URL']})")


def explore():
    st.selectbox('Sector', df['Sector'].unique())


# Button asthetics
st.write('')
_, col2, _, col4, _ = st.columns([2,1,1,1,2])
random_button = col2.button('Random')
explore_button = col4.button('Explore')
st.write('')

if random_button:
    get_random()
if explore_button:
    explore()



st.write('This data was provided by the [US Bureau of Labor Statistics](https://www.bls.gov/iag/tgs/iag_index_alpha.htm)')