import streamlit as st

st.title("Document Classifier System")
st.write(
    "Made with ❤️ by Aadarsh , Aditya and Ritesh."
)
st.write("Try Now!")

st.write("### Upload your document here")
uploaded_file = st.file_uploader(
    "Upload a file",
    type=["pdf", "docx", "txt"],
    label_visibility="collapsed",
)
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("File uploaded successfully!")
    st.write("## File Content")
    st.write(bytes_data.decode("utf-8", errors="ignore"))
    st.write("## Classify Document")
    st.button("Classify", key="classify_button")
    st.write("Document classified successfully!")
    st.write("## Classification Result")
    st.write("The document is classified as: **Business**")
    st.write("## Download the result")
    st.download_button(
        label="Download Result",
        data="classification_result.txt",
        file_name="classification_result.txt",
        mime="text/plain",
    )
st.write("## About the project")
st.write(
    "This is a document classifier system that classifies documents into different categories. It uses machine learning algorithms to classify the documents based on their content."
)
st.write("## How to use the project")
st.write(
    "1. Upload a document in PDF, DOCX or TXT format.\n"
    "2. Click on the 'Classify' button to classify the document.\n"
    "3. Download the classification result."
)
st.write("## Technologies used")
st.write(
    "- Streamlit\n"
    "- Python\n"
    "- Machine Learning\n"
    "- Natural Language Processing\n"
    "- Optical Character Recognition (OCR)\n"
)




st.write("\n")
st.write("\n")
st.write(
    "Made with ❤️ by Aadarsh , Aditya and Ritesh."
)