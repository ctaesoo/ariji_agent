import requests
import re
import datetime
from bs4 import BeautifulSoup
import html2text

json_url = 'http://www.golfpang.com/web/round/booking_tblList.do'

dt = datetime.datetime.now()
today = dt.strftime("%Y%m%d%H%M%S")    
file_name = './'+today+'.html'
cc_name = '58'  #아리지=58  신라:53

for i in range(1,20,1) :
    ndt = dt + datetime.timedelta(days=i)
    ndt_display = ndt.strftime("%Y-%m-%d")    

    data = {'pageNum':'1','bkOrder':'','rd_date': ndt_display, 'apmp': '', 'sector':'5', 'idx':'','cust_nick':'','clubname':cc_name}
    
    html_data = requests.post(json_url,data = data)
    
    data_soup = BeautifulSoup(html_data.text,"html.parser")

    ariji_list = data_soup.find("table", {"class":"type2"})

    ariji_data = ariji_list.find('tbody')#.text

    #print(ariji_data)
    for j in ariji_data:
        ariji_data1 = str(ariji_data)
        data1 = ariji_data1.strip().replace('리스트가 없습니다.','')
        data2 = data1.strip().replace('\r\n','')
        #data3 = "".join(data2.split())
        data3 = data2.strip().replace('\t','')
        data4 = data3.strip() + ''
        
        print(data4)

        # f = open('./golfpang_agent.text', 'a', encoding="UTF-8")
        # f.writelines(agent)
        # f.close

    # for j in ariji_data:
    #     ariji_data1 = ariji_data.replace('리스트가 없습니다.',' ')
    #     print(ariji_data1.text)
    # for j in ariji_list:
    #     ariji_agent = j['over'] + ' ' + j['price'] + ' ' + j['nick_name'] + ' ' + j['phone']
    #     print(ariji_agent)

    #pagination = data_soup.find()
    #print(html_data)    
    
    #cleanr = re.compile('<.*?>')
    #html_data = re.sub(cleanr, '', html_data)
    

    # html_data = html_data.replace('리스트가 없습니다.','')
    # html_data = html_data.replace('총','')
    # html_data = html_data.replace('개 타임이 검색되었습니다..','')
    # html_data = html_data.replace("지역",'')
    # html_data = html_data.replace("부킹일",'')
    # html_data = html_data.replace("티타임",'')
    # html_data = html_data.replace('포함','')
    # html_data = html_data.replace("골프장",'')
    # html_data = html_data.replace("홀수",'')
    # html_data = html_data.replace('그린피','')
    # html_data = html_data.replace('닉네임','')
    # html_data = html_data.replace('상황','')
    # html_data = html_data.replace('구분','')
    # html_data = html_data.replace('조회','')
    # html_data = html_data.replace('0 ','')
    

#    f.write(html_data)
    
#f.write('</body></html>')
#f.close