from urllib import request
import re
import os
import random
import math
from colorama import init
import logging


LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=r"D:\Tiles\arcgisonline\output.log"
                    )

init(autoreset=True)

agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1']


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) +
                                (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def getimg(Tpath, Spath, x, y):
    try:
        if (os.path.exists(Spath) and os.path.getsize(Spath) > 0):
            print(str(x) + '_' + str(y) + '已存在')
            return
        f = open(Spath, 'wb')
        req = request.Request(Tpath)
        req.add_header('User-Agent', random.choice(agents))
        pic = request.urlopen(req, timeout=60)

        f.write(pic.read())
        f.close()
        print(str(x) + '_' + str(y) + '\033[0;32;40m\t下载成功\033[0m')
    except Exception:
        logging.warning(Tpath + '下载失败')
        print(str(x) + '_' + str(y) + '\033[0;31;40m\t下载失败\033[0m')
        #getimg(Tpath, Spath, x, y)


rootDir = "D:\\Tiles\\arcgisonline\\"

for zoom in range(1, 8):
    print("正在下载  zoom:" + str(zoom))
    # for x in range(lefttop[0], rightbottom[0]):
    #     for y in range(lefttop[1], rightbottom[1]+1):
    for x in range(0, 2**zoom):
        for y in range(0, 2**zoom):
            # arcgisOnLine
            tilepath = 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/' + \
                str(zoom)+'/'+str(y)+'/'+str(x)+''
            path = rootDir + str(zoom) + "\\" + str(x)
            if not os.path.exists(path):
                os.makedirs(path)
            getimg(tilepath, os.path.join(path, str(y) + ".png"), x, y)

print('下载完成')
