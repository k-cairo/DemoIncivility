import os
import simplejson


# E5
class File:

    # --------------- JSON ---------------
    # E5
    @classmethod
    def load_json(cls, fullpath) -> (bool, str, any):
        success: bool = False
        message: str = ""
        data = None

        try:
            with open(file=fullpath, mode='r', encoding='utf-8') as reader:
                data = simplejson.load(reader)
            success = True
        except Exception as ex:
            message = f"\nLoad Json error : {ex}"
        return success, message, data

    # --------------- JSON ---------------
    # E5
    @classmethod
    def is_valid_path(cls, isdir: bool, path: str) -> bool:
        return bool((isdir and os.path.isdir(path)) or (not isdir and os.path.isfile(path)))
