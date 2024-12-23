from transformers import pipeline
import gradio as gr
import os

# Load the Whisper model pipelines
finetune_pipe = pipeline("automatic-speech-recognition", model="Maverickz1989/openai-whisper-small-canto-colab", return_timestamps=True)
base_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small", return_timestamps=True)

# Ensure the appdata directory exists
os.makedirs("./appdata", exist_ok=True)

# Transcription function
def transcribe(audio):
    # Transcribe audio with both pipelines
    finetuned_transcription = finetune_pipe(audio)["text"]
    base_transcription = base_pipe(audio)["text"]

    # Save both transcriptions to separate .txt files
    finetuned_output_file = "./appdata/finetuned_transcription.txt"
    base_output_file = "./appdata/base_transcription.txt"

    with open(finetuned_output_file, "w", encoding="utf-8") as f:
        f.write(finetuned_transcription)

    with open(base_output_file, "w", encoding="utf-8") as f:
        f.write(base_transcription)

    # Return both transcriptions and downloadable file paths
    return (
        finetuned_transcription,
        finetuned_output_file,
        base_transcription,
        base_output_file
    )

# Gradio Interface
iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(type="filepath"),  # File upload or recording
    outputs=[
        gr.Textbox(label="Finetuned Transcription"),  # Finetuned transcription
        gr.File(label="Download Finetuned Transcription as .txt"),  # File download for finetuned transcription
        gr.Textbox(label="Base Transcription"),  # Original transcription
        gr.File(label="Download Base Transcription as .txt"),  # File download for original transcription
    ],
    title="Whisper Small Canto vs Whisper Small",
    description="Compare Canto speech recognition using a fine-tuned Whisper small model and the base Whisper small model.",
)

# Launch the interface
iface.launch(server_name="0.0.0.0", server_port=7860)
