# douban_backup

> 声明：此项目只用来备份自己在豆瓣标记的读过的书，只是作为一个备份，不作它用。(看过的电影也是基本上差不多的)

**代码功能实现：**：

将Douban 读过的书的记录保存到 db/douban.db 数据库（sqlite）中和ex/douban.xlsx 文件中。


**项目文件说明：**：
```
douban_backup
- db
  - douban.db
- ex
  - douban.xlsx
- books.py
- douban.sql
- douban_config.py
- main.py
- z_db.py
```

> db/douban.db : sqlite数据库文件，最后保存的数据都在这里
> ex/douban.xlsx : Excel文件，最后保存的数据同步保存在这里
> books.py ：调用 main()方法，将Douban 读过的书的记录保存到数据库books表中和douban.xlsx 文件中
> douban.sql : 表创建的sql语句（books表）
> douban_config.py ：配置文件
> main.py ：主文件
> z_db.py ：数据库操作文件

### 一、在douban_config.py 文件中填写配置信息

**1.豆瓣登录的用户名和密码**
``` python
douban_id = '[豆瓣登录id(邮箱名)]'
douban_pwd = '[豆瓣登录密码]'
```

**2.关于webdriver，自己装好了添加到系统环境变量**

### 二、运行main.py中的方法备份

1.先运行init_create_table()方法初始化，创建数据库中的表

2.备份看过的书
去掉 `#books.main()`前面的 #注释，再 注释`init_create_table()`方法即可运行。

### 三、必看

更新于2022/05/12，采用selenium4版本，跳过selenium的webdriver检测（登录时需要手动划验证图片，但可以提前登录）

跳过selenium的webdriver检测，使用的是本地debugger模式。所以，需要自己在本地用debugger模式打开浏览器，再运行程序。

**操作方法：**

1).第一步，用Windows PowerShell或命令提示符运行chrome.exe

找到Chrome浏览器的安装路径，比如我的在：`C:\Program Files (x86)\Google\Chrome\Application`，里面就有chrome.exe程序。

运行以下命令：
```bash
cd "C:\Program Files (x86)\Google\Chrome\Application"

.\chrome.exe --remote-debugging-port=9222 --user-data-dir=D:\cdsf
```

> remote-debugging-port：是代码中指定的端口debuggerAddress；
> user-data-dir：随便指定一个目录就行（真实没有这个目录也没关系，名字随便取）

运行完后会打开Chrome浏览器。

2).第二步，运行 main.py

在main.py中运行程序。就会在打开的Chrome浏览器中正常运行了。

PS.如果自己提前登录过，还能记住密码。再登录的时候可以不需要登录了。（所以登录部分的代码做了这个判断）