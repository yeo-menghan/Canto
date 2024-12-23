# Data Visualization for Common Voice and Cantonese Songs

## Overview

This folder contains tools and resources for exploring and visualizing the Cantonese dataset (zh-HK) from **Mozilla Common Voice 11.0** and the characteristics of the selected Cantonese songs. It includes custom visualizations and insights aimed at better understanding the data distribution, quality, and relevance for fine-tuning the Whisper-Small ASR model.

Due to conflicting dependencies with other parts of the project, this submodule has its own `data_requirements.txt` file for managing dependencies.

## Setup Instructions

### Step 1: Create a Virtual Environment

To avoid dependency conflicts, it is recommended to use a virtual environment:

```bash
python3 -m venv data_viz_env
source data_viz_env/bin/activate  # On Windows, use `data_viz_env\Scripts\activate`
```

### Step 2: Install Dependencies
Install the required packages from data_requirements.txt:

```bash
pip install -r data_requirements.txt
```

## Notebooks

1. Common Voice Dataset Exploration (common_voices.ipynb)
- Visualizes the Cantonese dataset from Mozilla Common Voice 11.0.
- Insights include:
  - Data distribution (e.g., speaker demographics, audio lengths).  - Quality analysis of audio samples.
  - Metadata exploration (e.g., sentence structures, phonetics, etc.).
2. Cantonese Song Visualization (visualise_canto.ipynb)
- Focuses on the characteristics of the selected top 10 Cantonese songs.
- Generates visualizations such as:
  - Word frequency analysis of song lyrics.
  - Pronunciation patterns in lyrics.
  - Alignment of song vocabulary with the Common Voice dataset.

## Fonts for Visualization
This folder includes Chinese fonts to ensure proper rendering of Cantonese characters in visualizations:

- Noto Sans TC: A widely used font for Traditional Chinese.
- Source Han Sans CN Light: A lightweight font optimized for Chinese content.
- These fonts are embedded in the notebooks for seamless plotting and rendering.
