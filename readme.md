### 学习Cython


### Windows 安装
> Windows A popular option is to use the open source MinGW (a Windows distribution of gcc). 
See the appendix for instructions for setting up MinGW manually. 
Enthought Canopy and Python(x,y) bundle MinGW, but some of the configuration steps 
in the appendix might still be necessary. Another option is to use Microsoft’s Visual C.
 One must then use the same version which the installed Python was compiled with.

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

* 说明
    * 在VS2015中没有发现vcvarsall.bat，所以python3.5+VS没有成功。。。。
    * 解决办法：更换成pyhton2.7，采用[MinGW](http://docs.cython.org/en/latest/src/tutorial/appendix.html)的方式安装编译环境后，
    执行下面命令，生成了`.pyd`文件。
    ```
    pip2 install Cython
    python2 setup.py build_ext --inplace
    ```
    

### Ubuntn 安装
> Linux The GNU C Compiler (gcc) is usually present, or easily available through the package system. 
On Ubuntu or Debian, for instance, the command sudo apt-get install build-essential will fetch everything you need.

1. 安装 `pip install Cython`

2. 或者从官网下载后 `python setup.py install`


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


### 编译Cython代码
* Cython代码必须被编译，有两个阶段
    1. `.pyx`文件被`Cython`编译成`.c`文件。
    2. `.c`文件被`C compiler`编译成Linux的`.so`文件或Windows的`.pyd`文件，
    该文件可以被`Python`直接`import`导入。

* 编译Cython代码的几种方式

    1. 写一个`distutils` `setup.py`文件，这也是正常的和推荐的方式。
        1. 编写`hello.pyx`
        ```
        def say_hello_to(name):
            print("Hello %s!" % name)
        ```
        2. 编写相应的`setup.py`脚本
        ```
        from distutils.core import setup
        from Cython.Build import cythonize
        
        setup(
          name = 'Hello world app',
          ext_modules = cythonize("hello.pyx"),
        )
        ```
        3. 执行编译
        ```
        python3 setup.py build_ext --inplace
        ```
        
            其他说明：
            1. python3 setup.py build
                * 编译(过程中会生成.so文件，直接把该文件拷贝出来使用就行)
                * 为了使用方便，运行脚本直接和so文件放在一个目录下，使用import导入即可。
                
            2. python3 setup.py install
                * 安装(执行install后会把模块复制到python系统目录下)
                
        4. 使用
        ```
        from hello import say_hello_to
        say_hello_to("ALISURE")
        ```
        
    2. 使用`pyximport`，像导入`.py`一样导入`.pyx`(using distutils to compile and build in the background)
        * 在`pyximport_cython`文件夹中
        
    3. 使用`cython`命令行工具手动从`.pyx`产生`.c`文件，然后手动编译`.c`文件产生能够直接被`pyhton`导入的文件。
        以`pyximport_cython`中的`primes.pyx`为例
        * 命令行下执行命令：
        ```
        cd pyximport_cyhton
        cython primes.pyx
        gcc -c -fPIC -I /usr/include/python3.5 primes.c
        gcc -shared primes.o -o primes.so
        ```
        * 使用
        ```
        import primes
        print(primes.primes(1000))
        ```
    
    4. reference
        * [cython: source_files_and_compilation](http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html#compilation)   

    

### 如何优化
* 静态类型(static typing)：使用 `cdef`关键字
    * 示例代码在`types_cython`中
    * For performance critical code, it is often helpful to add static type declarations, 
    as they will allow Cython to step out of the dynamic nature of 
    the Python code and generate simpler and faster C code.
    * 类型声明导致源代码更加冗余、降低了可读性，只建议`使用在能提升性能的关键地方`。
    * 所有的C类型都可以声明，包括int/floating point/complex numbers/structs/unions/pointer
    * 例子：
        * 纯Python代码(run `types_demo.py` time is 0.657677s)
        ```
        def f(x):
            return x**2-x
        
        def integrate_f(a, b, N):
            s = 0
            dx = (b-a)/N
            for i in range(N):
                s += f(a+i*dx)
            return s * dx
        ```
        * 简单地使用Cython编译(run `types_demo.py` time is 0.555587s)
        
        * 增加类型声明(run `types_demo.py` time is 0.086425s)
        ```
        def f(double x):
            return x**2-x
        
        def integrate_f(double a, double b, int N):
            cdef int i
            cdef double s, dx
            s = 0
            dx = (b-a)/N
            for i in range(N):
                s += f(a+i*dx)
            return s * dx
        ```
        
* 函数类型(Typing Functions)
    * Python中的函数调用非常耗费时间。
    * `except ? *`
        * except-modifier
    * `cpdef`
        * Python wrapper
        * overridden
    * 副作用
        * 函数名称不能使用Python-space。
        * 不能在运行时改变函数的内容。
    * 例子：
        * Typing Functions(run `types_demo.py` time is 0.051151s)
        ```
        cdef double f(double x):
            return x**2-x
        ```

> [Determining where to add types](http://docs.cython.org/en/latest/src/quickstart/cythonize.html#determining-where-to-add-types)

* Calling C functions
    * Cython给出了调用原生C库函数的快捷方式，所有能快捷调用的方法在 
    [Cyhton/Includes](https://github.com/cython/cython/tree/master/Cython/Includes) 中
        ```
        from libc.stdlib cimport atoi

        cdef parse_charptr_to_py_int(char* s):
            assert s is not NULL, "byte string value is NULL"
            return atoi(s)   # note: atoi() has no error detection!
        ```
        ```
        from libc.math cimport sin

        cdef double f(double x):
            return sin(x*x)
        ```
        
    * 外部声明（External declarations）
        ```
        cdef extern from "math.h":
            double sin(double x)
        ```
    * 命名参数（Naming parameters）
        * 签名声明(不能使用keyword arguments)
        ```
        cdef extern from "string.h":
            char* strstr(const char*, const char*)
        ```
        * 参数有名称
        ```
        cdef extern from "string.h":
            char* strstr(const char *haystack, const char *needle)
        ```
        * 可以使用关键字参数调用
        ```
        cdef char* data = "hfvcakdfagbcffvschvxcdfgccbcfhvgcsnfxjh"

        pos = strstr(needle='akd', haystack=data)
        print pos != NULL
        ```

* Using C libraries(使用C库)
    > 示例代码在`c_library_cython`中，
    参考：[Using C libraries](http://docs.cython.org/en/latest/src/tutorial/clibraries.html#id1)
    
    1. 下载[CAlg](http://fragglet.github.io/c-algorithms/) / 
    [CAlg](https://github.com/fragglet/c-algorithms/releases)
    
    2. 安装CAlg(`INSTALL`文件中有安装说明)
        * 目的是安装 `libcalg/queue.h` 文件
        * 默认安装成功后会在`/usr/local/lib`下出现`libcalg.so`，
        在`/usr/local/include`下出现`libcalg-1.0`。
        * `sudo make check` 是可选的
        * `make clean` 只清除二进制和对象文件(binaries and object files)
        * `make distclean` 也清除 `sudo ./configure` 中创建的文件
        * `make install` 默认安装到`/usr/local/bin`,`/usr/local/man`等位置，
        可以指定安装地址`make install --prefix=PATH`
        * 其他问题详见`INSTALL`文件
        
        ```
        cd c-algorithms-1.2.0
        sudo ./configure
        sudo make
        sudo make check
        sudo make install
        make clean
        make distclean
        ```
    
    3. 在`.pxd`文件中重定义C API接口，在`c_library_cython/cqueue.pxd`中
    
    4. 在`.pyx`文件中编写包装类，在`c_library_cython/queue.pyx`中
    
    5. 在`setup.py`文件中编写setup文件
        ```
        ext_modules = cythonize([
            Extension("queue", ["queue.pyx"], libraries=["calg"])
            ])
        ```
    
    6. 编译
        ```
        CFLAGS="-I/usr/local/include/libcalg-1.0" LDFLAGS="-L/usr/local/lib" python3 setup.py build_ext -i
        ```
    
    7. 调用
        ```
        from c_library_cython.queue import Queue
        q = Queue()
        q.append(5)
        print(q.peek())
        print(q.pop())
        ```
    
    8. 遇到的错误
        * 编译阶段要注意pyhton的版本，我的需要使用python3
        * `ImportError: libcalg.so.0: cannot open shared object file: No such file or directory`
            * 环境变量中配置：LD_LIBRARY_PATH=/usr/local/lib
    
    9. OVER


### Pure Python Mode
* [Pure Python Mode](http://docs.cython.org/en/latest/src/tutorial/pure.html)


### Working with NumPy
* [Working with NumPy](http://docs.cython.org/en/latest/src/tutorial/numpy.html)


### 教程
* [cython](http://cython.org/)


### 说明
1. 在数字、浮点数等计算中Cython可以极大的提高性能，而这方面多线程几乎不能提高任何性能，有时候反而会降低。
2. 对于IO密集型应用，优化可以考虑使用多线程或者多进程方式，
对于计算密集型的场合，遇到瓶颈时可以考虑使用Cython或者封装C相关的模块。

