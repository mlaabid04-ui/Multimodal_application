# voice_transcription/voice_module.py
# ==================================
# Module de transcription vocale (version stable)

import time
import threading
import speech_recognition as sr

_recognizer = sr.Recognizer()
_microphone = sr.Microphone()

_last_text = ""
_voice_active = False


def _voice_loop():
    global _last_text, _voice_active

    with _microphone as source:
        _recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            with _microphone as source:
                _voice_active = False
                audio = _recognizer.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=4
                )

            _voice_active = True
            text = _recognizer.recognize_google(audio, language="fr-FR")
            _last_text = text
            print("[VOICE] Transcription :", text)

        except sr.WaitTimeoutError:
            _voice_active = False
        except sr.UnknownValueError:
            _voice_active = False
        except Exception as e:
            print("[VOICE ERROR]", e)
            _voice_active = False

        time.sleep(0.2)


def start_voice_recognition():
    thread = threading.Thread(target=_voice_loop, daemon=True)
    thread.start()


def is_voice_active():
    return _voice_active


def get_voice_text():
    global _last_text
    text = _last_text
    _last_text = ""
    return text
