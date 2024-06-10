import os

os.system("ls")
os.system("cd /home/xlab-app-center")
os.system("ls")

os.system("python app_test/download.py")
# os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava")
# os.system("python -m llava.serve.controller --host 0.0.0.0 --port 10000")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat")
# os.system("python -m internvl.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava")
# os.system("python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload")

os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava/llava/serve/")
os.system("python -m controller --host 0.0.0.0 --port 10000")

os.system("cd /home/xlab-app-center/app_test/internvl_chat/internvl/serve/")
os.system("python -m model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center")

os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava/llava/serve")
os.system("python -m gradio_web_server --controller http://localhost:10000 --model-list-mode reload")