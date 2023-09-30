import speech_recognition as sr
import openai
openai.api_key = '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'

#liste les micros
def listMicrophone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))


#reconnait la voix
def voiceToText():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Say something !")
        audio = r.listen(source)
        text = r.recognize_google(audio, None, language='fr=FR')
        print("J'ai dit: \"{0}\"".format(text))

def getChatGPTAnswer(text: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = text,
        temperature = 0,
        max_tokens = 100,
        top_p = 1.0,
        frequency_penalty= 0.2,
        presence_penalty = 0.0,
    )

voiceToText()
    

