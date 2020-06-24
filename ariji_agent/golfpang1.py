import requests
import json
import datetime

s = requests.Session()

r = s.get('http://www.golfpang.com/index.htm', stream = True)

print(r.text)




# # 골프몬은 post방식으로 post방식 url적용
# json_url = 'http://www.golfpang.com/web/round/booking_tblList.do'

# # 현재시간
# dt = datetime.datetime.now()

# # 골프장명
# cc_name = '아리지cc'

# # 날짜 하루씩 증가
# for i in range(1,30,1) :
#     ndt = dt + datetime.timedelta(days=i)
#     ndt_display = ndt.strftime("%Y-%m-%d")    

#     # Form Data 값 넣어주기(post 방식)
#     data = {'pageNum' : '1', 'rd_date' : ndt_display, 'sector' : '5', 'clubname' : '58'}

#     json_data = requests.post(json_url,data = data).json()
#     print(json_data)

#     '''    
#     for j in json_data:
#         if j['name'] == cc_name:
#             data1 = {'selectDATE': ndt_display, 'bokpTYPE': '1', 'locationTYPE':'999', 'golfcourse':cc_name, 'startNUM':'0','endedNUM':'999','teeup_time_search':'0'}
#             json_data1 = requests.post(json_url,data = data1).json()

#             for k in json_data1:
#                 print(k['teetime'] + ' ' + k['greenFee'] + ' ' + k['nick_name'] + ' ' + k['phone'])
#     '''
