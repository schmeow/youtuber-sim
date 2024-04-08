import os
from typing import Final

from discord import Intents, Client, app_commands, Object, Interaction
from dotenv import load_dotenv

import csv
import pandas as pd

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(
    name="create_channel",
    description="My first application Command",
    guild=Object(id=1224912313023467531)
)
async def first_command(interaction: Interaction, channel_name: str):

    df = pd.read_csv('user_data.csv')
    ids = df.user_id

    if interaction.user.id in ids:
        return

    with open('user_data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([interaction.user.id, channel_name])


@client.event
async def on_ready() -> None:
    await tree.sync(guild=Object(id=1224912313023467531))
    print(f'{client.user} is now running!')


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
