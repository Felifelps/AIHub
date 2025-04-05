from ai.rag.vector_store import VectorStore
import streamlit as st


@st.dialog('Delete current chat')
def delete_current_chat(collection):
    st.write(f'Are you sure you want to delete "{collection}"?')

    _, col2, col3 = st.columns([5, 1, 1])

    if col2.button('Yes', type='primary'):
        with st.spinner('Deleting...'):
            VectorStore.delete_collection(collection)
            del st.session_state.messages[collection]
        st.rerun()

    if col3.button('No'):
        st.rerun()
