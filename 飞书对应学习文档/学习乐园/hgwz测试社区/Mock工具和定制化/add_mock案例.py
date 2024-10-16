#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-15
import sys
from mitmproxy import ctx
from mitmproxy import tcp
from mitmproxy.utils import strutils
from mitmproxy.tools.main import mitmdump

def tcp_message(flow: tcp.TCPMessage):
    message = flow.messages[-1]
    old_content = message.contentpi
    message.content=message.content.repalce(b"foo", b"bar")


    ctx.log.info(
        "[tcp_message{}] from {} to {}:\n".format(
            "(modified)" if message.content != old_content else "",
            "client" if message.from_client else "server",
            "server" if message.from_client else "client",
            strutils.bytes_to_escaped_str(message.content)
        )
    )




if __name__ == '__main__':
    sys.argv=["","-p","5038","--rawtcp","--mode","reverse:http://localhost:5037/","-s",sys.argv[0],"-vv"]
    mitmdump()