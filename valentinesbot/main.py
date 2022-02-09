from discordclient import bot

from utils import EnvironmentVariables
from model import Presenter, Receiver, ValentineCard

env = EnvironmentVariables('DISCORD_BOT_TOKEN')


if __name__ == '__main__':
    print(tuple(Presenter.select().execute()))
    print(tuple(Receiver.select().execute()))
    print(tuple(ValentineCard.select().execute()))

    bot.run(env.DISCORD_BOT_TOKEN)
