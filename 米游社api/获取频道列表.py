import requests
url = "https://bbs-api.mihoyo.com/apihub/api/getGameList"
res_data = requests.get(url)
print(res_data.text)
#返回示例
'''
{
	"retcode": 0,
	"message": "OK",
	"data": {
		"list": [{
			"id": 2,
			"name": "原神",
			"en_name": "ys",
			"app_icon": "https://upload-bbs.mihoyo.com/game/ys/app_icon.png",
			"icon": "https://upload-bbs.mihoyo.com/game/ys/icon.png",
			"search_trend_word": "原神",
			"level_image": "https://upload-bbs.mihoyo.com/game/ys/levelImage.png",
			"level_text_color": "F3D8A8",
			"topic_num": 1,
			"op_name": "hk4e",
			"main_color": "BDA575",
			"has_wiki": true
		}, {
			"id": 5,
			"name": "大别野",
			"en_name": "dby",
			"app_icon": "https://upload-bbs.mihoyo.com/game/dby/app_icon.png",
			"icon": "https://upload-bbs.mihoyo.com/game/dby/app_icon.png",
			"search_trend_word": "大别野",
			"level_image": "https://upload-bbs.mihoyo.com/game/dby/levelImage.png",
			"level_text_color": "FFFFFF",
			"topic_num": 1,
			"op_name": "plat",
			"main_color": "19A3FF",
			"has_wiki": false
		}, {
			"id": 1,
			"name": "崩坏3",
			"en_name": "bh3",
			"app_icon": "https://upload-bbs.mihoyo.com/game/bh3/app_icon.png",
			"icon": "https://upload-bbs.mihoyo.com/game/bh3/icon.png",
			"search_trend_word": "崩坏3",
			"level_image": "https://upload-bbs.mihoyo.com/game/bh3/levelImage.png",
			"level_text_color": "FFFFFF",
			"topic_num": 1,
			"op_name": "bh3",
			"main_color": "01C3FF",
			"has_wiki": false
		}, {
			"id": 4,
			"name": "未定事件簿",
			"en_name": "wd",
			"app_icon": "https://upload-bbs.mihoyo.com/game/wd/app_icon.png",
			"icon": "https://upload-bbs.mihoyo.com/game/wd/icon.png",
			"search_trend_word": "未定事件簿 ",
			"level_image": "https://upload-bbs.mihoyo.com/game/wd/levelImage.png",
			"level_text_color": "FBF2E9",
			"topic_num": 1,
			"op_name": "nxx",
			"main_color": "A39EE0",
			"has_wiki": true
		}, {
			"id": 3,
			"name": "崩坏学园2",
			"en_name": "bh2",
			"app_icon": "https://upload-bbs.mihoyo.com/game/bh2/app_icon.png",
			"icon": "https://upload-bbs.mihoyo.com/game/bh2/icon.png",
			"search_trend_word": "崩坏学园",
			"level_image": "https://upload-bbs.mihoyo.com/game/bh2/levelImage.png",
			"level_text_color": "FFFFFF",
			"topic_num": 1,
			"op_name": "bh2",
			"main_color": "57BDDB",
			"has_wiki": false
		}]
	}
}
'''