# Typora Image uploader

Typora [ImgBB](https://api.imgbb.com/) uploader using [python3 requests](https://docs.python-requests.org/en/master/)



## Motivation

[Typora | Upload Image - Custom](https://support.typora.io/Upload-Image/#custom)



## Getting started

### Requirements

- python3 
- [python3 requests](https://docs.python-requests.org/en/master/) installed **NOT IN virtualenv** but in global pip
- ImgBB API KEY 
  - You can get this in [ImgBB API Reference](https://api.imgbb.com/))
  - Set this value in environment value `$TYPORA_IMAGE_UPLOADER_API_KEY`
  - Or you can hard code main.py with your key



### Usage

1. Clone this repository where you want (Assume C:/github)
```shell script
$ git clone https://github.com/raeperd/typora-image-uploader.git
```
2. Open typora, File > Settings > Image
3. Configure When Insert.. to `Upload image`
4. Configure Image Upload Settings as follow (With your repository path)
   - Image uploader => `Custom Command`
   - Command => `python3 C:\github\typora-iamge-uploader/main.py`
5. And click Test Uploader to verify your settings 



