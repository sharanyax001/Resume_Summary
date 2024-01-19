import streamlit as st
import spacy
import pickle
# Load the NER model
with open('blank_model.pkl', 'rb') as file:
    Trained_model = pickle.load(file)
# Function to extract information from resume summary


def extract_information(summary):
    doc = Trained_model(summary)
    years_of_experience = None
    previous_company = None
    company_applied_for = None
    field_of_expertise = None
    for ent in doc.ents:
        if ent.label_ == 'YEARS':
            years_of_experience = ent.text
        elif ent.label_ == 'COMPANY':
            if previous_company is None:
                previous_company = ent.text
            else:
                company_applied_for = ent.text
        elif ent.label_ == 'FIELD':
            field_of_expertise = ent.text
    return years_of_experience, previous_company, company_applied_for, field_of_expertise
# Streamlit UI


def main():
    st.title("Resume Summary Information Extraction")
    st.write("Enter your resume summary below:")
    # Text input
    summary = st.text_area("Resume Summary")
    if st.button("Extract Information"):
        # Check if summary is provided
        if summary.strip() != "":
            # Extract information
            years_of_experience, previous_company, company_applied_for, field_of_expertise = extract_information(
                summary)
            # Display extracted information
            st.write("Years of Experience:", years_of_experience)
            st.write("Previous Company:", previous_company)
            st.write("Company Applied For:", company_applied_for)
            st.write("Field of Expertise:", field_of_expertise)
        else:
            st.error("Please enter a resume summary.")


# Run the Streamlit app
if __name__ == '__main__':
    main()
