import pyttsx3
import speech_recognition as sr


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Select mic
mic_name = "default"
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
# Initialize the recognizer
r = sr.Recognizer()

# Loop infinitely for user to speak
while 1:
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone(device_index=device_id) as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Say something!")
            # listens for the user's input
            audio = r.listen(source)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio, language="TR")
            MyText = MyText.lower()

            print("Did you say " + MyText)
            SpeakText(MyText)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
