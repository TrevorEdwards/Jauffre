import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1, sample_rate = 44100, chunk_size = 512) as source:
        print("Say something!")
        audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        trans = r.recognize_google(audio)
        print trans
        return trans
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# import pyaudio
#
# def recognize():
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format = pyaudio.paInt16,
#         channels = 1,
#         rate = 256, #TODO tune this
#         input = True,
#         frames_per_buffer = 4, #TODO this too
#         input_device_index = 2) #TODO hardcode this right
#
#     recog = sr.Recognizer("en-GB")
#     r = array('h')
#
#     ## You will need to loop this next bit until you are finished recording
#     data = array('h',stream.read(framesPerBuffer))
#     rms = audioop.rms(data,2)
#     r.extend(data)
#     r.append(data)
#     ########
#     data = pack('<' + ('h'*len(r)), *r)
#     sample_width = p.get_sample_size(pyaudio.paInt16)
#
#     wf = wave.open("/home/pi/Desktop/foo.wav", 'wb')
#     wf.setnchannels(1)
#     wf.setsampwidth(sample_width)
#     wf.setframerate(sRate)
#     wf.writeframes(data)
#     wf.close()
#
#     with sr.WavFile("foo.wav") as source:
#         return recog.record(source)
