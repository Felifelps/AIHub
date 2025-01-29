import os
from ai.aihub_agent import AIHubAgent
from ai.rag.vector_store import VectorStore
from utils.file_handling import is_pdf, save_file, delete_file
from utils.page_utils import page_title, page_footer
import streamlit as st


@st.dialog('Add new file')
def add_new_file():
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

@st.dialog('Delete current file')
def delete_current_file(collection):
    st.write(f'Are you sure you want to delete "{collection}"?')

    _, col2, col3 = st.columns([5, 1, 1])

    if col2.button('Yes', type='primary'):
        with st.spinner('deleting'):
            VectorStore.delete_collection(collection)
        st.rerun()

    if col3.button('No'):
        st.rerun()


page_title()

try:
    current_collections = VectorStore.list_collections()

    if not current_collections:
        st.error("No collections found. Please add documents to the vector store.")

    col1, col2, col3 = st.columns([13, 1, 1])

    with col1:
        collection = st.selectbox(
            'Select a Document Collection',
            ['---'] + current_collections
        )
    
    with col2:
        if st.button('', icon=':material/add:'):
            add_new_file()
        
    with col3:
        if collection != '---' and st.button('', icon=':material/delete:', type='primary'):
            delete_current_file(collection)

    if "messages" not in st.session_state:
        st.session_state.messages = {}

    if collection != '---':
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
                st.warning('An error ocurred')
                st.rerun()

            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages[collection].append({"role": "assistant", "content": response})


except Exception as e:
    st.error(f"An error occurred: {e}")

page_footer()
