#!/usr/bin/env bash

#sudo -S pyenv local 3.10.4
python3 --version
pip3 install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

if [ ! -d "venv" ]; then
    virtualenv venv
fi

. venv/bin/activate

python3 --version

pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn