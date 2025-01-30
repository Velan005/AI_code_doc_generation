import os
import streamlit as st

# Ensure the output directory exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_file(content, file_name, file_type):
    """
    Saves content to a specified file type and provides a download button.
    """
    if not content.strip():
        st.error("Error: The content is empty!")
        return

    file_path = os.path.join(OUTPUT_DIR, file_name)

    # Save the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    # Define MIME types for different file formats
    mime_types = {
        "py": "text/x-python",
        "java": "text/x-java-source",
        "cpp": "text/x-c++src",
        "c": "text/x-c",
        "js": "application/javascript",
        "html": "text/html",
        "css": "text/css",
        "txt": "text/plain",
        "md": "text/markdown",
        "pdf": "application/pdf"
    }

    mime_type = mime_types.get(file_type, "application/octet-stream")  # Default to binary

    # Provide a download button
    with open(file_path, "rb") as file:
        st.download_button(
            label=f"Download {file_type.upper()} File",
            data=file,
            file_name=file_name,
            mime=mime_type
        )

# Streamlit UI
st.title("🔹 Code & Documentation Downloader")

# Choose file type: Code or Documentation
file_category = st.radio("📂 Select file type:", ["Code", "Documentation"])

# Input text area
content = st.text_area("📝 Enter your content here:", "print('Hello, World!')")

if file_category == "Code":
    file_extension = st.selectbox("🛠 Select code format:", ["py", "java", "cpp", "c", "js", "html", "css"])
    file_name = f"generated_code.{file_extension}"
else:
    file_extension = st.selectbox("📄 Select document format:", ["txt", "md", "pdf"])
    file_name = f"documentation.{file_extension}"

# Button to save and download file
if st.button("💾 Save & Download"):
    save_file(content, file_name, file_extension)
