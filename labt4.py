import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt_tab")
nltk.download('punkt', quiet=True)


st.set_page_config(page_title="Text Chunking Demo (NLTK)", layout="wide")
st.title("Text Chunking with NLTK Sentence Tokenizer")


st.write(
    "This app allows you to upload a PDF file and perform semantic text chunking using NLTK's sentence tokenizer."
)


uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
  
    reader = PdfReader(uploaded_file)
    full_text = ""
    
   
    for page in reader.pages:
        full_text += page.extract_text()
    
  
    text_sample = full_text[58:68]
    st.subheader("Extracted Text Sample (Indices 58 to 68):")
    st.write(text_sample)

   
    sentences = sent_tokenize(full_text)
    
  
    st.subheader("Text after Sentence Tokenization:")
    st.write(sentences[:5])  # Display first 5 sentences as a preview
    
  
    if st.button("Apply Sentence Chunking"):
        if not full_text.strip():
            st.warning("Please upload a valid PDF with text content.")
        else:
            st.subheader("Semantic Sentence Chunking:")
            st.write(sentences)
            
        
            for i, sentence in enumerate(sentences):
                st.write(f"Sentence {i + 1}: {sentence}")
