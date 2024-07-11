# Emotion Recognition App

Welcome to my Emotion Recognition App! This project is a web application that I developed to recognize human emotions from text input. It uses the `streamlit` library for the web interface and the `transformers` library by Hugging Face to perform sentiment analysis. The app leverages the pre-trained `arpanghoshal/EmoRoBERTa` model for detecting emotions.

## Features

- **Emotion Detection**: Identifies and classifies emotions from text.
- **Sentiment Analysis**: Provides a sentiment score and explanation for each detected emotion.
- **User Interface**: Easy-to-use web interface for entering text and viewing results.

## Installation

To get this application up and running, you will need to have Python installed. Follow these steps to set up the environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/emotion-recognition-app.git
    cd emotion-recognition-app
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the application with the following command:
```bash
streamlit run emotion.py
 ```

This will start the Streamlit server, and you can access the web application in your browser at `http://localhost:8501`.

## How to Use

1. **Enter Text**: In the text area provided on the main page, enter one or more sentences, each on a new line.
2. **Analyze Emotion**: Click the "Analyze Emotion" button to perform emotion detection and sentiment analysis on the entered text.
3. **View Results**: The analysis results will be displayed below, showing the detected emotion labels, their explanations, sentiment scores, and sentiment explanations.

## Example

After starting the app, you can enter sentences like:

## CSS

   ```bash
    I feel happy today.
    I'm angry at work.
    ```


Click on **"Analyze Emotion"** to see the results:

## yaml

   ```bash
    Emotion Label: joy
    Emotion Explanation: You are feeling joyful and happy.
    Sentiment Score: 0.95
    Sentiment Explanation: The sentiment is very positive.
    Emotion Label: anger
    Emotion Explanation: You are expressing anger or frustration.
    Sentiment Score: 0.89
    Sentiment Explanation: The sentiment is very negative.
    ```

## File Overview

**`emotion.py**: This is the main script for running the Streamlit application.
**`requirements.txt'**: This file lists the required Python packages.

## Contributing

I welcome contributions! If you have any suggestions or find any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

Hugging Face Transformers: Hugging Face
Streamlit: Streamlit

## sql

Feel free to personalize it further or make any adjustments that you see fit!
