import streamlit as st
from transformers import pipeline

# Load the model outside the main function
emotion_pipeline = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')

# Function to provide explanations for emotion labels and sentiment scores
def explain_emotion(label, score):
    emotion_explanations = {
        'admiration': 'You are expressing admiration or respect.',
        'amusement': 'You are feeling amused or entertained.',
        'anger': 'You are expressing anger or frustration.',
        'annoyance': 'You are feeling annoyed or irritated.',
        'approval': 'You are expressing approval or agreement.',
        'caring': 'You are feeling caring or affectionate.',
        'confusion': 'You are feeling confused or perplexed.',
        'curiosity': 'You are curious or inquisitive.',
        'desire': 'You are expressing desire or longing.',
        'disappointment': 'You are feeling disappointed or let down.',
        'disapproval': 'You are expressing disapproval or disagreement.',
        'disgust': 'You are feeling disgusted or repulsed.',
        'embarrassment': 'You are embarrassed or self-conscious.',
        'excitement': 'You are feeling excited or thrilled.',
        'fear': 'You are feeling fear or anxiety.',
        'gratitude': 'You are expressing gratitude or thankfulness.',
        'grief': 'You are experiencing grief or sorrow.',
        'joy': 'You are feeling joyful and happy.',
        'love': 'You are expressing love or affection.',
        'nervousness': 'You are feeling nervous or anxious.',
        'optimism': 'You are optimistic or hopeful.',
        'pride': 'You are feeling proud or accomplished.',
        'realization': 'You are having a realization or epiphany.',
        'relief': 'You are feeling relieved or comforted.',
        'remorse': 'You are feeling remorse or regret.',
        'sadness': 'You are experiencing sadness or sorrow.',
        'surprise': 'You are expressing surprise or astonishment.',
        'neutral': 'Your emotion is relatively neutral or mixed.',
        }

    sentiment_mapping = {
        'admiration': 'LABEL_5',
        'amusement': 'LABEL_5',
        'anger': 'LABEL_1',
        'annoyance': 'LABEL_2',
        'approval': 'LABEL_5',
        'caring': 'LABEL_5',
        'confusion': 'LABEL_3',
        'curiosity': 'LABEL_4',
        'desire': 'LABEL_4',
        'disappointment': 'LABEL_2',
        'disapproval': 'LABEL_1',
        'disgust': 'LABEL_1',
        'embarrassment': 'LABEL_2',
        'excitement': 'LABEL_4',
        'fear': 'LABEL_1',
        'gratitude': 'LABEL_5',
        'grief': 'LABEL_1',
        'joy': 'LABEL_5',
        'love': 'LABEL_5',
        'nervousness': 'LABEL_1',
        'optimism': 'LABEL_4',
        'pride': 'LABEL_5',
        'realization': 'LABEL_4',
        'relief': 'LABEL_4',
        'remorse': 'LABEL_1',
        'sadness': 'LABEL_1',
        'surprise': 'LABEL_4',
        'neutral': 'LABEL_3',
    }

    emotion_explanation = emotion_explanations.get(label, 'Emotion label not recognized.')
    
    sentiment_label = sentiment_mapping.get(label, f'LABEL_{score}')  # Use the numerical score as a fallback
    sentiment_explanation = {
        'LABEL_1': 'The sentiment is very negative.',
        'LABEL_2': 'The sentiment is somewhat negative.',
        'LABEL_3': 'The sentiment is neutral.',
        'LABEL_4': 'The sentiment is somewhat positive.',
        'LABEL_5': 'The sentiment is very positive.',
    }.get(sentiment_label, 'Sentiment label not recognized.')  # Use a default value
    
    return emotion_explanation, sentiment_explanation

# Function to display emotion labels, explanations, sentiment label, and sentiment score
def display_results(emotions):
    st.subheader("Analysis Results:")
    for emotion_result in emotions:
        emotion_label = emotion_result['label']
        emotion_score = emotion_result['score']
        emotion_explanation, sentiment_explanation = explain_emotion(emotion_label, emotion_score)

        st.warning(f"Emotion Label: {emotion_label}")
        st.warning(f"Emotion Explanation: {emotion_explanation}")

        # Display sentiment score and explanation
        st.warning(f"Sentiment Score: {emotion_score:.2f}")
        st.warning(f"Sentiment Explanation: {sentiment_explanation}")


def main():
    st.title("Emotion Detection App")

    # Text input for user to enter sentences for emotion analysis
    user_input = st.text_area("Enter your sentences here (one per line):", "I feel happy today.\nI'm angry at work.")

    # Split input text into sentences
    sentences = user_input.split('\n')

    # Button to trigger emotion detection
    if st.button("Analyze Emotion"):
        emotions = emotion_pipeline(sentences)  # Use the loaded model directly

        # Display the results for each sentence
        display_results(emotions)

if __name__ == "_main_":
    main()