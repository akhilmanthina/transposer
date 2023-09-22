# Transposer App

## Dependencies:
Requires Audiveris (compiled by cloning repo: https://github.com/Audiveris/audiveris) and Lilypond (downloaded here: http://lilypond.org/download.html).

Audiveris folder must be in root and title `Audiveris` and similarly Lilypond folder must be in root and titles `Lilypond`.

Need to create `.env` file and add your google palm api key as `GOOGLE_API_KEY`. Langchain is LLM agnostic, so this can be substituted with any inference model of choice.

Requires python packages:
-`music21`
-`dotenv`
-`langchain`
