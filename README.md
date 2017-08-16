# ProScanner

--------
利用线程池维护多线程，每个线程的任务由每个对应的队列中取出，使用了超时重传的机制，因为网络问题出现请求错误的会扔进队列继续请求，默认尝试10次，如失败url多建议降低线程提高重传次数。缺陷是多线程响应Interrupt还没处理好。。threadpool子线程都把主线程阻塞了。。。考虑以后换成multiprocess弄成守护进程应该就没问题了。。
And....字典是偷王师傅的。。他也写了一个很优秀的扫描器
github:https://github.com/WangYihang/SourceLeakHacker

--------

## Usage:
    -h or --help : For help
    -u or --url : The url you want to scan
    -t or --thread_num : The thread number you want to set, Default 30
    -c or --cookie : The cookie you want to use, Default Null
    -r or --retry : Retry times, Default 20
    
    Eg : python Pscanner.py -u localhost -t 30 -c 'user=admin;pass=123' -r 5

    ONLY FOR CTF Competition

--------
## TODO List:

[x] multithreading
[] Signal accept
[] coroutine
[x] description
[] random header
[x] beautify
[] dynamic dictionary

-------
## Test:

Url:http://218.76.35.75:65080/ (Web CTF)

Result:
- Success : 100%
- Cost : 26.5s
- Speed : 184.56 Url/s

![result](http://upload-images.jianshu.io/upload_images/6949366-6741f2b4c8979e0b.png?imageMogr2/auto-orient/strip)
