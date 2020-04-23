
# ======link 1
import discord
from discord import Webhook, RequestsWebhookAdapter, File
from my_beautify import my_beautify as mb #self created module


class DiscordWebhook1:
    def __init__(self):
        #mb.fname_print("Constructor")
        self.webhook_id = "ID here"
        self.webhook_token = 'Token here'
        self.webhook_obj = None
        self.embed = None
        self.product_list = None

    def authenticate(self):
        #mb.fname_print("authenticate")
        # Create webhook object
        self.webhook_obj = Webhook.partial(id=self.webhook_id, token=self.webhook_token,
                                            adapter=RequestsWebhookAdapter())

    def set_embed(self):  # setting embed to be sent
        #mb.fname_print("set_embed")
        self.embed = discord.Embed(title="On Site: Jabong", description="Price is: {}".format('120$'), color=0x00ff00)
        self.embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832__340.jpg")

        self.product_list = {
                                'us40': "[[ATC]](https://google.com)",
                                'us41': "[[ATC]](https://google.com)",
                                'us42': "[[ATC]](https://google.com)",
                                'us43': "[[ATC]](https://google.com)",
                                'us44': "[[ATC]](https://google.com)",
                                'us45': "[[ATC]](https://google.com)",
                                'us46': "[[ATC]](https://google.com)",
                            }

        for key, value in self.product_list.items():
            self.embed.add_field(name=key, value=value, inline=False)
            # self.embed.add_field(name="us 40", value="[[ATC]](https://google.com)",inline=False)   # without loop

        self.embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832__340.jpg")
        self.embed.set_footer(text="End of the message...Have a nice day")
        self.embed.set_author(name="New Product Notification...!")

    def send(self):
        #mb.fname_print("send")
        self.webhook_obj.send(embed=self.embed)


if __name__ == "__main__":
    dw1 = DiscordWebhook1()
    dw1.authenticate()
    dw1.set_embed()
    dw1.send()
