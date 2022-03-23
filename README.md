# conda-mirror
最近conda的镜像不太稳定，我自己之前也一直被镜像的问题折磨，大概是用的人太多，有时候就很慢。
所以我写了一个自动检测conda镜像源的响应速度并进行切换的脚本，应该会方便一些。

## 使用方法
先下载下来

```shell
git clone https://github.com/RestlessTail/conda-mirror.git
```

然后运行

```shell
python3 conda-mirror.py
```

就好了

+ 注意如果镜像站用的是https协议的话需要`conda config --set ssl_verify True`
