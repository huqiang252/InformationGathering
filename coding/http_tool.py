#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-25
import sys,requests,json
from pydantic import BaseModel
from typing import Dict, Any
from jsonpath import jsonpath


class HTTPTool(BaseModel):
    method: str = "GET"
    url: str = ""
    path: str = ""
    params: Dict[str, Any] = {}
    headers: Dict[str, str] = {}
    cookies: Dict[str, str] = {}
    data: Any = None
    json_data: Any = None
    file: Any = None
    stat_proxies: bool = True

    def set_url(self, url_data: str) -> 'HTTPTool':
        self.url = url_data
        return self

    def set_host_to_url(self, host: str) -> 'HTTPTool':
        self.url = host + self.path
        return self

    def set_headers(self, key: str, value: str) -> 'HTTPTool':
        self.headers.update({key: value})
        return self

    def set_params(self, params: Dict[str, Any]) -> 'HTTPTool':
        self.params = params
        return self

    def set_cookies(self, key: str, value: str) -> 'HTTPTool':
        self.cookies.update({key: value})
        return self

    def set_data(self, data: Any) -> 'HTTPTool':
        self.data = data
        return self

    def set_json(self, json_data: Any) -> 'HTTPTool':
        self.json_data = json_data
        return self

    def get_proxy(self) -> Dict[str, str]:
        if 'linux' not in sys.platform:
            if self.stat_proxies:
                return {"https": "https://127.0.0.1:8890", "http": "http://127.0.0.1:8890"}
            else:
                return None
        else:
            return None


    # Add other methods as needed

    def run(self, session=None):
        session = session or requests.sessions.Session()

        self.response = session.request(self.method,
                                        self.url,
                                        params=self.params,
                                        cookies=self.cookies,
                                        headers=self.headers,
                                        data=self.data,
                                        json=self.json_data,
                                        proxies=self.get_proxy(),
                                        verify=False,
                                        timeout=10
                                        )


        req_info = {
            "请求地址": self.url,
            "请求方法": self.method,
            "请求头": self.headers,
            "请求数据": self.data,
            "上传文件": str(self.file),
        }
        try:
            log_req_info = json.dumps(req_info, indent=4, ensure_ascii=False)
        except:
            log_req_info = req_info
        print(f'\n{log_req_info}')

        if self.response.status_code!=200:
            print(f"{self.url}在参数：{self.data}----------->响应码不正常：{self.response.status_code}")

        try:
            response_value=self.response.json()
        except:
            response_value=self.response.text

        rep_info = {
            "响应地址":self.response.url,
            "响应耗时(ms)": self.response.elapsed.total_seconds() * 1000,
            "状态码": self.response.status_code,
            "响应数据": response_value,
        }

        try:
            log_rep_info = json.dumps(rep_info, indent=4, ensure_ascii=False)
        except:
            log_rep_info = log_rep_info
        print(f'\n{log_rep_info}')

    def extract(self, field):
        # 参数提取

        value = self.response
        for _key in field.split("."):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                elif _key=="text":
                    value = self.response.text
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value.get(_key)
            elif isinstance(value, list):
                selectKey = (_key[1:-1]).split(":")
                if len(selectKey) == 1:
                    value = value[int(selectKey[0])]
                elif len(selectKey) == 2:
                    value = value[int(selectKey[0]):int(selectKey[1])]


        return value

    def extractOne(self,key=None):
        #通过jsonpath提取内容,返回一个列表
        try:
            datas = self.extract("json()")
        except:
            datas= self.extract("text")
        if key:
            extractDatalist=jsonpath(datas,key)
            return extractDatalist[0]
        else:
            return datas

    def extractAll(self,key=None):
        #通过jsonpath提取内容,返回一个列表
        datas = self.extract("json()")
        if key:
            extractDatalist=jsonpath(datas,key)
            return extractDatalist
        else:
            return datas





    def validate(self, key, expected_value,errormsg=""):
        actual_value = self.extract(key)
        assert actual_value == expected_value,errormsg
        return self




    def validate_to_jsonpath(self,jsonpath_key,expected_value,errormsg=""):
        actual_value = self.extractOne(jsonpath_key)
        assert actual_value == expected_value,errormsg
        return self


# Usage example:
http_data={
    "method":  "GET",
    "url": "http://www.baidu.com"
}
http_tool = HTTPTool(**http_data)

print(http_tool)
http_tool.run()