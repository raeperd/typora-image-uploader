from pathlib import Path

from requests import post


class ImgBBUploader:
    def __init__(self, api_key: str):
        self._address = "https://api.imgbb.com/1/upload"
        self._api_key = api_key

    def upload_image(self, image_file: Path):
        return post(self._address,
                    data={"key": self._api_key, "name": image_file.stem},
                    files={"image": image_file.read_bytes()})


if __name__ == '__main__':
    uploader = ImgBBUploader("SOME_API_KEY")
    response = uploader.upload_image(Path("../test/data/python.png").absolute())
    print(response.json())
