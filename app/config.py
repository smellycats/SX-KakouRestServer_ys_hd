# -*- coding: utf-8 -*-


class Config(object):
    # 密码 string
    SECRET_KEY = 'showmethemoney'
    # 服务器名称
    HEADER_SERVER = 'SX-KakouRestServer_ys_hd'
    # 加密次数 int
    ROUNDS = 123456
    # token生存周期，默认2小时 int
    EXPIRES = 7200
    # 数据库连接 string
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@123.123.123.123:5432/imos'
    # 数据库连接绑定 dict
    SQLALCHEMY_BINDS = {}
    # 连接池大小 int
    #SQLALCHEMY_POOL_SIZE = 10
    # 缓存类型
    CACHE_TYPE = 'simple'#'redis'
    #CACHE_REDIS_HOST = '10.47.223.147'
    #CACHE_REDIS_PORT = 6379
    #CACHE_REDIS_DB = 9
    #CACHE_REDIS_PASSWORD = ''
    # 缓存时间
    #CACHE_TIME = 60 * 30
    # 号牌颜色ID
    HPYS2CODE = {
        u'白牌': {'id': 0, 'code': 'WT'},
        u'黄牌': {'id': 1, 'code': 'YL'},
        u'蓝牌': {'id': 2, 'code': 'BU'},
        u'黑牌': {'id': 3, 'code': 'BK'},
        u'绿牌': {'id': 4, 'code': 'GN'},
        u'其他': {'id': 9, 'code': 'QT'}
    }
    # 号牌颜色ID
    HPYS_DICT = {
        0: {'name': u'白牌', 'code': 'WT'},
        1: {'name': u'黄牌', 'code': 'YL'},
        2: {'name': u'蓝牌', 'code': 'BU'},
        3: {'name': u'黑牌', 'code': 'BK'},
        4: {'name': u'绿牌', 'code': 'GN'},
        9: {'name': u'其他', 'code': 'QT'}
    }
    FXBH2NAME = {
        1: u'由东往西',
        2: u'由西往东',
        3: u'由南往北',
        4: u'由北往南',
        5: u'由东南往西北',
        6: u'由西北往东南',
        7: u'由东北往西南',
        8: u'由西南往东北'
    }
    # 方向代码
    FXBH2CODE = {
        u'进城': 'IN',
        u'出城': 'OT',
        u'由东往西': 'EW',
        u'由西往东': 'WE',
        u'由南往北': 'SN',
        u'由北往南': 'NS'
    }
    # 方向代码
    CODE2FXBH = {
        'IN': u'进城',
        'OT': u'出城',
        'EW': u'由东往西',
        'WE': u'由西往东',
        'SN': u'由南往北',
        'NS': u'由北往南'
    }
    # 卡口编号
    KKBH2KKDD = {
        '2E-3E-8E': '441323101',
        '2E-3E-70': '441323101',
        '2E-3E-92': '441323102',
        '2E-3E-75': '441323102',
        '2F-7A-44': '441323103',
        '2F-7A-41': '441323103',
        '2E-3E-8F': '441323104',
        '2E-3E-71': '441323104',
        '2E-3E-8C': '441323105',
        '2F-7A-45': '441323105',
        '2F-7A-42': '441323105',
        '2F-7A-47': '441323105',
        '2E-3E-8B': '441323106',
        '2E-3E-91': '441323106',
        '2E-3E-83': '441323106',
        '2E-3E-77': '441323106',
        '2F-7A-43': '441323107',
        '2F-7A-46': '441323107',
        '2E-3E-6E': '441323108',
        '2E-3E-6F': '441323108'
    }
    KKDD2NAME = {
        '441323101': u'安墩石塘至紫金路段',
        '441323102': u'白花至良井路段',
        '441323103': u'多祝缉毒卡哨',
        '441323104': u'高谭至紫金路段',
        '441323105': u'焦田铁马关卡口',
        '441323106': u'平山至吉隆好招楼路段',
        '441323107': u'松坑至紫金路段',
        '441323108': u'新庵横坑至海丰路段'
    }


class Develop(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


class Testing(Config):
    TESTING = True
