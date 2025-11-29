import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"{i}. {voice.name}")

    choice = int(input("\nChoose voice number: "))
    engine.setProperty('voice', voices[choice].id)
    text = input("\nEnter text to speak: ")

    print("\nSpeaking... ")
    engine.say(text)
    engine.runAndWait()
text_to_speech()
