import argparse
from pathlib import Path
from typing import List
from http.client import HTTPSConnection
from base64 import b64encode

import logging


class TyporaArgumentParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument("files", type=Path, nargs='*')

    def parse(self) -> List[Path]:
        return vars(self._parser.parse_args())['files']


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


####################################################################################################
API_KEY = "YOUR IMGBB API KEY HERE"


logging.basicConfig()
LOG = logging.getLogger()

if __name__ == '__main__':
    if not API_KEY or API_KEY == "YOUR IMGBB API KEY HERE":
        LOG.error(
            f"Must set ImgBB API-KEY to upload")
        exit()

    parser = TyporaArgumentParser()
    uploader = ImgBBUploader(API_KEY)

    print("Start to upload images")
    image_files = parser.parse()
    results = []
    for file in image_files:
        response = uploader.upload_image(file).json()
        if 200 != response["status"]:
            LOG.error(f"Error uploading image {file} with {response}")
            continue
        results.append(response["data"]["url"])

    for result in results:
        print(result)
