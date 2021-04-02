import requests
url = "https://bbs-api.mihoyo.com/apihub/api/getAppConfig"
res_data = requests.get(url)
print(res_data.text)
#返回示例
'''
{
	"retcode": 0,
	"message": "OK",
	"data": {
		"config": {
			"point_mall": "1",
			"max_image_upload_size": "20971520",
			"wd_obc_open": "1",
			"game_preorder": "1",
			"upload_log_disable": "0",
			"web_cert_guide": "/article/1582654",
			"game_preorder_home": "1",
			"showing_point": "1",
			"ys_obc_open": "1",
			"game_record_url": "https://webstatic.mihoyo.com/app/community-game-records/index.html?v=6",
			"role_manage_enable": "1",
			"transformer_area": "1",
			"show_creator_video_data": "1",
			"showing_creator_center": "1",
			"user_protocol_version": "1.0",
			"im_config": "[     {         \"name\":\"崩坏学园2\",         \"path\":\"mihoyobbs://forum/32\",         \"background\":\"http://upload-bbs.mihoyo.com/im/bh2.png\"     },     {         \"name\":\"崩坏3\",         \"path\":\"https://webstatic.mihoyo.com/community/event/bh3-bbs-customer-claim/index.html#/customer\",         \"background\":\"http://upload-bbs.mihoyo.com/im/bh3.png\"     },     {         \"name\":\"原神\",         \"path\":\"https://webstatic.mihoyo.com/ys/event/im-service/index.html?bbs_auth_required=true\u0026sign_type=2\u0026auth_appid=im_ccs\u0026authkey_ver=1\u0026lang=zh-cn\u0026app_client=bbs\u0026game_biz=hk4e_cn\u0026bbs_game_role_required=hk4e_cn#/\",         \"background\":\"http://upload-bbs.mihoyo.com/im/ys.png\"     },     {         \"name\":\"未定事件簿\",         \"path\":\"https://webstatic.mihoyo.com/nxx/event/im-service/index.html?bbs_auth_required=true\u0026sign_type=2\u0026auth_appid=im_ccs\u0026authkey_ver=1\u0026lang=zh-cn\u0026app_client=bbs\u0026game_biz=nxx_cn\u0026bbs_game_role_required=nxx_cn#/\",         \"background\":\"http://upload-bbs.mihoyo.com/im/wd.png\"     },     {         \"name\":\"米游社\",         \"path\":\"https://webstatic.mihoyo.com/bbs/event/im-service/index.html?bbs_auth_required=true\u0026sign_type=2\u0026auth_appid=im_ccs\u0026authkey_ver=1\u0026lang=zh-cn\u0026app_client=bbs\u0026game_biz=bbs_cn#/\",         \"background\":\"http://upload-bbs.mihoyo.com/im/mys.png\"     } ]",
			"feedback_url": "mihoyobbs://topic/150",
			"max_video_upload_size": "2147483648",
			"download_game": "1",
			"obc_open": "1",
			"bilibili_video_play_type": "2",
			"my_prize_url": "https://webstatic.mihoyo.com/bbs/event/bbs-logistics/index.html?bbs_presentation_style=fullscreen\u0026bbs_auth_required=true#/",
			"show_upload_video_button": "0",
			"app_cert_guide": "mihoyobbs://article/1582654",
			"showing_mall": "1"
		}
	}
}
'''