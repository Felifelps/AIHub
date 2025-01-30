import re
import streamlit as st


def validate_collection_name(collection_name):
    length = len(collection_name)

    if length > 63 or length < 3:
        return False, 'Must contain 3-63 characters'

    if collection_name in st.session_state.current_collections:
        return False, 'This name is already in use'

    if not (collection_name[0].isalnum() and collection_name[-1].isalnum()):
        return False, 'Must start and end with an alphanumeric character'

    if re.findall(r"[^a-zA-Z0-9_-]", collection_name):
        return False, 'Must contain only alphanumerical characters, hyphens (-) or underscores (_)'

    return True, None


def convert_collection_name_to_valid(collection_name):
    collection_name = re.sub(r"[^a-zA-Z0-9_-]", "", collection_name)
    original_name = collection_name
    count = 1
    while collection_name in st.session_state.current_collections:
        collection_name = f"{original_name}-{count}"
        count += 1
    return collection_name
