import streamlit as st
import PyPDF2
import re

def extract_education_from_text(text):
    education_section = re.search(r'EDUCATION\s*([\s\S]*?)(?=WORK HISTORY|$)', text)
    if education_section:
        return education_section.group(1).strip()
    return None

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title('Resume Education Extractor')

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        education_info = extract_education_from_text(resume_text)

        if education_info:
            st.header("Education Details:")
            st.text_area("Extracted Education", value=education_info, height=300)
        else:
            st.warning("No education details found in the resume.")

if __name__ == "__main__":
    main()
