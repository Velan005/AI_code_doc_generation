import streamlit as st
from new_file.part3 import chain
import prompt
from new_file.part3 import vectordb
from downloader import save_file  # Import the save_file function from downloader.py
vectordatabase = vectordb.initialize_chroma()
# Set the page configuration
st.set_page_config(page_title="AI Powered Documentation Generator", page_icon=":book:", layout="wide")

# Apply custom styling for blue background and white text
st.markdown(
    """
    <style>
    body {
        background-color: #007BFF;
        color: white;
    }
    .stApp {
        background-color: #404E61;
        color: white;
    }
    .stButton>button {
        background-color: white;
        color: black;
        border: 2px dashed white;
        font-weight: bold;
        margin-top: 10px;
    }
    .stSelectbox, .stCheckbox {
        border: 2px dashed white;
        padding: 5px;
        border-radius: 5px;
        color: white;
        background-color: #413C58;
    }
    .stFileUploader {
        border: 2px dashed white;
        padding: 10px;
        color: white;
        background-color: #413C58;
    }
    .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the heading
st.title("AI Powered Documentation Generator")

# Create a three-column layout (left panel, separator, right panel)
col1, col_sep, col2 = st.columns([3, 0.05, 5])

# Left column: Dropdown, Checkbox, and Buttons
with col1:
    st.markdown("### Settings", unsafe_allow_html=True)
    language = st.selectbox("Select Programming Language", ["Python", "Java"])
    generate_doc = st.checkbox("Generate overall document")

    # Download Button (trigger download logic from downloader.py)
    if st.button("Download"):
        # Placeholder for content to be downloaded
        content = "Sample content for download..."  # Replace this with the content to be downloaded
        file_name = f"generated_code.{language.lower()}"  # Example: generated_code.py or generated_code.java
        save_file(content, file_name, language.lower())  # Call the save_file function from downloader.py

# Middle column: Vertical separator
with col_sep:
    st.markdown(
        """<div style='border-left: 3px solid white; height: 65vh;'></div>""",
        unsafe_allow_html=True
    )

# Right column: File upload section takes the whole right side
with col2:
    st.markdown("### Upload File", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Browse or Drag & Drop a file", type=["txt", "pdf", "docx"])

    if uploaded_file is not None:
        st.success("File processed successfully!")

    # Submit Button Logic
    if st.button("Submit"):
        if uploaded_file is None:

            st.error("File not uploaded")  # Show error if no file is uploaded
        else:
            if generate_doc:
                st.success("Function to generate overall document called.")  # Placeholder
                respose = chain.generate_code_rag_chain(language, "Generate overall document",vectordatabase)
            else:
                st.success("Function for other task called.")  # Placeholder
                respose = chain.generate_code_chain(language, "Other task")
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)