from ui.code_corrector_page import render_code_corrector_page
from ui.home_page import render_home_page
from ui.readme_generator_page import render_readme_generator_page
from utils.set_up_sqlite import set_up_sqlite
import streamlit as st


set_up_sqlite()

def main():
    st.set_page_config(
        page_title='AIHub',
        page_icon='🤖',
        initial_sidebar_state="expanded"
    )

    st.title('AIHub')

    pages = {
        'Home': render_home_page,
        'CodeCorrector': render_code_corrector_page,
        'ReadmeGenerator': render_readme_generator_page,
    }

    menu_option = st.sidebar.selectbox(
        'Select an option:',
        tuple(pages.keys())
    )

    render_page = pages[menu_option]

    render_page()

    st.markdown(
        '''
        <p
            style="text-align: center; position: fixed; bottom: 0"
        >
            © 2024 Felifelps - Todos os direitos reservados.
        </p>
        ''',
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()
