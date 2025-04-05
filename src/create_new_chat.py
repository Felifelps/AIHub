from ai.rag.vector_store import VectorStore
from utils.collection_name import validate_collection_name, convert_collection_name_to_valid
from utils.file_handling import is_pdf, save_as_temp_file, delete_file
import streamlit as st


@st.dialog('Create new chat')
def create_new_chat():

    chat_name = st.text_input('ChatName:')
    chat_type = st.selectbox(
        'Chat Type',
        [
            'PDF',
            'GithubRepo'
        ]
    )

    if chat_type == 'PDF':
        file = st.file_uploader('Add a PDF file:')
    elif chat_type == 'GithubRepo':
        repo_name = st.text_input('Repository Name', placeholder='username/repo_name')
        branch = st.text_input('Branch name', placeholder='master')
        extensions = st.text_input('Extensions', placeholder='.html,.css,.js')

    if st.button('Create new chat'):
        with st.spinner('Creating...'):
            if not chat_name:
                return st.warning("Chat Name required")

            is_valid, message = validate_collection_name(chat_name)

            if not is_valid:
                return st.warning(message)

            try:
                if chat_type == 'PDF':
                    if not file:
                        return st.warning('Select a pdf file to the chat')

                    if not is_pdf(file.name):
                        return st.warning('Only pdf files accepted')

                    temp_file = save_as_temp_file(file)
                    tf_path = temp_file.name

                    VectorStore.add_pdf(chat_name, tf_path)
                    delete_file(tf_path)

                    return st.success('File added succesfully!')
                elif chat_type == 'GithubRepo':
                    if not repo_name:
                        return st.error("You must add a repo name")
                    
                    if not branch:
                        return st.error("Define your branch")

                    VectorStore.add_github_repo(
                        chat_name,
                        repo_name,
                        branch,
                        #extensions.split(',')
                    )
                    return st.success('Repo added succesfully!')

            except Exception as e:
                print(e)
                st.warning('An error ocurred')

        st.rerun()
