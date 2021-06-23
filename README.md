# Typora Image uploader

Typora [ImgBB](https://api.imgbb.com/) uploader using [python3 requests](https://docs.python-requests.org/en/master/)



## Motivation

[Typora | Upload Image - Custom](https://support.typora.io/Upload-Image/#custom)



## Getting started

### Requirements

- python3 
- ImgBB API KEY 
  - You can get this in [ImgBB API Reference](https://api.imgbb.com/)
  - **Set your API KEY value in variable `API_KEY` in main.py script**


### Usage

1. Download main.py in this repositories root, or clone it 
```shell script
$ git clone https://github.com/raeperd/typora-image-uploader.git
```
2. **Change `API_KEY` variable in main.py to your imgbb API KEY**
3. Open typora, File > Settings > Image
4. Configure When Insert.. to `Upload image`
5. Configure Image Upload Settings as follow (With your repository path)
   - Image uploader => `Custom Command`
   - Command => Specify python script path
   - For Example
     - On windows, `python3 C:\github\typora-iamge-uploader/main.py`
     - On unix like systems, `python3 /home/your_user_name/main.py` 
6. And click Test Uploader to verify your settings 
