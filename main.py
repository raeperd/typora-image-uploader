import argparse
import json
import logging
from base64 import b64encode
from codecs import encode
from http.client import HTTPSConnection
from pathlib import Path
from typing import List

########################################################################################################################
API_KEY = "YOUR IMGBB API KEY HERE"
########################################################################################################################


class TyporaArgumentParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument("files", type=Path, nargs='*')

    def parse(self) -> List[Path]:
        return vars(self._parser.parse_args())['files']


class ImgBBUploader:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._boundary = "BOUNDARY_FOR_IMGBB_UPLOADER"

    def upload_image(self, image_file: Path):
        connection = HTTPSConnection("api.imgbb.com")
        header = self._build_request_header()
        body = self._build_request_body(image_file)
        connection.request("POST", f"/1/upload?key={self._api_key}&name={image_file.stem}",
                           body,
                           header)
        return connection.getresponse()

    def _build_request_header(self):
        return {
            'Content-type': f'multipart/form-data; boundary={self._boundary}'
        }

    def _build_request_body(self, image_file: Path):
        payloads = [encode('--' + self._boundary),
                    encode(f'Content-Disposition: form-data; name=image;'),
                    encode('Content-Type: text/plain'),
                    encode(''),
                    b64encode(image_file.read_bytes()),
                    encode('--' + self._boundary + '--'),
                    encode('')]
        return b'\r\n'.join(payloads)


########################################################################################################################

logging.basicConfig()
LOG = logging.getLogger()

if __name__ == '__main__':
    if not API_KEY or API_KEY == "YOUR IMGBB API KEY HERE":
        LOG.error(
            f"Must set ImgBB API-KEY to upload")
        exit()

    parser = TyporaArgumentParser()
    uploader = ImgBBUploader(API_KEY)

    image_files = parser.parse()
    results = []
    for file in image_files:
        response = uploader.upload_image(file).read().decode()
        response = json.loads(response)
        if 'error' in response.keys():
            LOG.error(f"Error uploading image {file} with {response}")
            continue
        results.append(response["data"]["url"])

    for result in results:
        print(result)
