import streamlit as st
import os

def download_code(file_path):
    """Downloads the generated code file, supporting multiple programming languages."""
    if not os.path.exists(file_path):
        st.error("File not found! Please generate the code first.")
        return

    file_name = os.path.basename(file_path)
    file_extension = file_name.split(".")[-1]

    mime_types = {
        "py": "text/x-python",
        "java": "text/x-java-source",
        "cpp": "text/x-c++src",
        "c": "text/x-c",
        "js": "application/javascript",
        "html": "text/html",
        "css": "text/css",
        "txt": "text/plain"
    }

    mime_type = mime_types.get(file_extension, "application/octet-stream")  # Default binary type

    with open(file_path, "rb") as file:
        st.download_button(
            label=f"Download {file_extension.upper()} Code",
            data=file,
            file_name=file_name,
            mime=mime_type
        )

def download_document(file_path):
    """Downloads the documentation file (TXT, MD, PDF, etc.)."""
    if not os.path.exists(file_path):
        st.error("File not found! Please generate the documentation first.")
        return

    file_name = os.path.basename(file_path)
    file_extension = file_name.split(".")[-1]

    mime_types = {
        "txt": "text/plain",
        "md": "text/markdown",
        "pdf": "application/pdf"
    }

    mime_type = mime_types.get(file_extension, "application/octet-stream")  # Default binary type

    with open(file_path, "rb") as file:
        st.download_button(
            label=f"Download {file_extension.upper()} Documentation",
            data=file,
            file_name=file_name,
            mime=mime_type
        )
