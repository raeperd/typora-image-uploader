import logging
import os

from src.typora_argument_parser import TyporaArgumentParser
from src.imgbb_uploader import ImgBBUploader

logging.basicConfig()

if __name__ == '__main__':
    API_KEY = os.getenv("TYPORA_IMAGE_UPLOADER_API_KEY")
    if not API_KEY:
        logging.error(f"Must set ImgBB API-KEY to environment variable $TYPORA_IMAGE_UPLOADER_API_KEY")
        exit()

    print("parser")
    parser = TyporaArgumentParser()
    uploader = ImgBBUploader(API_KEY)

    image_files = parser.parse()
    results = []
    for file in image_files:
        print("uploading")
        response = uploader.upload_image(file).json()
        if 200 != response["status"]:
            logging.error(f"Error uploading image {file} with {response}")
            continue
        results.append(response["data"]["url"])
    for result in results:
        print(result)
