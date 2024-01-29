import os
try:
  import requests
  from datetime import datetime
except:
  os.system('pip install requests')
t = 0
comm_num = 0
def search(q,type):
 global comm_num,t
 while True:
    try:
        response = requests.get(f"https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id={videoid}&count=9999999&cursor={t}",headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36','referer': f'https://www.tiktok.com/@whisper/video/{videoid}'}).json()
        for x in range(len(response["comments"])):
         comm_num += 1
         if type == 'user':
          if str(q) in str(response["comments"][x]['user']['unique_id']):
            print(f'''[+] Comment Number : {comm_num}
[+] Comment Text : {response["comments"][x]['text']}
[+] Comment Date : {datetime.fromtimestamp(int(response["comments"][x]['create_time']))}
[+] UserName : {response["comments"][x]['user']['unique_id']}
[+] NickName : {response["comments"][x]['user']['nickname']}''')
            print('='*50)
          else:
           pass
         elif type == 'text':
          if str(q) in str(response["comments"][x]['text']):
            print(f'''[+] Comment Number : {comm_num}
[+] Comment Text : {response["comments"][x]['text']}
[+] Comment Date : {datetime.fromtimestamp(int(response["comments"][x]['create_time']))}
[+] UserName : {response["comments"][x]['user']['unique_id']}
[+] NickName : {response["comments"][x]['user']['nickname']}''')
            print('='*50)
          else:
           pass
         elif type == 'all':
          if str(q) in str(response["comments"][x]):
            print(f'''[+] Comment Number : {comm_num}
[+] Comment Text : {response["comments"][x]['text']}
[+] Comment Date : {datetime.fromtimestamp(int(response["comments"][x]['create_time']))}
[+] UserName : {response["comments"][x]['user']['unique_id']}
[+] NickName : {response["comments"][x]['user']['nickname']}''')
            print('='*50)
          else:
           pass
         elif type == 'name':
          if str(q) in str(response["comments"][x]['user']['nickname']):
            print(f'''[+] Comment Number : {comm_num}
[+] Comment Text : {response["comments"][x]['text']}
[+] Comment Date : {datetime.fromtimestamp(int(response["comments"][x]['create_time']))}
[+] UserName : {response["comments"][x]['user']['unique_id']}
[+] NickName : {response["comments"][x]['user']['nickname']}''')
            print('='*50)
          else:
           pass
        t += 50
    except TypeError:
        print(f'[×] The End')
os.system("cls" if os.name == "nt" else "clear")
videoid = input('[?] TikTok Video Link : ')
if "vm.tiktok.com" in videoid or "vt.tiktok.com" in videoid:
    videoid = requests.head(videoid, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?",1)[0]
else:
    videoid = videoid.split("/")[5].split("?", 1)[0]
print('='*30)
mode=input(f'''[01] Search In UserNames
{'='*30}
[02] Search In Comments Text
{'='*30}
[03] Search In NickNames
{'='*30}
[04] Search In All
{'='*30}
[?¿] Search Mode : ''')
print('='*30)
if mode == '01' or mode == '1':
 q=input(f'[?] UserName : ')
 print('='*30)
 type='user'
 search(q,type)
elif mode == '02' or mode == '2':
 q=input(f'[?] KeyWord : ')
 print('='*30)
 type='text'
 search(q,type)
elif mode == '03' or mode == '3':
 q=input(f'[?] NickName : ')
 print('='*30)
 type='name'
 search(q,type)
elif mode == '04' or mode == '4':
 q=input(f'[?] Query : ')
 print('='*30)
 type='all'
 search(q,type)
else:
 print('Fuck You')