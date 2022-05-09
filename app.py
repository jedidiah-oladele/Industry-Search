import streamlit as st
import pandas as pd
import random


def get_random():
    """Loads the random page"""
    random_row = df.iloc[random.randint(0, len(df)-1)]
    st.markdown(f"##### Sector: {random_row['Sector']}")
    st.markdown(f"##### Industry: {random_row['Industry']}")
    
    with st.expander('About'):
        st.write(random_row['Industry_description'])
        st.write(f"[Read more]({random_row['Industry_URL']})")


def explore():
    """Loads the explore page"""
    selected_sector = st.selectbox('Sector', df['Sector'].unique())
    selected_industry = st.selectbox('Industry', df[df['Sector']==selected_sector]['Industry'])

    selected_row = df[df['Industry']==selected_industry]

    with st.expander('About'):
        st.write(selected_row['Industry_description'].iloc[0])
        st.write(f"[Read more]({selected_row['Industry_URL'].iloc[0]})")



if __name__ == '__main__':

    # Load and cahce the data
    @st.cache(allow_output_mutation=True)
    def load_data():
        return pd.read_csv('data.csv')
    df = load_data()


    # Write Heading
    st.markdown("<h1 style='text-align:center'>Project Idea Generator</h1>", unsafe_allow_html=True)


    # Button asthetics
    st.write('')
    _, col2, _, col4, _ = st.columns([1,1,1,1,1])
    random_button = col2.button('Random')
    explore_button = col4.button('Explore')
    st.write('')


    # Page control logic
    if random_button:
        st.session_state['selected_page'] = 'random'
    if explore_button:
        st.session_state['selected_page'] = 'explore'

    # Makes sure the same page is displayed during rerun 
    if 'selected_page' in st.session_state:
        selected_page = st.session_state['selected_page']

        if selected_page == 'random':
            get_random()
        elif selected_page == 'explore':
            explore()



    # TODO Turn to footer
    st.write('This data was provided by the [US Bureau of Labor Statistics](https://www.bls.gov/iag/tgs/iag_index_alpha.htm)')
