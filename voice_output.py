import win32com.client as wincom
def to_voice(text):
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

