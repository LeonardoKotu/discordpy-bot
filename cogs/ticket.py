import disnake
from disnake.ext import commands
from main import bot
# Наследуем модальное окно
class Menu(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.select(
        custom_id="select",
        placeholder="🔑 Выберите тип обращение",
        min_values=1,
        max_values=1,
        options = [
            disnake.SelectOption(

                label="Жалоба",
                description = "Жалоба на стафф/участник",
                emoji="🔒"
            ),

            disnake.SelectOption(
                label="Идея & Баги",
                description="Предложение для развитие сервера/нахождение багов",
                emoji="🔒"
            ),

            disnake
            .SelectOption(
                label="Снять выбор",
                emoji="❗"
            ),

        ]
        )


    # Обработка ответа, после отправки модального окна
    async def callback(self, select, inter):

        # если пользователь нажал на жалобу
        if select.values[0] == "Жалоба":

            cat = disnake.utils.get(inter.guild.categories, name="—  •  🔐 Тикеты") # категория
            global channel
            channel = await inter.guild.create_text_channel(f'🔖обращение-от-{inter.author}', category=cat) # создаем канал на этой категории

            '''отправляем эмбед'''
            embed_zaloba = disnake.Embed(
                title = "Обращение на тему `жалоба`",
                description=
                """
                > Опишите вашу проблему, *причину* и *ник* человека которые вы захотили **пожаловаться**.
                > За ложный тикет, вы будете **замьючены.**
                """,
                colour = 0x34582
            )

            # настройка
            
            embed_zaloba.set_footer(text="🌙 /close чтобы закрыть тикет.") # футер
            await channel.send(content=f"{inter.user.mention} / <@&1100946600886534177>", embed=embed_zaloba) # отправка сообщений, после нажатий меню
            
            await channel.set_permissions(inter.guild.default_role, read_messages=False) # это установит роле @everyone запрет на просмотр чата
            await channel.set_permissions(inter.user, read_messages=True, send_messages=True) # указываем права

            await inter.response.send_message(f"Для вас создана канал обращение - <#{channel.id}>, желаем удачи!", ephemeral=True) # сообщение о том что все успешно

            log_channel = inter.guild.get_channel(1100900722855387196)

            new_log = disnake.Embed(
            title = f"{inter.user}, создал тикет",
            description=
            f"""
            {inter.user.mention} создал тикет, на канале <#{channel.id}>
            Тип: {select.values[0]}
            """
        )
            await log_channel.send(embed=new_log)


        if select.values[0] == "Идея & Баги":

            cat = disnake.utils.get(inter.guild.categories, name="—  •  🔐 Тикеты") # категория
            channel = await inter.guild.create_text_channel(f'💡обращение-от-{inter.author}', category=cat) # создаем канал на этой категории

            '''отправляем эмбед'''
            embed_zaloba = disnake.Embed(
                title = "Обращение на тему `Идея & Баги`",
                description=
                """
                > Расскажите **идею** для развитие сервера, или **баг** в котором вы заметили на сервере.
                > За ложный тикет, вы будете **замьючены.**
                """,
                colour = 0x39e582
            )

            # настройка
            
            embed_zaloba.set_footer(text="🌙 /close чтобы закрыть тикет.") # футер
            await channel.send(content=f"{inter.user.mention} / <@&1100946600886534177>", embed=embed_zaloba) # отправка сообщений, после нажатий меню
            
            await channel.set_permissions(inter.guild.default_role, read_messages=False) # это установит роле @everyone запрет на просмотр чата
            await channel.set_permissions(inter.user, read_messages=True, send_messages=True) # указываем права

            await inter.response.send_message(f"Для вас создана канал обращение - <#{channel.id}>, желаем удачи!", ephemeral=True) # сообщение о том что все успешно

            log_channel = inter.guild.get_channel(1100900722855387196)

            new_log = disnake.Embed(
            title = f"{inter.user}, создал тикет",
            description=
            f"""
            {inter.user.mention} создал тикет, на канале <#{channel.id}>
            Тип: {select.values[0]}
            """
        )
            await log_channel.send(embed=new_log)


        if select.values[0] == "Снять выбор":

            await inter.response.send_message("Успешно.", ephemeral=True) # сообщение о том что все успешно



class Titckets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        bot.add_view(Menu())

    @commands.slash_command()    
    async def ticket(self, inter):
        
        embed = disnake.Embed(
            title = "Помоги нам стать лучше вместе с AMNESIA!",
            description=
            """
            > `-` Это канал поддержки. Выберите тип *обращение*, который вы хотите **обратиться**.

            """,
            colour = 0x2f3136

        )

        embed.set_footer(text="Просим не создавать обращении бессмысленно.")

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1101908582376689834/1101910941223899247/help-web-button.png")

        await inter.send(embed=embed, view=Menu())

    @commands.slash_command(description="Закрыть тикет")
    async def close(self, inter):
        await channel.delete()

def setup(bot):
    bot.add_cog(Titckets(bot))
