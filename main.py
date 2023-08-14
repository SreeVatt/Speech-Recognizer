import speech_recognition as sr
r = sr.Recognizer()
def perform_task():
    with sr.Microphone() as source:
        print('Speak now...')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print('Command:', command)
        except:
            print('Error: Could not recognize command.')
perform_task()
