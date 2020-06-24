import requests
import json
import datetime
import html2text

# 골프몬은 post방식으로 post방식 url적용
json_url = 'http://www.golfmon.net/renewal/api/post_booking_plaza_board.php'

# 현재시간
dt = datetime.datetime.now()

# 골프장명
cc_name = '아리지cc'

# 날짜 하루씩 증가
for i in range(1,30,1) :
    ndt = dt + datetime.timedelta(days=i)
    ndt_display = ndt.strftime("%Y-%m-%d")    

    # Form Data 값 넣어주기(post 방식)
    data = {'selectDATE': ndt_display, 'bokpTYPE': '1', 'locationTYPE':'2', 'startNUM':'0','endedNUM':'100','teeup_time_search':'0'}

    # data json으로 받기
    json_data = requests.post(json_url,data = data).json()

    
    for j in json_data:
        
        # 골프장명 입력
        if j['name'] == cc_name:
            data1 = {'selectDATE': ndt_display, 'bokpTYPE': '1', 'locationTYPE':'999', 'golfcourse':cc_name, 'startNUM':'0','endedNUM':'999','teeup_time_search':'0'}
            json_data1 = requests.post(json_url,data = data1).json()

            # data 정리
            for k in json_data1:
                agent = k['teetime'] + ' ' + k['greenFee'] + ' ' + k['nick_name'] + ' ' + k['phone']
                print(agent)

                # 저장하기
                f = open('./golfmon_agent.text', 'a', encoding="UTF-8")
                f.writelines(agent)
                f.close

