from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")

def main():
    tts.say("I can speak!")
    while True:
        pass
def destroy():
    tts.say("Bye!")
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()