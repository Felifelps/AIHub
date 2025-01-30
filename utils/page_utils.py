import streamlit as st


def page_title():
    st.set_page_config(
        page_title='AIHub',
        page_icon='🤖',
    )

    st.title('AIHub')


def page_footer():
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
