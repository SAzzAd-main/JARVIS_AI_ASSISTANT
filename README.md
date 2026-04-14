# Jarvis - Voice Assistant in Python
[🚀 View Live Demo](https://sazzad-main.github.io/JARVIS_AI_ASSISTANT/)

Jarvis is a simple voice-controlled assistant built using Python. It can recognize speech, perform basic tasks like opening websites, playing music, fetching news, and even respond using AI.

---

## Features

* Voice activation using wake word **"Jarvis"**
* Open popular websites:

  * Google
  * Facebook
  * YouTube
  * LinkedIn
* Play music from a custom music library
* Fetch and read latest news headlines
* AI-powered responses using Google Generative AI
* Text-to-speech output

---

## Technologies Used

* Python
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* requests (API calls)
* Google Generative AI (Gemini)
* Webbrowser module

---

## Installation

1. Clone the repository:

git clone https://github.com/SAzzAd-main/JARVIS_AI_ASSISTANT.git
cd JARVIS_AI_ASSISTANT

2. Install dependencies:

```
pip install speechrecognition pyttsx3 requests google-generativeai pypiwin32
```

3. (Optional for better speech recognition)

```
pip install pocketsphinx
```

---

## Setup

* Replace your API keys inside the code:

```
newsapi = "YOUR_NEWS_API_KEY"
apiKey = "YOUR_GEMINI_API_KEY"
```

* Make sure your microphone is working properly.

---

## How to Run

```
python jarvis.py
```

Say **"Jarvis"** to activate, then give a command.

---

## Example Commands

* "Jarvis open Google"
* "Jarvis open YouTube"
* "Jarvis play believer"
* "Jarvis tell me news"
* "Jarvis what is artificial intelligence"

---

## Project Structure

```
jarvis.py
musiclibrary.py
README.md
```

---

## Notes

* Speech recognition depends on internet connection.
* News API has request limits.
* Music must be predefined in `musiclibrary.py`.

---

## Future Improvements

* Add GUI interface
* Support more commands
* Improve speech accuracy
* Add continuous conversation mode

---

## Author

Sazzad Hossain

---

## License

This project is open-source and free to use.
