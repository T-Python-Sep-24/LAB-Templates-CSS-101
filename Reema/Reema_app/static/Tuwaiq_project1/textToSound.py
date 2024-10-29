from gtts import gTTS
import os
import playsound

class TextToSpeech:
    def __init__(self):
        self.language = 'en'  # Default language

    def set_language(self, language):
        self.language = language

    def text_to_speech(self, text):
        try:
            # Create a gTTS object
            tts = gTTS(text=text, lang=self.language, slow=False)
            filename = "output.mp3"
            tts.save(filename)  # Save the audio file
            playsound.playsound(filename)  # Play the audio file
            return filename
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def display_menu():
    print("\n--- Text to Speech Converter ---")
    print("1. Convert Text to Speech")
    print("2. Change Language")
    print("3. Exit")

def main():
    tts_system = TextToSpeech()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            text = input("Enter the text you want to convert to speech: ")
            if text.strip():  # Check if text is not empty
                tts_system.text_to_speech(text)
            else:
                print("Text cannot be empty.")
        elif choice == '2':
            language = input("Enter language code (e.g., 'en' for English, 'es' for Spanish): ")
            tts_system.set_language(language)
            print(f"Language set to {language}.")
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
