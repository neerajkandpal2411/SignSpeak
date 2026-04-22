import pyttsx3
import threading

_engine = None
_lock = threading.Lock()

def get_engine():
    global _engine
    with _lock:
        if _engine is None:
            _engine = pyttsx3.init()
            _engine.setProperty('rate', 150)
        return _engine

def speak(text):
    """Speak text safely without RuntimeError"""
    def _speak():
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"Speech error (ignored): {e}")
    
    thread = threading.Thread(target=_speak)
    thread.daemon = True
    thread.start()