import functools
import os
import logging
import sys
import xml.etree.ElementTree as ET

class FileNotFound(FileNotFoundError):
    def __init__(self, *args):
        super().__init__(*args)

class FileCorrupted(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def logged(exception=Exception, mode=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Configure logging according to the given mode
            current_mode = mode or getattr(self, "_logger_mode", "console")
            log_path = getattr(self, "_log_path", None)

            if current_mode == "console":
                logging.basicConfig(
                    level=logging.INFO,
                    handlers=[logging.StreamHandler(sys.stdout)],
                    force=True,
                    format="%(asctime)s [%(levelname)s] %(message)s"
                )
            elif current_mode == "file":
                logging.basicConfig(
                    level=logging.INFO,
                    handlers=[logging.FileHandler(log_path, encoding="utf-8")],
                    force=True,
                    format="%(asctime)s [%(levelname)s] %(message)s"
                )

            logging.info(f"Starting execution of '{func.__name__}' for file: {self.full_path}")

            try:
                result = func(self, *args, **kwargs)
                logging.info(f"Successful completion of '{func.__name__}' for file: {self.full_path}")
                return result
            except exception as err:
                logging.error(f"Error occurred while executing '{func.__name__}' for file: {self.full_path}. {err}")
                raise
        return wrapper
    return decorator

# Version of the logged decorator that handles logger_mode and log_path for __init__ method
# def logged(exception=Exception, mode=None):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             current_mode = mode
#             log_path = None

#             if func.__name__ == "__init__":
#                 current_mode = current_mode or kwargs.get("logger_mode") or (args[2] if len(args) > 2 else "console")
                
#                 # # Configure logging according to the given mode
#                 if current_mode == "file":
#                     name = kwargs.get("name") or (args[0] if len(args) > 0 else "")
#                     path = kwargs.get("path") or (args[1] if len(args) > 1 else "")
#                     if not name.endswith(".xml"):
#                         name += ".xml"
#                     base_dir = os.path.abspath(os.getcwd())
#                     clean_path = path.strip("/")
#                     log_path = os.path.join(base_dir, clean_path, name[:-4] + ".log")
#             else:
#                 current_mode = current_mode or getattr(self, "_logger_mode", "console")
#                 log_path = getattr(self, "_log_path", None)

#             if current_mode == "console":
#                 logging.basicConfig(
#                     level=logging.INFO,
#                     handlers=[logging.StreamHandler(sys.stdout)],
#                     force=True,
#                     format="%(asctime)s [%(levelname)s] %(message)s"
#                 )
#             elif current_mode == "file" and log_path:
#                 logging.basicConfig(
#                     level=logging.INFO,
#                     handlers=[logging.FileHandler(log_path, encoding="utf-8")],
#                     force=True,
#                     format="%(asctime)s [%(levelname)s] %(message)s"
#                 )

#             file_id = getattr(self, "full_path", getattr(self, "name", "file"))

#             logging.info(f"Starting execution of '{func.__name__}' for file: {file_id}")

#             try:
#                 result = func(self, *args, **kwargs)
#                 logging.info(f"Successful completion of '{func.__name__}' for file: {file_id}")
#                 return result
#             except exception as err:
#                 logging.error(f"Error occurred while executing '{func.__name__}' for file: {file_id}. {err}")
#                 raise
#         return wrapper
#     return decorator

class File:
    # decorator applied to __init__ method to log its execution and handle exceptions
    # @logged(exception=(FileNotFound, FileCorrupted))
    def __init__(self, name: str, path: str, logger_mode = "console"):
        # Check if the file name ends with ".xml", if not, append it
        if not name.endswith(".xml"):
            name += ".xml"

        base_dir = os.path.abspath(os.getcwd())
        clean_path = path.strip("/")

        full_path = os.path.join(base_dir, clean_path, name)
        
        self.name = name
        self.path = path
        self.full_path = full_path
        self._logger_mode = logger_mode
        self._log_path = os.path.join(base_dir, clean_path, name[:-4] + ".log") if logger_mode == "file" else None

        # Set the log path based on the logger mode
        if logger_mode not in ("console", "file"):
            raise ValueError("Invalid logger mode. Choose 'console' or 'file'.")

        # The class is attached to an existing file, if not, raise an exception
        if not os.path.exists(full_path):
            raise FileNotFound("File doesn't exist")

    @logged(exception=FileCorrupted)
    def read(self):
        try:
            with open(self.full_path, 'r') as file:
                content = file.read()
            # check the XML's validity
            ET.fromstring(content)
            return content
        except (ET.ParseError, OSError, UnicodeDecodeError) as err:
            raise FileCorrupted(f"File is corrupted or XML structure is invalid: {err}")
    
    @logged(exception=FileCorrupted)
    def write(self, content):
        try:
            # check the XML's validity of given content
            ET.fromstring(content)
            with open(self.full_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except (ET.ParseError, OSError) as err:
            raise FileCorrupted(f"File is corrupted or XML structure is invalid: {err}")
    @logged(exception=FileCorrupted)
    def append(self, content):
        try:
            # check the XML's validity of given content
            ET.fromstring(content)
            with open(self.full_path, 'a', encoding='utf-8') as file:
                ET.fromstring(file.read())  # Read existing content to ensure it's valid XML
                file.write(content)
        except (ET.ParseError, OSError) as err:
            raise FileCorrupted(f"File is corrupted or XML structure is invalid: {err}")

def main():
    # Create testing folder
    test_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(test_dir, exist_ok=True)
    test_file = os.path.join(test_dir, "db.xml")

    # Create a valid XML file for testing
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("<root><item>Initial data</item></root>")

    # 1. Successful reading and writing (both console and file logging)
    print("1. Reading and writing:")
    try:
        file1 = File("db", "/data")
        file2 = File("db", "/data", logger_mode="file")
        # read (console logger)
        print("Content:", file1.read())
        # write (console logger)
        file1.write("<root><item>New content 1</item></root>")
        # read (file logger)
        print("Content:", file2.read())
        # write (file logger)
        file2.write("<root><item>New content 2</item></root>")
    except Exception as e:
        print(f"Error: {e}")

    # 2. Missing file exception (both console and file logging)
    print("\n2. Checking for missing file (FileNotFound)")
    try:
        file_missing = File("non_existent", "/data")
    except Exception as e:
        print(f"Exception caught: {type(e).__name__} -> {e}")
    try:
        file_missing = File("non_existent", "/data", logger_mode="file")
    except Exception as e:
        print(f"Exception caught: {type(e).__name__} -> {e}")

    # 3. Corrupted file exception (both console and file logging)
    print("\n3. Simulating corrupted XML (FileCorrupted)")
    try:
        # Write an invalid XML
        with open(test_file, "w", encoding="utf-8") as f_raw:
            f_raw.write("<root><unclosed_tag></root>")
        
        file_corrupted = File("db", "/data")
        file_corrupted.read()
    except Exception as e:
        print(f"Exception caught: {type(e).__name__} -> {e}")

    try:
        # Write an invalid XML
        with open(test_file, "w", encoding="utf-8") as f_raw:
            f_raw.write("<root><unclosed_tag></root>")
            
        file_corrupted = File("db", "/data", logger_mode="file")
        file_corrupted.read()
    except Exception as e:
        print(f"Exception caught: {type(e).__name__} -> {e}")

if __name__ == "__main__":
    main()