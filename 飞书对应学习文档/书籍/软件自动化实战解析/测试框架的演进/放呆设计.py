#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28


class QaFtpClient:

    def connect(self):
        pass

    def download(self, remote_path):
        pass

    def disconnect(self):
        pass


def test_ftp():
    ftp_client = QaFtpClient()

    ftp_client.connect()

    downloaded_file1 = ftp_client.download('remote_path_1')

    do_some_logic()

    downloaded_file2 = ftp_client.download('remote_path_2')

    do_some_other_logic()

    # do yet another logic
    downloaded_file3 = ftp_client.download('remote_path_3')

    ftp_client.disconnect()