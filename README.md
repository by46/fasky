# flasky

##  数据库迁移

如果对模型进行了修改，需要迁移数据库，可以通过执行如下命令来解决：

```shell
# 生成迁移脚本
python shell.py db migrate
# 执行迁移脚本
python shell.py db upgrade

```
