from tts import TTS

tts = TTS(engine='espeak')
tts.lang("en-US")

def main():
    tts.say("hello, nice to meet you!")
    while True:
        pass
    
def destroy():
    tts.say("see you later")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()