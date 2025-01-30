# import streamlit as st

# # Set the page configuration for blue and white theme
# st.set_page_config(page_title="AI Powered Documentation Generator", page_icon=":book:", layout="wide")

# # Set the heading
# st.title("AI Powered Documentation Generator")

# # Create a two-column layout
# col1, col2 = st.columns([1, 2])
# st.divider()

# # Left column: Dropdown for Python and Java
# with col1:
#     language = st.selectbox("Select Programming Language", ["Python", "Java"])

# # Right column: File upload section with drag-and-drop
# with col2:
#     st.header("Upload File")
#     uploaded_file = st.file_uploader("Browse or Drag & Drop a file", type=["txt", "pdf", "docx"])

# # Checkbox for "Generate overall document"
# generate_doc = st.checkbox("Generate overall document")

# # Submit button to trigger different functions based on the checkbox state
# if st.button("Submit"):
#     if generate_doc:
#         # Call function for generating overall document
#         st.write("Function to generate overall document called.")
#         # (Add your function here)
#     else:
#         # Call function for other task
#         st.write("Function for other task called.")
#         # (Add your other function here)



# import streamlit as st

# # Set the page configuration for blue and white theme
# st.set_page_config(page_title="AI Powered Documentation Generator", page_icon=":book:", layout="wide")

# # Apply custom styling for blue and white theme
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f0f8ff;
#     }
#     .stButton>button {
#         background-color: #007BFF;
#         color: white;
#         border-radius: 5px;
#     }
#     .stSelectbox, .stCheckbox {
#         border: 1px solid #007BFF;
#         padding: 5px;
#         border-radius: 5px;
#     }
#     .stFileUploader {
#         border: 2px dashed #007BFF;
#         padding: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Set the heading
# st.title("AI Powered Documentation Generator")

# # Create a three-column layout (left panel, separator, right panel)
# col1, col_sep, col2 = st.columns([1, 0.05, 2])

# # Left column: Dropdown, Checkbox, and Submit button
# with col1:
#     st.markdown("### Settings")
#     language = st.selectbox("Select Programming Language", ["Python", "Java"])
#     generate_doc = st.checkbox("Generate overall document")

#     if st.button("Submit"):
#         if generate_doc:
#             st.write("Function to generate overall document called.")
#             # Call your function here
#         else:
#             st.write("Function for other task called.")
#             # Call your other function here

# # Middle column: Vertical separator
# with col_sep:
#     st.markdown(
#         """<div style='border-left: 3px solid #007BFF; height: 100vh;'></div>""",
#         unsafe_allow_html=True
#     )

# # Right column: File upload section takes the whole right side
# with col2:
#     st.markdown("### Upload File")
#     uploaded_file = st.file_uploader("Browse or Drag & Drop a file", type=["txt", "pdf", "docx"])
# import streamlit as st

# # Set the page configuration
# st.set_page_config(page_title="AI Powered Documentation Generator", page_icon=":book:", layout="wide")

# # Apply custom styling for blue background and white text
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #007BFF;
#         color: white;
#     }
#     .stApp {
#         background-color: #404E61;
#         color: white;
#     }
#     .stButton>button {
#         background-color: white;
#         color: black;
#         border: 2px dashed white;
#         font-weight: bold;
#         margin-top: 10px;
#     }
#     .stSelectbox, .stCheckbox {
#         border: 2px dashed white;
#         padding: 5px;
#         border-radius: 5px;
#         color: white;
#         background-color: #413C58;
#     }
#     .stFileUploader {
#         border: 2px dashed white;
#         padding: 10px;
#         color: #413C58;
#         background-color: #413C58;
#     }
#     .stMarkdown {
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Set the heading
# st.title("AI Powered Documentation Generator")

# # Create a three-column layout (left panel, separator, right panel)
# col1, col_sep, col2 = st.columns([3, 0.05, 5])

# # Left column: Dropdown, Checkbox, and Submit button
# with col1:
#     st.markdown("### Settings", unsafe_allow_html=True)
#     language = st.selectbox("Select Programming Language", ["Python", "Java"])
#     generate_doc = st.checkbox("Generate overall document")

#     if st.button("Submit"):
#         if generate_doc:
#             st.write("Function to generate overall document called.")
#             # Call your function here
#         else:
#             st.write("Function for other task called.")
#             # Call your other function here

# # Middle column: Vertical separator
# with col_sep:
#     st.markdown(
#         """<div style='border-left: 3px solid white; height: 60vh;'></div>""",
#         unsafe_allow_html=True
#     )

# # Right column: File upload section takes the whole right side
# with col2:
#     st.markdown("### Upload File", unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("Browse or Drag & Drop a file", type=["txt", "pdf", "docx"])

import streamlit as st

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

    # Download Button
    if st.button("Download"):
        st.success("Download function triggered.")  # Placeholder for download logic

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
            else:
                st.success("Function for other task called.")  # Placeholder
