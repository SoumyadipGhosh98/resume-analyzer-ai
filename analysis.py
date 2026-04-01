import streamlit as st
import os
import google.generativeai as genai

import warnings
from warnings import filterwarnings

from pdf import extractpdf # refers to pdf.py

from dotenv import load_dotenv
load_dotenv()


key = os.getenv('Google_API_Key')
genai.configure(api_key=key)

model =genai.GenerativeModel('gemini-2.5-flash')


def analyze_resume(pdf_doc,job_des):
    
    if pdf_doc is not None:
        pdf_text=extractpdf(pdf_doc) # class in pdf.py will run
        st.write('Extracted Successfully ✅')
    else:
        st.warning(':red[Error] 🔴 Extraction Failed')
        

    ats_score = model.generate_content(
        f"""
    Compare resume {pdf_text} with job description {job_des} and give ATS score (0–100).

    Output:
    - ATS Score: XX/100
    - 5 bullet points:
    • Strengths
    • Gaps
    - Matched Keywords: []
    - Missing Keywords: []
    - 3 improvement suggestions
    """
    )

    prob_score = model.generate_content(
        f"""
    Compare resume {pdf_text} with job description {job_des} and estimate selection probability (0–100%).

    Output:
    - Selection Probability: XX%
    - 5 bullet points:
    • Strengths
    • Weaknesses
    - 2 risk factors
    - 3 improvement suggestions
    - Verdict: High / Medium / Low
    """
    )

    good_fit = model.generate_content(
        f"""
    Compare resume {pdf_text} with job description {job_des} and determine fit.

    Output:
    - Fit Status: Good Fit / Moderate Fit / Not a Good Fit
    - 5 bullet points:
    • Strengths
    • Weaknesses
    - Missing Skills/Keywords: []
    - 3 improvement suggestions
    """
    )

    swot_analysis = model.generate_content(
        f"""
    Analyze resume {pdf_text} and provide SWOT analysis.

    Output:
    - Strengths: (2–3 points)
    - Weaknesses: (2–3 points)
    - Opportunities: (2 points)
    - Threats: (2 points)
    """
    )
    
    return {
        st.write(ats_score.text),
        st.write(prob_score.text),
        st.write(good_fit.text),
        st.write(swot_analysis.text)
    }

