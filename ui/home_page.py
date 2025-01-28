import os
from ai.aihub_agent import AIHubAgent
from ai.rag.vector_store import VectorStore
from utils.file_handling import is_pdf, save_file, delete_file
import streamlit as st


def render_home_page():
    try:
        current_collections = VectorStore.list_collections()

        if not current_collections:
            st.error("No collections found. Please add documents to the vector store.")
            return
        
        with st.sidebar:

            collection = st.selectbox(
                'Select a Document Collection',
                ['---'] + current_collections
            )

            if st.button('Delete current file (irreversible action)'):
                with st.spinner('deleting'):
                    VectorStore.delete_collection(collection)
                return st.rerun()

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
    with st.sidebar:
        temp_dir = "temp_files"
        if 'temp_dir' not in st.session_state:
            os.makedirs(temp_dir, exist_ok=True)
            st.session_state.temp_dir = temp_dir

        files = st.file_uploader(
            'Add a PDF file:',
            accept_multiple_files=True
        )        

        if st.button('Add PDF'):
            with st.spinner('Adding...'):
                for file in files:
                    if not is_pdf(file.name):
                        return st.warning('Only pdf files accepted')

                    file_name = VectorStore.validate_collection_name(file.name)

                    file_path = os.path.join(temp_dir, file_name)

                    try:
                        save_file(file, file_path)

                        VectorStore.add_pdf(file_name, file_path)
                        st.success('File added succesfully!')

                        delete_file(file_path)
                    except Exception as e:
                        print(e)
                        st.warning('An error ocurred')

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

        try:
            response = agent.run(str(prompt))
        except Exception as e:
            return st.warning('An error ocurred')

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages[collection].append({"role": "assistant", "content": response})
