import disnake
from disnake.ext import commands
from main import bot

class Button(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        custom_id="btn1",
        label='',
        emoji="<:console:1102333817789882378>"
    )


    async def callback_1(self, button, inter):
        if button.custom_id == 'btn1':
            member = inter.author
            role = inter.guild.get_role(1102006225736056882)
            await member.add_roles(role)
        await inter.response.send_message(f"Вы получили роль **Ивента.**", ephemeral=True)


    @disnake.ui.button(
        custom_id="btn2",
        label='',
        emoji="<:newspaper:1102333814933557268>"
    )


    async def callback_2(self, button, inter):
        if button.custom_id == 'btn2':
            member = inter.author
            role = inter.guild.get_role(1102006228722389133)
            await member.add_roles(role)
        await inter.response.send_message(f"Вы получили роль **Новости и обновление.**", ephemeral=True)



    @disnake.ui.button(
        custom_id="btn3",
        label='',
        emoji="<:suitcase:1102333812207259820>"
    )


    async def callback_3(self, button, inter):
        if button.custom_id == 'btn3':
            member = inter.author
            role = inter.guild.get_role(1102006227363450950)
            await member.add_roles(role)
        await inter.response.send_message(f"Вы получили роль **Набор.**", ephemeral=True)

    @disnake.ui.button (
        custom_id="btn4",
        label="",
        emoji="<:bellring:1102715523239772180>"
    )

    async def callback_4(self, button, inter):
        if button.custom_id == "btn4":
            member = inter.author
            role = inter.guild.get_role(1102009783306965034)
            await member.add_roles(role)
        await inter.response.send_message(f"Вы получили роль **Бамп.**", ephemeral=True)


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Button())


    @commands.slash_command()
    async def info(self, ctx):

        embed = disnake.Embed(
            title = "<a:green_sparkling_star:1101997680055558197> Выбор роли оповещений Amnesia",
            description=
            """
            ｡︎ »︎ <:console:1102333817789882378> - игры/ивенты
            ｡︎ »︎ <:newspaper:1102333814933557268> - новости и обновление 
            ｡︎ »︎ <:suitcase:1102333812207259820> - набор на стафф
            ｡︎ »︎ <:bellring:1102715523239772180> - [бампы](https://discord.com/channels/1100858771347095755/1101908856931623042)
            """,
            colour=0xe513f0
        )

        embed.set_image(url="https://i.pinimg.com/564x/ef/26/dd/ef26dde66380a72c8ac9b7571530820e.jpg")

        await ctx.send(view=Button(), embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
