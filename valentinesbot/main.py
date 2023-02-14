from discordclient import bot

from utils import EnvironmentVariables

env = EnvironmentVariables('DISCORD_BOT_TOKEN')


if __name__ == '__main__':
    bot.run(env.DISCORD_BOT_TOKEN)
