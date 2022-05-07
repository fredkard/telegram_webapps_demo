import requests,json
#'http://t.me/CashbackExpress_bot'
bot = 'your bot token'
from definition import menu

class menu:
        def __init__(self,chat_id,bot):
            self.chat_id = chat_id
            self.bot = bot
             
            self.url = 'your url'
        def webapp(self,message_id):
            caption = 'Test'
            button = '[{"text":"Web App","web_app":{"url":"%s/oxcash.php"}}],'%self.url
            link = ('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML&reply_markup={"inline_keyboard":[%s'%(self.bot,self.chat_id,caption,button))
            link+= '[{"text":"⬅ Back","callback_data":"back_to_pay"}]]}'
            requests.get('https://api.telegram.org/bot%s/deleteMessage?chat_id=%s&message_id=%s'%(self.bot,self.chat_id,message_id))
            requests.get(link)

while (True):
    r = requests.get('https://api.telegram.org/bot%s/getUpdates'%bot).json()
    for x in r['result']:
        update_id = x['update_id']
        if 'message' in x:
            text = (x['message']['text'])
            chat_id =  (x['message']['chat']['id'])
            message_id = x['message']['message_id']
            print(message_id)
            main = menu(chat_id,bot)
            #send reply
            if '/test' in text:
            main.webapp(message_id)
        requests.get('https://api.telegram.org/bot%s/getUpdates?offset=%s'%(bot,update_id+1))
