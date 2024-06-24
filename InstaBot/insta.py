from instabot import Bot
bot=Bot()

bot.login(username="",password="")
bot.follow("ashwinmali_")
bot.upload_photo("",caption="Hello this is my post..")
bot.unfollow("ashwinmali_")
bot.send_message("i love python",["ashwinmali_",""])

followers=bot.get_user_followers("")
for follower in followers:
    print(bot.get_user_info(follower))

following=bot.get_user_following("")
for Following in following:
    print(bot.get_user_info(Following))