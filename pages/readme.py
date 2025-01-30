from ai.especific_agents.readme_generator_agent import ReadmeGeneratorAgent
from utils.page_utils import page_title, page_footer
import streamlit as st


page_title()
st.header('ReadmeGenerator')

agent = ReadmeGeneratorAgent()

repo_name = st.text_input('Repository Name', placeholder='username/repo_name')
branch = st.text_input('Branch name', placeholder='master')
extensions = st.text_input('Extensions', placeholder='.html,.css,.js')

if st.button('Generate'):
    with st.spinner('Generating...'):
        try:
            response = agent.run(
                repo_name=repo_name,
                branch=branch,
                extensions=extensions,
            )
            st.markdown(response)
        except Exception as e:
            print(e)
            st.warning('An error ocurred')

page_footer()
