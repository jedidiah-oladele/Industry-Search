import streamlit as st
import pandas as pd
import random


TASKS = ['Data Collection and Cleaning',
        'Exploratory Data Analysis',
        'Data Visualization',
        'Article and Explainer blog',
        'Modelling and Deployment'
        ]


data_source="""
<div class="footer">
<p style="font-size:0.9em; text-align:center; padding:30px">This data was provided by The <a href="https://www.bls.gov/iag/tgs/iag_index_alpha.htm">US Bureau of Labor Statistics</a></p>
</div>
"""



def get_random():
    """Loads the random page"""
    task = random.choice(TASKS)
    st.markdown(f'##### Task: {task}')

    random_row = df.iloc[random.randint(0, len(df)-1)]
    st.markdown(f"##### Sector: {random_row['Sector']}")
    st.markdown(f"##### Industry: {random_row['Industry']}")
    
    with st.expander('About'):
        st.write(random_row['Industry_description'])
        st.write(f"[Read more]({random_row['Industry_URL']})")
    
    st.markdown(data_source, unsafe_allow_html=True)




def explore():
    """Loads the explore page"""
    selected_sector = st.selectbox('Sector', df['Sector'].unique())
    selected_industry = st.selectbox('Industry', df[df['Sector']==selected_sector]['Industry'])

    selected_row = df[df['Industry']==selected_industry]

    with st.expander('About'):
        st.write(selected_row['Industry_description'].iloc[0])
        st.write(f"[Read more]({selected_row['Industry_URL'].iloc[0]})")

    st.markdown(data_source, unsafe_allow_html=True)






if __name__ == '__main__':

    st.set_page_config(page_title='Industry Generator')
    st.markdown("<style>#MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)

    # Load and cahce the data
    @st.cache(allow_output_mutation=True)
    def load_data():
        return pd.read_csv('data.csv')
    df = load_data()


    # Write Heading
    st.markdown("<h1 style='text-align:center'>Industry Generator</h1>", unsafe_allow_html=True)


    # Button asthetics
    with st.container():
        st.write('')
        col1, col3 = st.columns([1,1])
        col1, col3 = st.columns(2)
        random_button = col1.button('Random Selection')
        explore_button = col3.button('Explore All')
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
