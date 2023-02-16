# NOTE: Make sure your APP/BOT has the guild_members intent enabled in the developer portal

to_download = [285898487554375681, 642867988940324879]

bot_token = "TOKEN"

# Everything below this line can be ignored

import naff
import pandas as pd

intents = naff.Intents.new(
    guild_members=True,
    guilds=True,
)

bot = naff.Client(
    intents=intents,
    sync_interactions=True,
    basic_logging=True,
)


@naff.listen(naff.events.Startup, delay_until_ready=True)
async def download_members():
    print("Ready!")
    for guild_id in to_download:
        guild = bot.get_guild(guild_id)
        # save the members into a csv with the guild_id,member_id,tag
        print(f"Downloading {guild.name}...")
        # chunk all the members
        # it takes ten seconds for each 1000 members
        print(
            f"Chunking... {guild.member_count} members. ETA: {guild.member_count / 1000 * 10} seconds"
        )
        await guild.chunk()
        print("Done chunking!")
        print(f"Saving {guild.name}...")
        # use pandas to save the members
        df = pd.DataFrame(
            [
                {
                    "guild_id": guild_id,
                    "member_id": member.id,
                    "tag": member.tag,
                }
                for member in guild.members
            ]
        )
        df.to_csv(f"{guild_id}.csv", index=False)
        print("Done saving!")

        print(f"Done with {guild_id}")

    print("Done downloading all members!")
    print("Go to compare.py and put in the 2 file names.")
    await bot.stop()


bot.start(bot_token)
