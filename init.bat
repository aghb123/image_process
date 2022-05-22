if not exist venv (
    virtualenv venv
)

call .\venv\Scripts\activate

pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn