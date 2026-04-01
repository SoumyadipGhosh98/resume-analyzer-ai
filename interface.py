import streamlit as st
from analysis import analyze_resume

# App Page Basic Config
st.set_page_config(page_title='Resume Analzysis Using AI',page_icon='📝🔎',layout='wide')
st.title("🤖 AI Assistant for :blue[Resume Analysis]")
st.subheader(f''' AI Powered Resume Analyzer based on the given Designation and Job Description using Gemini Model''',divider=True)


# Adding upload in the side bar
st.sidebar.subheader('Drop Your Resume Here 📝')
pdf_doc=st.sidebar.file_uploader('Click here to browse',type=['pdf'])

job_des = st.text_area(
    'Copy and paste the JD here',
    max_chars=10000
)

submit = st.button('Generate Results 📊')

if submit:
    with st.spinner('Getting Results....'):
        analyze_resume(pdf_doc,job_des)