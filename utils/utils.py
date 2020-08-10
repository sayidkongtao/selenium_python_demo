import os
import configparser
import json

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)


class Utils:

    @staticmethod
    def load_config():
        config = configparser.ConfigParser()
        config.read(PATH(os.path.join("..", "environment", "config.cfg")), encoding="utf-8")
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

