#!/bin/bash

cd /home/xlab-app-center/app_test/internvl_chat_llava/ && python -m llava.serve.controller --host 0.0.0.0 --port 10000

cd /home/xlab-app-center/app_test/internvl_chat/ && python -m internvl.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center
