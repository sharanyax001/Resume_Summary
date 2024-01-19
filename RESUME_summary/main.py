import streamlit as st
import pandas as pd
import joblib
import pickle
import os


def save_data_to_file(data):
    # Save the data to the "training_data.csv" file
    if os.path.isfile('training_data.csv'):
        data.to_csv('training_data.csv', mode='a', header=False, index=False)
    else:
        data.to_csv('training_data.csv', index=False)


def train_model(data):

    pass


def main():
    global saved_data

    saved_data = pd.DataFrame(columns=['Text', 'Label'])

    st.title('Text Annotation and Model Training')

    # Text input for the paragraph

    text = st.text_area('Enter the paragraph')

    # Dropdown menu for selecting portions of the text

    selected_labels = []
    selected_texts = []
    num_selections = st.number_input(
        'Number of selections', min_value=1, max_value=10, value=1, step=1)

    for i in range(num_selections):
        selected_text = st.text_input(f'Selection {i+1}')
        label = st.selectbox(f'Label for Selection {i+1}', [
                             'Years of Experience', 'Previous Company', 'Applied for', 'Field of Expertise'])
        selected_labels.append(label)
        selected_texts.append(selected_text)

    # Button to save the selected data

    if st.button('Save Data'):
        new_data = pd.DataFrame(
            {'Text': selected_texts, 'Label': selected_labels})
        saved_data = pd.concat([saved_data, new_data], ignore_index=True)
        save_data_to_file(saved_data)
        st.success('Data saved successfully!')

        # Display the saved data queue

        st.header('Saved Data')
        st.dataframe(saved_data)

    # Button to train the model

    if st.button('Train Model'):
        data = pd.read_csv('training_data.csv')
        train_model(data)
        blank_model = "blank_model.pkl"
        st.success('Model trained successfully!'.format(blank_model))


LrdetectFile = open('blank_model.pkl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

if __name__ == '__main__':
    main()
