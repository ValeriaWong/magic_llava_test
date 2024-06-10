# from openxlab.model import download

# download(model_repo='Nobody-ML/internvl-1_5-2b', output='/home/xlab-app-center')

from modelscope import snapshot_download
model_dir = snapshot_download('OpenGVLab/Mini-InternVL-Chat-2B-V1-5', cache_dir='/home/xlab-app-center')