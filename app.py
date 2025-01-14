import streamlit as st
import tempfile
import os
from pathlib import Path
from markitdown import convert_to_markdown
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment variables
MAX_UPLOAD_SIZE = int(os.getenv('MAX_UPLOAD_SIZE', 5)) * 1024 * 1024  # Convert MB to bytes

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary directory and return the path"""
    try:
        # Check file size
        if len(uploaded_file.getvalue()) > MAX_UPLOAD_SIZE:
            raise ValueError(f"File size exceeds the maximum limit of {MAX_UPLOAD_SIZE/(1024*1024)}MB")
            
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

def create_download_link(markdown_content, filename):
    """Create a download link for the markdown file"""
    b64 = base64.b64encode(markdown_content.encode()).decode()
    return f'<a href="data:text/markdown;base64,{b64}" download="{filename}.md">Download Markdown File</a>'

def main():
    st.title("Document to Markdown Converter")
    st.write("""
    Convert your documents to Markdown format using Microsoft's markitdown library.
    Supported formats include: DOCX, PDF, HTML, and more.
    """)

    # Display max upload size
    st.info(f"Maximum file size: {MAX_UPLOAD_SIZE/(1024*1024)}MB")

    # File upload
    uploaded_file = st.file_uploader(
        "Choose a document to convert", 
        type=["docx", "pdf", "html", "txt", "rtf"]
    )

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        
        # Save the uploaded file temporarily
        temp_path = save_uploaded_file(uploaded_file)
        
        if temp_path:
            try:
                # Convert to markdown
                with st.spinner("Converting document to Markdown..."):
                    markdown_content = convert_to_markdown(temp_path)
                
                # Display preview
                st.subheader("Markdown Preview")
                st.text_area("", markdown_content, height=300)
                
                # Create download button
                output_filename = Path(uploaded_file.name).stem
                st.markdown(
                    create_download_link(markdown_content, output_filename),
                    unsafe_allow_html=True
                )
                
                # Cleanup
                os.unlink(temp_path)
                
            except Exception as e:
                st.error(f"Error converting file: {str(e)}")
                if temp_path:
                    os.unlink(temp_path)

    # Add information about supported formats
    with st.expander("Supported Formats Information"):
        st.write("""
        This converter supports the following input formats:
        - Microsoft Word Documents (.docx)
        - PDF Documents (.pdf)
        - HTML Files (.html)
        - Text Files (.txt)
        - Rich Text Format (.rtf)
        
        The output will be a clean, well-formatted Markdown file.
        """)

if __name__ == "__main__":
    main()