import streamlit as st
import re

# Basic app settings
st.set_page_config(page_title="Consulting Document Analyzer", layout="wide")

# Title and description
st.title("Consulting Document Analyzer")

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input section
    doc_text = st.text_area("Paste your consulting document here:", height=300)
    
    # Document type selection with descriptions
    doc_type = st.selectbox(
        "Select document type",
        ["Meeting Notes", "Strategy Document", "Project Plan", "Client Report"]
    )

    # Add some basic settings
    with st.expander("Analysis Settings"):
        min_keyword_length = st.slider("Minimum keyword length", 3, 10, 4)
        show_detailed_stats = st.checkbox("Show detailed statistics", True)

# Analysis button
if st.button("Analyze Document"):
    if doc_text:
        with col2:
            st.subheader("Analysis Results")
            
            # Basic metrics
            word_count = len(doc_text.split())
            paragraph_count = len(doc_text.split('\n\n'))
            
            # More advanced analysis
            sentences = re.split('[.!?]+', doc_text)
            avg_sentence_length = word_count / len(sentences) if sentences else 0
            
            # Extract potential keywords (simple version)
            words = re.findall(r'\b\w+\b', doc_text.lower())
            keywords = [word for word in set(words) 
                       if len(word) >= min_keyword_length 
                       and word.isalnum()]
            
            # Display results
            st.metric("Word Count", word_count)
            st.metric("Paragraph Count", paragraph_count)
            st.metric("Average Sentence Length", f"{avg_sentence_length:.1f}")
            
            if show_detailed_stats:
                st.subheader("Key Terms")
                st.write(", ".join(sorted(keywords)[:10]))
                
                st.subheader("Document Structure")
                st.progress(min(1.0, avg_sentence_length/20))
                st.caption("Sentence Complexity")
    else:
        st.warning("Please enter some text to analyze")

# Add a footer with version info
st.markdown("---")
st.caption("v0.1 - Basic Analysis Version")
