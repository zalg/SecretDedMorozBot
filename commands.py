import telebot
import os

import santa_logic as sl

DEBUG_TOKEN = "000"

TOKEN = DEBUG_TOKEN

if TOKEN == DEBUG_TOKEN:
    print('you are in test mode')
    bot = telebot.TeleBot(TOKEN, parse_mode=None)
else:
    bot = telebot.TeleBot(os.environ.get('TOKEN'))

global_players_list = dict()

global_games_list = dict()
restrictions = dict()



# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")



@bot.message_handler(commands=['start'])
def start(message):
        if message.chat.type == 'private':
            d = dict()
            user_id = message.from_user.id
            if user_id not in global_players_list.keys():
                d['first_name'] = message.from_user.first_name
                d['last_name'] = message.from_user.last_name            
                d['username'] = message.from_user.username
                d['chat_id'] = message.chat.id
                global_players_list[user_id] = d
            #DEBUG bot.reply_to(message, "You are ready for Secret Santa games!")
            print(f"global_players_list is {global_players_list}")
        if message.chat.type == 'group': 
            chat_id = message.chat.id
            if chat_id not in global_games_list.keys():
                global_games_list[chat_id] = []
                restrictions[chat_id] = []
                print(f"global_games_list is {global_games_list}")
                #DEBUG bot.reply_to(message, "Let's begin new game!")
            else:
                print("Ooops! Game has been already started")

@bot.message_handler(commands=['add_me'], chat_types=['group'])
def add_me_to_the_game(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id not in global_players_list:
        #DEBUG bot.reply_to(message,"Please send /start command in your private dialogue with SecretSantaPro bot")
        return
    if chat_id not in global_games_list.keys():
        #DEBUG bot.reply_to(message,"Please start the game first with /start command in this group")
        return
    if user_id not in global_games_list[chat_id]:
        global_games_list[chat_id].append(message.from_user.id)
        #DEBUG bot.reply_to(message,"Congretulations! You have been added to Secret Santa game in this chat ")
        
        for e in message.entities:
            if e.type == 'mention':
                username = message.text [e.offset+1:e.offset+e.length]
                for u in global_players_list:
                    if global_players_list[u]['username'] == username:
                        restrictions[chat_id].append((user_id,u))
            if e.type == 'text_mention':
                restrictions[chat_id].append((user_id,e.user.id))
        print(f"\nrestrictions are {restrictions}")

    else:
        bot.reply_to(message,"You are already in the list")
    print(global_games_list)

        

@bot.message_handler(commands=['list_users'], chat_types=['group'])
def list_users(message):
    chat_id = message.chat.id
    print("Games list")
    print(global_games_list)
    print("global_players_list")
    print(global_players_list)
    print("This game's players list")
    print(global_games_list[chat_id])
    for user in global_games_list[chat_id]:
        bot.send_message(global_players_list[user]['chat_id'], "Hi there!")
         
@bot.message_handler(commands=['make_it'])
def make_the_game(message):
    if message.chat.type == 'group': 
        chat_id = message.chat.id
        users_list = global_games_list[chat_id]
        rslt = sl.make_pairs(users_list,restrictions[chat_id])
        print("Result ")
        print(rslt)
        for (j,k) in rslt:
            bot.send_message(global_players_list[j]['chat_id'], f"Your friend is {global_players_list[k]['first_name']} {global_players_list[k]['username']} {global_players_list[k]['last_name']}")
            print(f"{j} is {k}")

@bot.message_handler(commands=['test1'], chat_types= ['group'])
def test1(message):
    chat_id = message.chat.id
    sender_id = message.from_user.id
    for e in message.entities:
        if e.type == 'mention':
            username = message.text [e.offset+1:e.offset+e.length]
            for u in global_players_list:
                if global_players_list[u]['username'] == username:
                    restrictions[chat_id].append((sender_id,u))
                    print(restrictions)

@bot.message_handler(commands=['test2'])
def test2(message):
    bot.reply_to(message,"hi")
    print(message.entities)


# ---------------- local testing ----------------
if __name__ == '__main__':
    bot.infinity_polling()

#TODO reset command
