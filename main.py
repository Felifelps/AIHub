from ai.especific_agents.aihub_agent import AIHubAgent
from ai.rag.vector_store import VectorStore
from src.create_new_chat import create_new_chat
from src.delete_chat import delete_current_chat
from utils.page_utils import page_title, page_footer
import streamlit as st


page_title()

try:
    st.session_state.current_collections = VectorStore.list_collections()

    if not st.session_state.current_collections:
        st.error("No collections found. Please add documents to the vector store.")

    col1, col2, col3 = st.columns([13, 1, 1])

    with col1:
        collection = st.selectbox(
            'Select a Document Collection',
            ['---'] + st.session_state.current_collections
        )

    with col2:
        if st.button('', icon=':material/add:'):
            create_new_chat()

    with col3:
        if collection != '---' and st.button('', icon=':material/delete:', type='primary'):
            delete_current_chat(collection)

    if "messages" not in st.session_state:
        st.session_state.messages = {}

    if collection != '---':
        if collection not in st.session_state.messages:
            st.session_state.messages[collection] = []

        for message in st.session_state.messages[collection]:
            with st.chat_message(message[0]):  # role
                st.markdown(message[1])  # content

        if prompt := st.chat_input("What is up?"):
            agent = AIHubAgent(
                collection,
                st.session_state.messages[collection]
            )

            with st.chat_message("user"):
                st.markdown(prompt)

            st.session_state.messages[collection].append(("user", prompt))

            try:
                with st.spinner('Loading response...'):
                    response = agent.run(str(prompt))
            except Exception as e:
                print(e)
                st.warning('An error ocurred')
                st.rerun()

            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages[collection].append(("assistant", response))


except Exception as e:
    st.error(f"An error occurred: {e}")

page_footer()
