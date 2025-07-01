# Sentiment Analysis

This project uses an LSTM-based neural network to classify movie reviews from the IMDb dataset as **Positive** or **Negative**.

## Project Overview

- **Dataset**: IMDb movie reviews (from Keras)
- **Model**: Embedding + LSTM + Dense
- **Framework**: TensorFlow/Keras
- **Accuracy**:
  - Training: ~93%
  - Validation: ~87%
- **Platform**: Google Colab

 **How to Run This Project (Locally)**
Step 1: Install Python & Dependencies
Then install the required packages:
pip install tensorflow numpy

Step 2: Place Files in One Folder
Ensure the following files are in the same folder:
sentiment_model.h5
tokenizer.pkl
predict.py

Step 3: Run the Sentiment Prediction Script
Open a terminal or command prompt, navigate to your folder:

Step 4: Input Text to Predict Sentiment
Enter a review (or 'exit'):
Type something like:
The movie was really good!
And the model will respond:

Sentiment: Positive 😊 



