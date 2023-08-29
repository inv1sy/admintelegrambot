import telebot
import time
from telebot import TeleBot
from pyTelegramBotCAPTCHA import CaptchaManager

token='5416624245:AAHQjx8LNfIzhxGYlmBzBrI74ZD31u74Aps'
bot = telebot.TeleBot(token,skip_pending=True,)
GROUP_ID=-1001667705369
captcha_manager = CaptchaManager(bot.get_me().id)
@bot.message_handler(commands=['news'])
def start(message):
    time.sleep(10)
    bot.send_message(message.chat.id,'Дорогие участники группы "Парения".Все объявления,где есть жидкость в коробке и не видны следы эксплуатации на банке,будут баняться на 10 дней,а далее - на год.')
pass
@bot.message_handler(commands=['bl'])
def start(message):
    time.sleep(10)
    bot.send_message(message.chat.id,'\n 1️⃣Любой спам(одно объявление раз в час),\n 2️⃣Разжигание конфликта и переход на личность - сразу бан,(не мут,а бан),\n 3️⃣ Любой контент 18+  ,\n 4️⃣  Реклама своих услуг(в качестве барыги,шопа,канала,группы,чата и т.д), \n 5️⃣ Любой офтоп(объявление не тематики группы) Примеры:обмен на голду,обменяю аккаунт,обменяю наушники,телефон и т.д')
    paragraphs = print('\n\n')
pass
@bot.message_handler(commands=['ruls'])
def start(message):
    time.sleep(10)
    bot.send_message(message.chat.id, '⛔️ЗАПРЕЩЕНО: \n ❌cпам, \n ❌офтоп, \n ❌реклама, \n ❌контент 18+, \n ❌оскорбления.  \n Другие команды бота: \n /news - нововведение в правилах. \n /bl - возможные причины бана')
    pass
def handle_message(message):
    pass
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass
@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
  for new_user in message.new_chat_members:
    captcha_manager.restrict_chat_member(bot, message.chat.id, new_user.id)
    captcha_manager.send_new_captcha(bot, message.chat, new_user)
                                                                    
# Callback query handler
@bot.callback_query_handler(func=lambda callback:True)
def on_callback(callback):
  captcha_manager.update_captcha(bot, callback)
                                                                    
# Handler for correct solved CAPTCHAs
@captcha_manager.on_captcha_correct
def on_correct(captcha):
  bot.send_message(captcha.chat.id, "Вы прошли проверку.Прочтите наши правила перед общением - /ruls ")
  captcha_manager.unrestrict_chat_member(bot, captcha.chat.id, captcha.user.id)
  captcha_manager.delete_captcha(bot, captcha)

# Handler for wrong solved CAPTCHAs
@captcha_manager.on_captcha_not_correct
def on_not_correct(captcha):
  if (captcha.incorrect_digits == 1 and captcha.previous_tries < 2):
    captcha_manager.refresh_captcha(bot, captcha)
  else:
    bot.kick_chat_member(captcha.chat.id, captcha.user.id)
    bot.send_message(captcha.chat.id, f"{captcha.user.first_name} Не смог решить капчу и был забанен!")
    captcha_manager.delete_captcha(bot, captcha)
  
# Handler for timed out CAPTCHAS
@captcha_manager.on_captcha_timeout
def on_timeout(captcha):
  bot.kick_chat_member(captcha.chat.id, captcha.user.id)
  bot.send_message(captcha.chat.id, f"{captcha.user.first_name} Не решил капчу и был забанен!")
  captcha_manager.delete_captcha(bot, captcha)

if __name__ == "__main__":
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)
    #bot.infinity_polling()
    #bot.polling()
