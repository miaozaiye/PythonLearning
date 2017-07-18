# ERROR 1045 (28000): Access denied for user 'linqiliang'@'localhost' (using password: NO)
这个错误困扰我很久了
又一个方式就是需要跳过
skip-grant-tables选项重启服务，修改密码

尝试方法如下：
第一步：
停止sql服务

第二步：
mysqld --skip-grant-tables &
跳过鉴权表启动

第三步：
修改密码
UPDATE mysql.user SET password=PASSWORD('NewPassord') WHERE user='root';

我现在的问题是第一步；
启动MySQL服务
sudo /usr/local/MySQL/support-files/mysql.server start

停止MySQL服务
sudo /usr/local/mysql/support-files/mysql.server stop

重启MySQL服务
sudo /usr/local/mysql/support-files/mysql.server restart

 查看当前进程

 最后，重新安装解决，通过workbench直接修改新密码 为123456


