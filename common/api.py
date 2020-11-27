import requests
import urllib3
from contextlib import closing

urllib3.disable_warnings()


class APIClient(object):
    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.session()

    def build_url(self, relative_url):
        self.base_url = self.base_url.strip()
        relative_url = relative_url.strip()
        if self.base_url != "" and self.base_url[len(self.base_url) - 1] == "/":
            self.base_url = self.base_url[:len(self.base_url) - 1]
        if relative_url != "" and relative_url[0] == "/":
            relative_url = relative_url[1:]
        if self.base_url != "":
            return "/".join([self.base_url, relative_url])
        return "".join([self.base_url, relative_url])

    def send_request(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url=self.build_url(url), params=params, data=data, json=json, headers=headers, **kwargs)

    def download_file(self, method, url, file_name, *args, **kwargs):
        with closing(self.send_request(method, url, stream=True, *args, **kwargs)) as response:
            if response.status_code == 200:
                with open(file_name, "wb") as file:
                    for chunk in response.iter_content(chunk_size=128):
                        file.write(chunk)
            else:
                return response

    def close_session(self):
        self.session.close()


if __name__ == "__main__":
    a = APIClient(base_url="https://www.baidu.com")
    print(a.build_url("/a/b/c"))
    print(a.build_url("a/b/c"))
