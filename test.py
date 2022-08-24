import commands as cmd
from telebot import types

import copy

mg = {
    'content_type': 'text', 
    'id': 524, 
    'message_id': 524, 
    'from_user': {
        'id': 74287802, 
        'is_bot': False, 
        'first_name': 'Dmitry', 
        'username': None, 
        'last_name': 'Glazkin', 
        'language_code': 'ru', 
        'can_join_groups': None, 
        'can_read_all_group_messages': None, 
        'supports_inline_queries': None, 
        'is_premium': None, 
        'added_to_attachment_menu': None}, 
    'date': 1659553647, 
    'chat': {
        'id': 74287802,
        'type': 'private', 
        'title': None, 
        'username': None, 
        'first_name': 'Dmitry', 
        'last_name': 'Glazkin', 
        'photo': None, 
        'bio': None, 
        'join_to_send_messages': None, 
        'join_by_request': None, 
        'has_private_forwards': None, 
        'description': None, 
        'invite_link': None, 
        'pinned_message': None, 
        'permissions': None, 
        'slow_mode_delay': None, 
        'message_auto_delete_time': None, 
        'has_protected_content': None, 
        'sticker_set_name': None, 
        'can_set_sticker_set': None, 
        'linked_chat_id': None, 
        'location': None}, 
    'sender_chat': None, 
    'forward_from': None, 
    'forward_from_chat': None, 
    'forward_from_message_id': None, 
    'forward_signature': None, 
    'forward_sender_name': None, 
    'forward_date': None, 
    'is_automatic_forward': None, 
    'reply_to_message': None, 
    'via_bot': None, 
    'edit_date': None, 
    'has_protected_content': None, 
    'media_group_id': None, 
    'author_signature': None, 
    'text': '/test2', 
    'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}], 
    'caption_entities': None, 
    'audio': None, 
    'document': None, 
    'photo': None, 
    'sticker': None, 
    'video': None, 
    'video_note': None, 
    'voice': None, 
    'caption': None, 
    'contact': None, 
    'location': None, 
    'venue': None, 
    'animation': None, 
    'dice': None, 
    'new_chat_member': None, 
    'new_chat_members': None, 
    'left_chat_member': None, 
    'new_chat_title': None, 
    'new_chat_photo': None, 
    'delete_chat_photo': None, 
    'group_chat_created': None, 
    'supergroup_chat_created': None, 
    'channel_chat_created': None, 
    'migrate_to_chat_id': None, 
    'migrate_from_chat_id': None, 
    'pinned_message': None, 
    'invoice': None, 
    'successful_payment': None, 
    'connected_website': None, 
    'reply_markup': None,
    'json': {
        'message_id': 524, 
        'from': {
            'id': 74287802, 
            'is_bot': False, 
            'first_name': 'Dmitry', 
            'last_name': 'Glazkin', 
            'language_code': 'ru'}, 
        'chat': {
            'id': 74287802, 
            'first_name': 'Dmitry', 
            'last_name': 'Glazkin', 
            'type': 'private'}, 
        'date': 1659553647, 
        'text': '/test2', 
        'entities':[{'offset': 0, 'length': 6, 'type': 'bot_command'}]
    }
}

players = dict()
messages = dict()

players['dima'] = r'"from":{"id":108929734,"first_name":"Dima","last_name":"Glazkin","username":"dima","is_bot":false},'    
players['leha'] = r'"from":{"id":108929735,"first_name":"Leha","last_name":"Ar","username":"leha","is_bot":false},'    
players['nadya'] = r'"from":{"id":108929736,"first_name":"Nadya","last_name":"Ar","username":"nadya","is_bot":false},'    
players['yulya'] = r'"from":{"id":108929737,"first_name":"Yulya","last_name":"Glazkina","username":"yulya","is_bot":false},'    

#step 1
for k in players:
    tmp = r'{"message_id":1,' + players[k] + r'"chat":{"id":1734,"first_name":"F","type":"private","last_name":"Wa","username":"oir"},"date":1435296025,"text":"HIHI"}'
    messages[k] = types.Message.de_json(tmp)
    cmd.start(messages[k])


messages['dima'].chat.type = 'group'
messages['dima'].chat.id = 1000

#step 2
cmd.start(messages['dima'])

messages['dima'].text = "/add_me @yulya"
messages['dima'].entities = []
messages['dima'].entities.append(types.MessageEntity.de_json(r'{"offset":8,"length":5,"type":"mention"}'))
print(messages['dima'].entities[0])
#step 3
#cmd.add_me_to_the_game(messages['dima'])

#messages['dima'].entities = [{'offset': 0, 'length': 6, 'type': 'bot_command'}]
#cmd.start(messages['dima'])