# Transposer App

## Description:
Transposes PDF sheet music given input instrument and output instrument! 

Future functionality:
- Streamlit UI (drag and drop input pdf)
- Deployed Demo
- More chat-like UX?

## Dependencies:
Requires Audiveris (compiled by cloning repo: https://github.com/Audiveris/audiveris) and Lilypond (downloaded here: http://lilypond.org/download.html).

Audiveris folder must be in root and title `Audiveris` and similarly Lilypond folder must be in root and titles `Lilypond`.

Need to create `.env` file and add your Google PaLM API key as `GOOGLE_API_KEY`. Langchain is LLM agnostic, so this can be substituted with any inference model of choice.

Requires the following Python packages, install with pip:
- `music21`
- `dotenv`
- `langchain`
