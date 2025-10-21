# 扩展1 ，获取文件中匹配的行
def match_lines_from_file(path, pattern):
    with open(path) as fp:
        for line in fp:
            if pattern in line:
                yield line.strip("\n")


# 扩展2： 日志文件转字典

def paser_log_records(lines):
    for line in lines:
        lever, message = line.split(":", 1)
        yield {"level": lever, "message": message}


if __name__ == '__main__':
    lines = match_lines_from_file("log.txt", "WARNING")
    for line in paser_log_records(lines):
        print(line)

# {'level': 'WARNING', 'message': ' Disk usage exceeding 85%'}
# {'level': 'WARNING', 'message': ' Almost out of beer'}
