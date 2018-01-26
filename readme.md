### 学习Cython

### 安装
1. 下载 [Cython‑0.27.3‑cp35‑cp35m‑win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#cython)

2. 安装 `pip install Cython‑0.27.3‑cp35‑cp35m‑win_amd64.whl`

3. 查看所需的VS版本
    `..\Python3\Lib\distutils\_msvccompiler.py`
    
    ```
    if version >= 14 and version > best_version:
        best_version, best_dir = version, vc_dir
    ```
    
3. 安装 VS2015
> version >= 14，所以需要安装VS2015

4. 配置环境变量
添加 `VS90COMNTOOLS=%VS140COMNTOOLS%` 即可


### 初级Demo
> `hello_cython`


### 速度测试
> `compute_cython`


### 说明
1. 在数字、浮点数等计算中Cython可以极大的提高性能，而这方面多线程几乎不能提高任何性能，有时候反而会降低。
2. 对于IO密集型应用，优化可以考虑使用多线程或者多进程方式，
对于计算密集型的场合，遇到瓶颈时可以考虑使用Cython或者封装C相关的模块。

