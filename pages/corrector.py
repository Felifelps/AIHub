from ai.code_corrector_agent import CodeCorrectorAgent
from constants import LANGUAGES
from utils.page_utils import page_title, page_footer
import streamlit as st


page_title()
st.header('CodeCorrector')

agent = CodeCorrectorAgent()

question = st.text_input('Question')
language = st.selectbox('Language', LANGUAGES)
answer = st.text_area('Answer')

if st.button('Correct'):
    with st.spinner('Analising...'):
        try:
            response = agent.run(
                question=question,
                language=language,
                answer=answer
            )
            st.markdown('## Resposta')
            st.markdown(response)
        except Exception as e:
            print(e)
            st.warning('An error ocurred')

page_footer()
