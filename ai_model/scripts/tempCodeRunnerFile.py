for file in audio_files:
    file_path = os.path.join(audio_dir, file)
    print(f"Transcribing: {file_path}")
    
    transcription = model.transcribe(file_path)["text"]
    results.append({"filename": file, "transcription": transcription})