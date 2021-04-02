import requests
url = "https://bbs-api.mihoyo.com/apihub/api/getAppSplash"
res_data = requests.get(url)
print(res_data.text)
#返回示例
'''
{
	"retcode": 0,
	"message": "OK",
	"data": {
		"splashes": [{
			"id": 556,
			"splash_image": "https://upload-bbs.mihoyo.com/upload/2021/04/02/b123569cdc87ac69c05b83a3573be775.jpeg",
			"app_path": "https://genshin.1752e.com/xsh5/index.html",
			"show_time": 3,
			"freq_type": 2,
			"game_id": 2
		}, {
			"id": 554,
			"splash_image": "https://upload-bbs.mihoyo.com/upload/2021/03/30/1a433c755435bb8811ca1dc3428fabb5.jpeg",
			"app_path": "mihoyobbs://article/5202101",
			"show_time": 3,
			"freq_type": 2,
			"game_id": 1
		}],
		"has_splash": true
	}
}
'''