"""
dict 客户端
"""

from socket import *
from getpass import getpass

ADDR = ('127.0.0.1',8000)
s = socket()
s.connect(ADDR)

# 二级界面
def login(name):
    print("""
            ====================welcome======================
             1. 查单词          2. 历史记录             3. 注销
            =================================================
            """)
    cmd = input("输入选像：")
    if cmd == '1':
        do_register()
    elif cmd == '2':
        do_login()
    elif cmd == '3':
        return
    else:
        print("请输入正确")


# 注册
def do_register():
    while True:
        name = input("User:")
        passwd = input("passwd:")
        passwd1 = input("again:")

        if (' ' in name) or (' ' in passwd):
            print("用户名和密码不能有空格")
            continue
        if passwd != passwd1:
            print("俩次密码不一致")
            continue

        msg = "R %s %s"%(name,passwd)
        # 发送请求
        s.send(msg.encode())

        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return


def do_login():
    name = input("User:")
    passwd = input("passwd:")
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())
    # 等待反馈
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功")
        login(name)
    else:
        print("登录失败")


# 创建网络连接
def main():
    while True:
        print("""
        =========================welcome=================
         1. 注册             2. 登录                3. 退出
        =================================================
        """)
        cmd = input("输入选像：")
        if cmd =='1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print("请输入正确")

if __name__ == '__main__':
    main()
