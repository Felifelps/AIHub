from ai.code_corrector_agent import CodeCorrectorAgent
from constants import LANGUAGES
import streamlit as st


def render_code_corrector_page():
    st.header('CodeCorrector')
    agent = CodeCorrectorAgent()
    question = st.text_input('Question')
    language = st.selectbox(
        'Language',
        LANGUAGES
    )
    answer = st.text_area('Answer')

    if st.button('Correct'):
        with st.spinner('Analising...'):
            response = agent.run(
                question=question,
                language=language,
                answer=answer
            )
            st.markdown('## Resposta')
            st.markdown(response)
