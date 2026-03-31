from preprocessing.audio_extractor import extract_audio
from preprocessing.speech_to_text import transcribe_audio
from models.summarizer import summarize_text
from extraction.action_extractor import extract_action_items
from embeddings.rag_engine import create_index, query_index

def process_file(file_path):
    if file_path.endswith(".mp4"):
        print("Extracting audio from video...")
        audio_path = "data/temp_audio.wav"
        extract_audio(file_path, audio_path)
    else:
        audio_path = file_path

    print("Transcribing audio...")
    text = transcribe_audio(audio_path)

    print("\n--- TRANSCRIPT ---\n")
    print(text)

    print("\n--- SUMMARY ---\n")
    summary = summarize_text(text)
    print(summary)
    
    print("\n--- ACTION ITEMS ---\n")
    actions = extract_action_items(text)

    for item in actions:
        print(item)
        
    print("\n--- Q&A SYSTEM ---\n")

    index, sentences = create_index(text)

    while True:
        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = query_index(index, sentences, question)

        print("\nRelevant answers:")
        print("-", answer)    

if __name__ == "__main__":
    process_file("data/Sample.mp4")  # change file name