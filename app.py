import streamlit as st
import json

st.title("🏦 BFSI Call Center AI Assistant")
st.write("AI assistant for loan, EMI and banking queries")

# Load dataset
with open("bfsi_dataset.json") as f:
    data = json.load(f)

questions = [item["question"].lower() for item in data]
answers = [item["answer"] for item in data]


st.markdown("### Ask your banking question:")

query = st.text_input("Type here and press Enter")

if query:
    found = False
    
    for i, q in enumerate(questions):
        if q in query.lower():
            st.success(answers[i])
            found = True
            break
    
    if not found:
        st.warning("This is a demo AI response. Please contact bank support for exact details.")

    if "account number" in query.lower():
        st.error("Cannot access personal account details. Contact official bank support.")
