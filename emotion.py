import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download necessary data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define positive and negative word lists
positive_words = ['happy', 'joy', 'love', 'excellent', 'good', 'amazing', 'wonderful', 'great', 'fantastic', 'positive']
negative_words = ['sad', 'hate', 'angry', 'bad', 'terrible', 'awful', 'horrible', 'negative', 'worse', 'poor']

def analyze_sentiment(statement):
    # Tokenize and POS tagging
    tokens = word_tokenize(statement.lower())
    tagged_words = pos_tag(tokens)

    # Analyze sentiment
    pos_count = sum(1 for word, tag in tagged_words if word in positive_words)
    neg_count = sum(1 for word, tag in tagged_words if word in negative_words)

    # Determine sentiment
    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment

# Function to decode file content
def decode_file(file_content):
    try:
        return file_content.decode("utf-8")  # Attempt to decode as UTF-8
    except UnicodeDecodeError:
        try:
            return file_content.decode("ISO-8859-1")  # Fallback to ISO-8859-1
        except UnicodeDecodeError:
            return file_content.decode("latin-1")  # Fallback to latin-1

# URL of the background image
background_image_url = "https://images.pexels.com/photos/3184638/pexels-photo-3184638.jpeg"

# Streamlit app styling
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .header {{
        font-size: 40px;
        color: blue;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }}
    .result {{
        font-size: 18px;
        margin-top: 20px;
        font-weight: bold;
        color: blue;
    }}
    .blue-text {{
        color: blue;
        font-size: 20px;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Title of the web app
st.markdown("<div class='header'>Sentiment Analysis</div>", unsafe_allow_html=True)

# First Section: Text input for word/phrase
st.markdown("<div class='blue-text'>Enter a word or phrase:</div>", unsafe_allow_html=True)
user_input = st.text_input("")

if user_input:
    sentiment_result = analyze_sentiment(user_input)
    st.markdown(f"<div class='result'>Sentiment: {sentiment_result}</div>", unsafe_allow_html=True)

# Second Section: File upload for sentiment analysis
st.markdown("<div class='blue-text'>Upload a Text File:</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("<div class='blue-text'>Upload your text file for sentiment analysis:</div>", type=["txt"], label_visibility="hidden")

if uploaded_file is not None:
    try:
        # Read the file content and decode
        file_content = uploaded_file.read()
        decoded_text = decode_file(file_content)
        
        # Display the content
        st.text("File content:")
        st.text(decoded_text)
        
        # Analyze the file content sentiment
        sentiment_result = analyze_sentiment(decoded_text)
        st.markdown(f"<div class='result'>Sentiment of the file: {sentiment_result}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error reading file: {e}")
