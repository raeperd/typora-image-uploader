from base64 import b64encode
from pathlib import Path

from http.client import HTTPSConnection


class ImgBBUploader:
    def __init__(self, api_key: str):
        self._address = "https://api.imgbb.com/1/upload"
        self._api_key = api_key

    def upload_image(self, image_file: Path):
        connection = HTTPSConnection("api.imgbb.com")
        connection.request("POST", f"/1/upload?key={self._api_key}&name={image_file.stem}",
                           f"image={b64encode(image_file.read_bytes()).decode()}",
                           headers={"Content-Type": "application/x-www-form-urlencoded"})
        return connection.getresponse()


if __name__ == '__main__':
    uploader = ImgBBUploader("")
    response = uploader.upload_image(
        Path("../test/data/python.png").absolute())
    print(response.read().decode())
    print(response.headers)
