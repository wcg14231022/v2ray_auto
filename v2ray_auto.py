import os
import re

import requests
import config
import subprocess


class V2RayAuto:
    def __init__(self):
        self.curl_cmd = ""
        self.get_curl_cmd()

    def get_curl_cmd(self):
        """
        获取curl命令，通过curl命令运行github仓库上的v2ray安装脚本

        :return:
        """
        raw_url = V2RayAuto.get_v2ray_install_url()
        self.curl_cmd = f"bash <(curl -s -L {raw_url})"

    @staticmethod
    def get_v2ray_install_url():
        """
        从github仓库中获取v2ray安装脚本的url

        :return:
        """
        headers = {'Authorization': f'token {config.GITHUB_TOKEN}'}
        api_url = f'https://api.github.com/repos/{config.REPO_ADDR}/contents/' \
                  f'{config.V2RAY_SCRIPT_PATH}?ref={config.BRANCH}'
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # 检查 API 请求是否成功
        data = response.json()
        raw_url = data['download_url']
        print(raw_url)  # 输出文件的 Raw URL
        return raw_url

    def auto_install(self):
        """
        调用v2ray.sh自动安装

        :return:
        """
        if self.is_v2ray_install():
            self.uninstall_v2ray()
        resp = subprocess.check_output(self.curl_cmd, shell=True)
        resp = subprocess.check_output("1", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("Y", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        resp = subprocess.check_output("\n", shell=True)
        print("last resp:")
        print(resp)

    def is_v2ray_install(self):
        """
        检查v2ray是否已经安装

        :return:
        """
        subprocess.check_output(self.curl_cmd, shell=True)
        resp = subprocess.check_output("1", shell=True)
        if re.search(r"无需重新安装", resp, re.I | re.M):
            return True
        return False

    def uninstall_v2ray(self):
        """
        卸载v2ray

        :return:
        """
        subprocess.check_output(self.curl_cmd, shell=True)
        subprocess.check_output("2", shell=True)
        subprocess.check_output("Y", shell=True)
        subprocess.check_output("\n", shell=True)
