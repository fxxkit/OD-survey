# -*- coding: utf-8 -*-

SITE_TITLE = u"App 點菜"

APPLE_BADGE = 'app-store-badge.svg'
GOOGLE_BADGE = 'google-play.png'

DEMO_URL = 'https://moqups.com/jordan00830@gmail.com/rwGGjJuF/p:afc8a2376'
MONGODB_URI = 'mongodb://heroku_app33034248:pg9t7en0b41cmbglhniuf4vf8s@ds031611.mongolab.com:31611/heroku_app33034248'

LOOP_CONTROL = True
LOOP_INDICATORS = False
LOOP_IMAGES = [
    {
        'order': 0,
        'file': 'demo/qrcode.png',
        'stay': 20,
        'url': '#',
    },
    {
        'order': 1,
        'file': 'demo/menu.png',
        'stay': 20,
        'url': '#',
    },
    {
        'order': 2,
        'file': 'demo/menu_2.png',
        'stay': 20,
        'url': '#',
    },
    {
        'order': 3,
        'file': 'demo/menu_3.png',
        'stay': 20,
        'url': '#',
    },
    {
        'order': 4,
        'file': 'demo/done.png',
        'stay': 20,
        'url': '#',
    },    
    {
        'order': 5,
        'file': 'demo/history.png',
        'stay': 20,
        'url': '#',
    },
    {
        'order': 6,
        'file': 'demo/history_2.png',
        'stay': 20,
        'url': '#',
    },
]
LOOP_INTERVAL = 20

scenarios = [(u'café', 'cafe.jpg', [u'星巴克']),
    (u'熱炒', 'taiwan.jpg', []), 
    (u'居酒屋', 'izakaya.jpg', []), 
    (u'拉麵', 'ramen.jpg', []), 
    (u'酒吧', 'bar.jpg', []), 
    (u'下午茶', 'tea.jpg', []), 
    (u'早餐店', 'brunch.jpg', ['']),
    (u'西餐', 'steak.jpg', [u'王品', u'茹絲葵'])
]
sections = {
    'demo-heading': [
        {
            'text': u'如果,',
            'subTxt': u'點菜可以這樣:',
            'phone': True,
            'textClass': 'fc-black',
            'subTxtClass': 'fc-black',                  
            'cssClass': 'b-w',
            'image': { 'demo': sorted(LOOP_IMAGES, key=lambda x:x['order'])[1]['file'] },
            'loop': True,
        },
        {
            'text': u'輕輕一滑',
            'subTxt': u'點了什麼都一目了然  <i class="fa fa-smile-o"></i>',
            'triTxt': u'',
            'phone': True,
            'textClass': 'fc-black',
            'subTxtClass': 'fc-black',
            'cssClass': 'b-w',
            'image': {'demo': 'demo/history.png' }
        },
        {
            'text': u'無論是在',
            'subTxt': u'文青的咖啡廳，還是熱鬧的快炒店',
            'scenario': True,
            'left': '4', 'right': '8',
            'textClass': 'fc-white',
            'subTxtClass': 'fc-white',
            'cssClass': 'bg-theme-a-grey',
        },
        {
            'text': u'點餐',
            'subTxt': u'可以如此簡單！',
            'textClass': 'fc-black',
            'badges': False,
            'phone': True,
            'cssClass': '',
            'image': {'demo': 'demo/done.png' }
        },
        {
            'text': u'您覺得,',
            'subTxt': u'用 APP 點菜如何?',
            'triTxt': u'點選來選擇意見 <i class="fa fa-hand-o-right"></i>',
            'form-opinions': True,
            'textClass': 'fc-black fs-48',
            'subTxtClass': 'fc-black',
            'triTxtClass': 'fc-333 pt-24',
            'cssClass': 'pt-108 bg-theme-a-white pb-108',
            'left': '5', 'right': '7',
        },
        {
            'text': u'您覺得,',
            'subTxt': u'哪些場合適合用 APP 點菜?',
            'triTxt': u'點一下吧 <i class="fa fa-hand-o-right"></i>',
            'form-scenario': True,
            'textClass': 'fc-white fs-48',
            'subTxtClass': 'fc-white',
            'triTxtClass': 'fc-white pt-24',
            'cssClass': 'bg-themed',
            'left': '4', 'right': '8',
            'id': 'opinion-scenario',
        },
        {
            'text': u'等等',
            'subTxt': u'我還有話要說：',
            'form-comment': True,
            'textClass': 'fc-white fs-48',
            'subTxtClass': 'fc-white',
            'cssClass': 'pt-64 pb-64 bg-333',
            'left': '5', 'right': '7'
        },
        {
            'text': u'謝謝！',
            'subTxt': u'我們很珍惜您寶貴的意見',
            'form-thanks': True,
            'textClass': 'fc-black fs-48',
            'subTxtClass': 'fc-black',
            'cssClass': 'pt-108 pb-160',
            'left': '5', 'right': '7'
        },
    ],
    'demo-images': [
        'odapp.png',
        'odapp.png',
    ],
    'form-heading': [
        {
            'text': u'',
            'subTxt': u'',
        },
    ]
}

form = {
    'text': ''
}

ages = list(enumerate([u'10 以下', u'10 - 20', u'20 - 30', u'30 - 40', u'40 - 50', u'50 - 60', u'60 以上']))

opinions = [
    { 'id': 'notbad',       'cht': u'不錯',   'btn': 'success',  'score': 3, },
    { 'id': 'awesome',      'cht': u'讚啦',   'btn': 'success',  'score': 5, },
    { 'id': 'soso',         'cht': u'普通',   'btn': 'primary',  'score': 1,},
    { 'id': 'useless',      'cht': u'沒啥用', 'btn': 'warning',  'score': 0,},
    { 'id': 'inconvenient', 'cht': u'很麻煩', 'btn': 'warning',  'score': -1,},
    { 'id': 'sucks',        'cht': u'糟透了', 'btn': 'danger',   'score': -2,},
]
