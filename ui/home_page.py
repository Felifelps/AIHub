import os
from ai.aihub_agent import AIHubAgent
from ai.rag.vector_store import VectorStore
import streamlit as st


def render_home_page():
    try:
        current_collections = VectorStore.list_collections()

        if not current_collections:
            st.error("No collections found. Please add documents to the vector store.")
            return

        collection = st.sidebar.selectbox(
            'Select a Document Collection',
            ['---'] + current_collections
        )

        render_add_pdf_form()

        if "messages" not in st.session_state:
            st.session_state.messages = {}

        if collection == '---':
            st.write('Select a file or add one on the sidebar!')
        else:
           render_chat_messages(collection)

    except Exception as e:
        st.error(f"An error occurred: {e}")


def render_add_pdf_form():
    temp_dir = "temp_files"
    if 'temp_dir' not in st.session_state:
        os.makedirs(temp_dir, exist_ok=True)
        st.session_state.temp_dir = temp_dir

    file = st.sidebar.file_uploader('Add a PDF file:')

    if file:
        
        if not file.name.endswith('.pdf'):
            return st.sidebar.warning('Only pdf files accepted')

        file_path = os.path.join(temp_dir, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

    if st.sidebar.button('Add PDF'):
        with st.spinner('Adding...'):
            VectorStore.add_pdf(
                file.name.replace(' ', ''),
                file_path
            )

            os.remove(file_path)
        st.rerun()


def render_chat_messages(collection):
    if collection not in st.session_state.messages:
        st.session_state.messages[collection] = []            

    for message in st.session_state.messages[collection]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        agent = AIHubAgent(collection)

        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages[collection].append({"role": "user", "content": prompt})

        response = agent.run(str(prompt))

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages[collection].append({"role": "assistant", "content": response})