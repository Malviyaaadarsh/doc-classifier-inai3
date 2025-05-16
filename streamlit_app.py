import streamlit as st

st.title("Document Classifier System")

st.caption("\n #### [ Model still under development by Air labs. ][Stay Tuned!]  \n")

st.markdown("#### Upload your document here")
uploaded_file = st.file_uploader(
    "Upload a file",
    type=["pdf", "docx", "txt","xls"],
    label_visibility="collapsed",
)
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.caption("File uploaded!")
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
st.markdown(" Select the type of document you usually deal with")  
genre = st.radio(
    "What type of document you usually deal with ? ",
    ('Bills', 'Resume', 'Notices','Business','Technical','Legal','Reseach Paper','Others'),
    label_visibility="collapsed",)
if genre != 'Others':
    st.markdown('You selected '+ genre)
else:
    st.write("You select others. Please specify the type of document you usually deal with.")
    st.text_input("Please specify the type of document you usually deal with.", key="other_genre")
    
st.markdown("#### About the project")
st.markdown(
    "This is a document classifier system that classifies documents into different categories. It uses machine learning algorithms to classify the documents based on their content."
)
st.markdown("#### How to use the project")
st.markdown(
    "- Upload a document in PDF, DOCX or TXT format.\n"
    "- Click on the 'Classify' button to classify the document.\n"
    "- Download the classification result."
)
st.markdown("#### Technologies used")
st.markdown(
    "- Streamlit\n"
    "- Python\n"
    "- Machine Learning\n"
    "- Natural Language Processing\n"
    "- Optical Character Recognition (OCR)\n"
)




st.markdown("\n")
st.markdown("\n")
st.markdown(
    "Made with ❤️ by Aadarsh , Aditya and Ritesh."
)