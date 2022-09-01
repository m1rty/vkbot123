import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
 
session = vk_api.VkApi(token="vk1.a.DkSKf9WjQtAtwWeW1ahkwRwTuPcD00DfsFKAojTOrRtF76mvPP17Y9VDobygpL16JuMBzv4vCQ816UbiiC2Zb17i8GHlzy55xwx-DNaHxPhJvnBYl023fUijCeIp1c_Km8G-A46TT0QuAIEMwrMYvJnw5u2j0lPcSHJdntKk2xEiv1T3YV9UehBHYhKAxHD0")
 
lang = 0
def send_message(user_id, message, keyboard=None):
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    }
 
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
 
    session.method("messages.send", post)
 

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
 
        if text == "start":
            keyboard = VkKeyboard()
            keyboard.add_button("button", VkKeyboardColor.PRIMARY)
            send_message(user_id, "Запуск бота...")
            
            
        elif text == "blue":
            send_message(user_id, "BLUE")
        elif text == "/help":
            send_message(user_id, "В разработке!")
        else:
            send_message(user_id, "Неизвестная команда! Пропишите /help")
