# eye_tracking/eye_module.py
# =========================
# Module de communication oculaire
# Compatible avec le ModeManager

import threading
import time

# -------------------------------------------------
# VARIABLE PARTAGÉE (lue par main.py)
# -------------------------------------------------

_last_eye_command = None
_lock = threading.Lock()


# -------------------------------------------------
# FONCTION APPELÉE PAR main.py
# -------------------------------------------------

def get_eye_command() -> str:
    """
    Retourne la dernière commande oculaire validée
    (ou None si rien de nouveau)
    """
    global _last_eye_command
    with _lock:
        cmd = _last_eye_command
        _last_eye_command = None
    return cmd


# -------------------------------------------------
# À APPELER QUAND UNE SÉLECTION EST VALIDÉE
# (double clignement)
# -------------------------------------------------

def _set_eye_command(command: str):
    global _last_eye_command
    with _lock:
        _last_eye_command = command


# -------------------------------------------------
# THREAD EYE-TRACKING (TON CODE EXISTANT)
# -------------------------------------------------

def eye_tracking_loop():
    """
    Ici TU METS TON CODE EXISTANT :
    - OpenCV
    - MediaPipe
    - Calibration
    - Double clignement
    """

    print("[EYE] Eye-tracking started")

    while True:
        # EXEMPLE (À REMPLACER PAR TON CODE)
        # ---------------------------------
        # Si double clignement + bouton "WC"
        # alors :
        # _set_eye_command("Besoin WC")

        time.sleep(0.01)


def start_eye_tracking():
    """
    Lance le eye-tracking dans un thread séparé
    """
    t = threading.Thread(target=eye_tracking_loop, daemon=True)
    t.start()
