import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
model = load_model('sentiment_model.h5')
with open('tokenizer.pkl', 'rb') as f:
    word_index = pickle.load(f)

# Preprocessing function
def preprocess(text, max_len=200):
    words = text.lower().split()
    seq = [word_index.get(word, 0) for word in words]
    return pad_sequences([seq], maxlen=max_len)

# Predict function
def predict_sentiment(text):
    input_seq = preprocess(text)
    prediction = model.predict(input_seq)[0][0]
    return "Positive 😊" if prediction > 0.5 else "Negative 😞"

# Run example
if __name__ == "__main__":
    while True:
        user_input = input("Enter a review (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
        print("Sentiment:", predict_sentiment(user_input))
