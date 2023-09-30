import whisper as sr
import openai
openai.api_key = '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'

#liste les micros
def listMicrophone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))


#reconnait la voix
def voiceToText():
    r = sr.Whisper()
    with sr.Whisper(1) as source:
        print("Say something !")
        audio = r.listen(source)
        text = r.recognize_google(audio, None, language='fr=FR')
        print("J'ai dit: \"{0}\"".format(text))

voiceToText()





