import logging
from pathlib import Path

from src.typora_argument_parser import TyporaArgumentParser
from src.imgbb_uploader import ImgBBUploader

logging.basicConfig()
LOG = logging.getLogger()

if __name__ == '__main__':
    API_KEY = Path(__file__).parent.with_name("APIKEY").read_text()
    if not API_KEY:
        LOG.error(
            f"Must set ImgBB API-KEY to environment variable $TYPORA_IMAGE_UPLOADER_API_KEY")
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
