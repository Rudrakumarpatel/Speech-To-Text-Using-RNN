# Speech-To-Text-Using-RNN

# Gujarati Speech-to-Text

This project implements a **Speech-to-Text** system for the **Gujarati language** using various libraries, including **pyttsx3** (text-to-speech), and **pydub** for audio processing. The system processes audio files, degrades the quality to simulate noisy conditions, and converts speech to text in Gujarati. Errors are intentionally introduced to simulate real-world recognition challenges.

This project implements a **Speech-to-Text** system specifically designed for the **Gujarati language** using **Recurrent Neural Networks (RNNs)** for enhanced accuracy. It processes speech data, converts it into text, and integrates features such as noise degradation and error simulation for a more robust solution.

## Features

- **Speech Recognition**: Converts spoken Gujarati audio into text.
- **Audio Degradation**: Lowers the audio quality to simulate noisy environments, making the recognition task more challenging.

## RNN Integration

The project uses **Recurrent Neural Networks (RNNs)**, which are well-suited for processing sequential data like speech. RNNs can maintain context across time steps, making them ideal for speech-to-text applications. This model is trained to better recognize Gujarati speech, improving transcription accuracy even under noisy conditions.


## Requirements

Before running this project, make sure you have the following libraries installed:

- **pyttsx3**: For text-to-speech functionality.
- **pydub**: For audio file manipulation (e.g., changing sample rate, adding noise).
- **numpy**: For handling arrays and mathematical operations.
- **random**: For introducing random errors in recognized text.

You can install these libraries using pip:

```bash
pip install pyttsx3 pydub numpy
