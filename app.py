import ollama
import streamlit as st

from PIL import Image

# Page configuration
st.set_page_config(
    page_title='snap-to-typst',
    page_icon='typ.png',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title('SNAP TO TYPST')
col1, col2 = st.columns(2)

# HELPER FUNCTION TO FETCH DATA


def fetch_data(type):

    if type == 'image':
        with open('eq.txt', 'r') as file:
            img_eq = file.read()
        message = {
            'role': 'user',
            'content': img_eq,
            'images': [uploaded_image.getvalue()]
        }
    else:
        with open('bib.txt', 'r') as file:
            url_bib = file.read()
        message = {
            'role': 'user',
            'content': url_bib
        }

    result = ollama.chat(
        model='llama3.2-vision',
        messages=[message]
    )
    return result


# COLUMN 1: EQUATION PARSER
with col1:
    st.subheader('Equation Parser')
    uploaded_image = st.file_uploader(
        'Upload an image:', type=['jpg', 'jpeg', 'png']
        )

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_container_width=True)

    if st.button('Parse', use_container_width=True):
        with st.spinner('Fetching description...'):
            try:
                result = fetch_data('image')
                st.write(result['message']['content'])
            except Exception as e:
                st.write('Error occurred:', e)

# COLUMN 2: URL DESCRIPTION
with col2:
    st.subheader('URL Bibliography Fetcher')
    url = st.text_input('Enter a URL:', '')

    if st.button('Hayagriva Compatible Entry', use_container_width=True):
        with st.spinner('Fetching description...'):
            try:
                result = fetch_data('url')
                st.write(result['message']['content'])
            except Exception as e:
                st.write('Error occurred:', e)

if st.button('Clear', use_container_width=False):
    st.session_state['uploaded_image'] = ''
    st.session_state['url'] = ''
