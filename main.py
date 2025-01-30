from ai.especific_agents.aihub_agent import AIHubAgent
from ai.rag.vector_store import VectorStore
from utils.collection_name import validate_collection_name, convert_collection_name_to_valid
from utils.file_handling import is_pdf, save_as_temp_file, delete_file
from utils.page_utils import page_title, page_footer
import streamlit as st


@st.dialog('Create new chat')
def create_new_chat():

    chat_name = st.text_input('ChatName (Defaults to file name):')
    file = st.file_uploader('Add a PDF file:')

    if st.button('Create new chat') and file:
        with st.spinner('Creating...'):
            if not is_pdf(file.name):
                return st.warning('Only pdf files accepted')

            if not chat_name:
                chat_name = convert_collection_name_to_valid(file.name)

            is_valid, message = validate_collection_name(chat_name)

            if not is_valid:
                return st.warning(message)

            try:
                temp_file = save_as_temp_file(file)
                tf_path = temp_file.name

                VectorStore.add_pdf(chat_name, tf_path)
                st.success('File added succesfully!')

                delete_file(tf_path)
            except Exception as e:
                print(e)
                st.warning('An error ocurred')

        st.rerun()


@st.dialog('Delete current chat')
def delete_current_chat(collection):
    st.write(f'Are you sure you want to delete "{collection}"?')

    _, col2, col3 = st.columns([5, 1, 1])

    if col2.button('Yes', type='primary'):
        with st.spinner('Deleting...'):
            VectorStore.delete_collection(collection)
        st.rerun()

    if col3.button('No'):
        st.rerun()


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
