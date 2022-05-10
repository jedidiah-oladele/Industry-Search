import streamlit as st
import pandas as pd
import random


TASKS = ['Data Collection and Cleaning', 'Exploratory Data Analysis', 'Data Visualization', 'Article and Explainer blog', 'Modelling and Deployment']


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



def explore():
    """Loads the explore page"""
    selected_sector = st.selectbox('Sector', df['Sector'].unique())
    selected_industry = st.selectbox('Industry', df[df['Sector']==selected_sector]['Industry'])

    selected_row = df[df['Industry']==selected_industry]

    with st.expander('About'):
        st.write(selected_row['Industry_description'].iloc[0])
        st.write(f"[Read more]({selected_row['Industry_URL'].iloc[0]})")






if __name__ == '__main__':

    st.set_page_config(page_title='Project Idea Generator')

    # Load and cahce the data
    @st.cache(allow_output_mutation=True)
    def load_data():
        return pd.read_csv('data.csv')
    df = load_data()


    # Write Heading
    st.markdown("<h1 style='text-align:center'>Project Idea Generator</h1>", unsafe_allow_html=True)


    # Button asthetics
    with st.container():
        st.write('')
        col1, _, col3 = st.columns([1,2,1])
        col1, col3 = st.columns(2)
        random_button = col1.button('Random')
        explore_button = col3.button('Explore')
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
    #st.write('This data was provided by The [US Bureau of Labor Statistics](https://www.bls.gov/iag/tgs/iag_index_alpha.htm)')
    


footer = """<style>
footer {
    visibility: visible;
}
footer:before {
	content:'This data was provided by the US Bureau of Labor Statistics'; 
	visibility: visible;
	display: block;
	position: relative;
	top: 2px;
}
</style>
"""


footer2="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: absolute;
left: 0;
top: 200px;
width: 100%;
text-align: center;
padding: 30px;
}

</style>
<div class="footer">
<p style="font-size:0.9em">This data was provided by the <a href="https://www.bls.gov/iag/tgs/iag_index_alpha.htm">US Bureau of Labor Statistics</a></p>
</div>
"""


st.markdown(footer, unsafe_allow_html=True)
st.markdown(footer2, unsafe_allow_html=True)




# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


