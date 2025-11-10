import speech_recognition as sr

# Select mic
mic_name = "default"
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

r = sr.Recognizer()
with sr.Microphone(device_index=device_id) as source:
    print("Say something!")
    audio = r.listen(source)
    print("finished")
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        text = r.recognize_google(audio, language="TR")
        print("you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
