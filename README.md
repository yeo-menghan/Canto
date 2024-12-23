# Fine-Tuning Whisper-Small for Cantonese ASR

## Project Overview

This project focuses on fine-tuning OpenAI's **Whisper-Small** model using the Cantonese dataset (zh-HK) from the Mozilla Foundation's **Common Voice 11.0** dataset. The primary goal is to improve **Automatic Speech Recognition (ASR)** performance for Cantonese, specifically targeting the transcription of lyrics from my **top 10 Cantonese songs**. By fine-tuning Whisper-Small, a lightweight yet powerful ASR model, with high-quality, community-contributed audio data, this project aims to deliver reliable and domain-specific transcription for Cantonese music lyrics.

## Key Features

- Fine-tuned **Whisper-Small** model for Cantonese ASR.
- Utilizes the **Common Voice 11.0** Cantonese dataset (zh-HK).
- Focused transcription on **Cantonese song lyrics**.
- Tools for processing YouTube audio and visualizing dataset insights.

---

## Getting Started

### Prerequisites

- **Docker**: Ensure you have Docker installed on your system.
- **Python 3.9+** (optional, if not using Docker).

### Running the Application

1. **Build the Docker Image**

   ```bash
   docker build -t whisper-canto-app .
   ```
2. ***Run Docker Container***
    ```bash
    docker run -p 7860:7860 whisper-canto-app
    ```
  The program may take a while to boot up
3. Once the container is running, you can access the application via your browser via http://localhost:7860/


### Alternative way to run application (if docker not working)

1. ***Create python virtual environment on python version 3.11.6***
    ```bash
    python3.11.6 -m venv venv
    source venv/bin/activate
    ```

2. ***Installation of dependencies using pip***
    ```bash
    pip install requirements.txt
    ```

3. ***Run the program***
    ```bash
    python app.py
    ```

## Features & Directory Structure
1. Transcription
- Directory: data_transcription/
- Functionality:
  - Process YouTube links (stored in ./sample_data) to transcribe audio into text.
  - Converts YouTube links to .mp3 formatted audio files for transcription.
2. Dataset Visualization
- Directory: data_visualisation/
- Functionality:
  - Tools to explore the Common Voice 11.0 dataset.
  - Visualize patterns and characteristics of the dataset and the selected Cantonese songs.


## Dataset Details
- Source: Mozilla Common Voice 11.0
- Language: Cantonese (zh-HK)
- Purpose: Fine-tuning the Whisper-Small model for domain-specific performance targeting Cantonese Speech.


## Contributing
Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m "Add feature-name".
4. Push to the branch: git push origin feature-name.
5. Open a pull request.
