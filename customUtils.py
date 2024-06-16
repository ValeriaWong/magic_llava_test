import requests

async def fetch_image_info(file):
    """异步获取图像信息的API调用"""
    url = 'http://v.onlyax.com:38200/upload_file_and_detect_text'
    response = requests.post(url, files={'file': file})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API调用失败")
