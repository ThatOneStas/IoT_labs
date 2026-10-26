import functools
import os
import logging
import sys

class File:
    def __init__(self, name: str, path: str, logger_mode = "console"):
        # Check if the file name ends with ".xml", if not, append it
        if not name.endswith(".xml"):
            name += ".xml"

        base_dir = os.path.abspath(os.getcwd())
        clean_path = path.strip("/")

        full_path = os.path.join(base_dir, clean_path, name)

        # The class is attached to an existing file, if not, raise an exception
        if not os.path.exists(full_path):
            raise FileNotFound("File doesn't exist")
        
        self.name = name
        self.path = path
        self.full_path = full_path
        self.__logger_mode = logger_mode
        self.__log_path = None

        if logger_mode == "console":
            pass
        elif logger_mode == "file":
            self.__log_path = os.path.join(base_dir, clean_path, name[0:-4] + ".log")
        else:
            raise Exception("Unsupported logger mode")

    @staticmethod
    def logger(func):
            @functools.wraps(func)
            def log(self, *args, **kwargs):
                # check if the logger mode is set to "console" or "file" and set config for the chosen mode
                if self.__logger_mode == "console":
                    logging.basicConfig(level=logging.INFO,
                                        handlers=[logging.StreamHandler(sys.stdout)],
                                        force=True)
                elif self.__logger_mode == "file":
                    logging.basicConfig(level=logging.INFO,
                                        handlers=[logging.FileHandler(filename=self.__log_path, encoding="utf-8")],
                                        force=True)

                # log the start of the function call
                logging.info(f"'{func.__name__}' was called for {self}")

                # perform the function call and log any exceptions that occur
                try:
                    result = func(self, *args, **kwargs)
                except Exception as err:
                    logging.error(f"Error occurred while calling '{func.__name__}': {err}")
                    raise

                # log the end of the function call
                logging.info(f"'{func.__name__}' ended for {self}")
                return result
            return log

    @logger
    def read(self):
        try:
            with open(self.full_path, 'r') as file:
                return file.read()
        except Exception as err:
            raise FileCorrupted("File is corrupted or an error occured")
    
    @logger
    def write(self, content):
        try:
            with open(self.full_path, 'w') as file:
                file.write(content)
        except Exception as err:
            raise FileCorrupted("File is corrupted or an error occured.\n" \
                f"Error message: {err}")
    @logger
    def append(self, content):
        try:
            with open(self.full_path, 'a') as file:
                file.write(content)
        except Exception as err:
            raise FileCorrupted("File is corrupted or an error occured")

class FileNotFound(FileNotFoundError):
    def __init__(self, *args):
        super().__init__(*args)

class FileCorrupted(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def main():
    # 1. Attach the class obj to an existing file and perform its operations successfully
    try:
        file = File("db", "/data")
        file.write("Test writing")
        file.append("\nTest adding")
        print(f"File content:\n{file.read()}")
    except Exception as err:
        print(f"Error: {err}")

    # 2. Attach the class obj to a non-existing file and handle the exception
    print()
    try:
        file2 = File("db_2", "/data")
        file2.write("Test writing")
    except Exception as err:
        print(f"Error: {err}")

    # 3. Attach the class obj to an existing file and perform its operations successfully with logger_mode set to "file"
    print()
    try:
        file3 = File("db", "/data", logger_mode="file")
        file3.write("Test writing")
        file3.append("\nTest adding")
        print(f"\nFile content:\n{file3.read()}\n")
    except Exception as err:
        print(f"Error: {err}")

main()