# encoding=utf-8
## 利用faker自动生成日志
## https://www.jianshu.com/p/6bd6869631d9

from faker import Faker
import time
f=Faker()

for i in range(1,100):
    print(f.name()+","+f.address()+","+f.ipv4()+","+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+","+f.image_url()+","+f.numerify())
