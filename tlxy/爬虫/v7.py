#urlerror

from urllib import request, error

if __name__ == '__main__':
    # url = 'http://www.baidu.com'
    url = 'http://blog.tengyue.infox'
    try:
        req = request.Request(url)
        rsp =request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLerror: {0}".format(e.reason))
    except Exception as e:
        print(e)
