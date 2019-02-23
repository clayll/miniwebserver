import requests
cooikes = {"talionnav_show_app":"0", "bid":"HDUDAXQGL84", "Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2":"1550399045", "_ga":"GA1.3.1298233735.1550399045","_gid":"GA1.3.1784054858.1550399045","_vwo_uuid_v2":"D4635162B015B651B3A873C1C4A256691|71f333885b8e49df7daf86c70c8d18f2", "_gat_UA-53594431-4":"1", "_gat_UA-53594431-6":"1", "Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2":"1550401319"}
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"}
r = requests.get("https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=18&count=18&loc_id=108288", headers=headers, cookies = cooikes)

print(r.content.decode())