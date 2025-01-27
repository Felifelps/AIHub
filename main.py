from ui.code_corrector_page import render_code_corrector_page
from ui.home_page import render_home_page
from ui.readme_generator_page import render_readme_generator_page
import streamlit as st


def main():
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
