### 学习Cython


### Windows 安装
1. 下载 [Cython‑0.27.3‑cp35‑cp35m‑win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#cython)

2. 安装 `pip install Cython‑0.27.3‑cp35‑cp35m‑win_amd64.whl`

3. 查看所需的VS版本
    `..\Python3\Lib\distutils\_msvccompiler.py`
    
    ```
    if version >= 14 and version > best_version:
        best_version, best_dir = version, vc_dir
    ```

4. 安装 VS2015
> version >= 14，所以需要安装VS2015

5. 配置环境变量
添加 `VS90COMNTOOLS=%VS140COMNTOOLS%` 即可


### Ubuntn 安装
1. 安装 `pip install Cython`

2. ...


### 初级Demo
> `hello_cython`

1. 编写三个文件
    1. hello.pyx
        ```
        def print_hello(name):
            print("hello {}".format(name))
            pass
        ```
    2. setup.py
        ```
        from distutils.core import setup
        from distutils.extension import Extension
        from Cython.Distutils import build_ext
        
        setup(
            name="Hello pyx",
            cmdclass={'build_ext': build_ext},
            ext_modules=[Extension("hello",["hello.pyx"])]
        )
        ```
    3. __init__.py
        ```
        from hello import *
        ```
    
2. 编译
    ```
    python3 setup.py build_ext --inplace
    ```
    
3. 调用
    ```
    from hello_cython import hello
    hello.print_hello("xxx")
    ```

4. 结果
    ```
    /usr/bin/python3.5 /home/z840/ALISURE/python_cython/python-cython/hello_demo.py
    hello xxx
    ```


### 速度测试
> `compute_cython`

0. compute.py
    * 全部用python实现
    * 执行`compute_demo.py`
    * 运行时间
        ```
        run 1 time: 0.651578 s
        run 2 time: 1.620753 s
        ```
    
1. compute_cython.pyx
    * 用cython编译
    * 执行`compute_demo.py`
    * 运行时间
        ```
        run 1 time: 0.573591 s
        run 2 time: 1.538987 s
        ```
    
2. compute_cython2.pyx
    * 使用C中的变量类型，然后用cython编译
    * 执行`compute_demo.py`
    * 运行时间
        ```
        run 1 time: 0.002526 s
        run 2 time: 1.525995 s
        ```
    
3. compute_cython3.pyx
    * 使用C中的库函数，使用C中的变量类型，然后用cython编译
    * 执行`compute_demo.py`
    * 运行时间
        ```
        run 1 time: 0.002509 s
        run 2 time: 0.382405 s
        ```


### 编译入门
1. python3 setup.py build
    * 编译(过程中会生成.so文件，直接把该文件拷贝出来使用就行)
    * 为了使用方便，运行脚本直接和so文件放在一个目录下，使用import导入即可。
    
2. python3 setup.py install
    * 安装(执行install后会把模块复制到python系统目录下)




### 说明
1. 在数字、浮点数等计算中Cython可以极大的提高性能，而这方面多线程几乎不能提高任何性能，有时候反而会降低。
2. 对于IO密集型应用，优化可以考虑使用多线程或者多进程方式，
对于计算密集型的场合，遇到瓶颈时可以考虑使用Cython或者封装C相关的模块。


