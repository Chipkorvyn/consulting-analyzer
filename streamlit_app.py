# First version of our consulting analyzer
import streamlit as st

# Basic app settings
st.set_page_config(page_title="Consulting Document Analyzer")

# Title and description
st.title("Consulting Document Analyzer")
st.write("Upload your consulting documents for quick analysis")

# Input section
doc_text = st.text_area("Paste your consulting document here:", height=200)

# Document type selection
doc_type = st.selectbox(
    "Select document type",
    ["Meeting Notes", "Strategy Document", "Project Plan", "Client Report"]
)

# Analysis button
if st.button("Analyze Document"):
    if doc_text:
        # Basic analysis
        word_count = len(doc_text.split())
        paragraph_count = len(doc_text.split('\n\n'))
        
        # Display results
        st.subheader("Basic Analysis")
        st.write(f"Document Type: {doc_type}")
        st.write(f"Word Count: {word_count}")
        st.write(f"Paragraph Count: {paragraph_count}")
        
        # Display a sample "advanced" metric
        st.write("Complexity Score:", len(set(doc_text.split())) / word_count)
    else:
        st.warning("Please enter some text to analyze")
