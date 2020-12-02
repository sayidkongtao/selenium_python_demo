import os
import configparser
import json


class Utils:

    @staticmethod
    def load_config():
        config = configparser.ConfigParser()
        config.read(os.path.join(Utils.get_root_directory(), "environment", "config.cfg"), encoding="utf-8")
        # 账号、密码
        username = config.get("login", "username")
        password = config.get("login", "password")
        # url
        url = config.get("platform", "url")
        return {"username": username, "password": password, "url": url}

    @staticmethod
    def load_json_file(file_name):
        with open(file_name, encoding="utf-8") as f:
            content = f.read()
            return json.loads(content)

    @staticmethod
    def get_root_directory():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_file_absolute_path(a, *paths):
        return os.path.join(Utils.get_root_directory(), a, *paths)
