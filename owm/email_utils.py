# ! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 开发者
development_list = ['ouweiming@clickwifi.net']
# 运营
operations_list = ['liaojingjing@clickwifi.net']
operations_list_demo = ['464226728@qq.com']

# 配置发件邮件信息
mail_host = "smtp.163.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "13249767060@163.com"  # 用户名
mail_pass = "a123456789"  # 密码
mail_postfix = "163.com"  # 邮箱的后缀，网易就是163.com


# 发送邮件 to_list：发送邮件列表  sub:主题 content:正文
def send_mail(to_list, sub, content, retry=3):
    me = "clickwifi" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = formataddr(["ClickWiFi", mail_user])
    msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    print(msg)
    for i in range(retry):
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)  # 连接服务器
            server.login(mail_user, mail_pass)  # 登录操作
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            print("邮件发送成功")
            return True
        except Exception as e:
            print(str(e))
    print("邮件发送失败")
    return False


def send_development(sub, content):
    send_mail(development_list, sub, content)


def send_operations(sub, content):
    send_mail(operations_list, sub, content)


def send_all(sub, content):
    send_mail(development_list + operations_list, sub, content)


if __name__ == '__main__':
    send_mail(development_list + operations_list_demo, "飞凡数据更新完毕", "飞凡数据更新完毕\n  耗时：")













