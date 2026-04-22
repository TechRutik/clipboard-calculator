import keyboard
import pyperclip
import time

last_run = 0

def safe_eval(expr):
    allowed_chars = "0123456789+-*/(). "
    if all(c in allowed_chars for c in expr):
        return eval(expr)
    else:
        raise ValueError("Unsafe input")

def calculate():
    global last_run
    current_time = time.time()

    if current_time - last_run < 0.5:
        return

    last_run = current_time

    keyboard.press_and_release('ctrl+c')
    time.sleep(0.2)

    text = pyperclip.paste().strip()

    try:
        result = safe_eval(text)
        pyperclip.copy(str(result))
        time.sleep(0.1)

        keyboard.press_and_release('right')  # remove selection
        keyboard.press_and_release('ctrl+v')

    except Exception as e:
        print("Error:", e)

keyboard.add_hotkey('ctrl+=', calculate)

print("Running... Press ESC to stop")
keyboard.wait('esc') 