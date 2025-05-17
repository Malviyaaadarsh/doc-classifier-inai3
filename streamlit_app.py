import streamlit as st
st.set_page_config(page_title="Document Classifier System", page_icon=":guardsman:", initial_sidebar_state="expanded",layout="wide")
st.title("Document Classifier System")

st.caption("\n ## [ Model still under development by Air labs. ][Stay Tuned!]  \n")

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
    ('Bills', 'Resume', 'Notices','Business','Technical','Legal','Reseach Paper','Invoice','Others'),
    label_visibility="collapsed",horizontal=True)
if genre != 'Others':
    st.markdown('You selected '+ genre)
else:
    st.write("You select others. Please specify the type of document you usually deal with.")
    st.text_input("Please specify the type of document you usually deal with.", key="other_genre")
    
st.markdown("#### About")
st.markdown(
    "This is a document classifier system that classifies documents into different categories. It uses machine learning algorithms to classify the documents based on their content. \n "
    "The system is designed to help users quickly classify documents and save time in the process. \n"
    "The system is still under development and will be updated with more features in the future.\n"
    "The system is designed to be user-friendly and easy to use. Users can upload documents in different formats and get the classification result in a few clicks.\n"
)
st.markdown("#### How to use this App")
st.markdown(
    "- Upload a document in PDF, DOCX or TXT format.\n"
    "- Click on the 'Classify' button to classify the document.\n"
    "- Download the classification result."
)



st.markdown("\n")
st.markdown(
    "#### Disclaimer"
)
st.markdown(
    "This is a prototype of a document classifier system. The classification results may not be accurate and should not be used for any critical decision making. \n"
    "The App store no information of the User and doesn't ask for any permission. \n"
)
st.caption(
    "#### Made with ❤️ by Aadarsh , Aditya and Ritesh."
)