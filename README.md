# Member Compare Bot

This is a bot that compares the members of two different Discord servers and displays the members that are in one server but not in the other.

## Setup

1. Install python3.11 or later: [Download Python](https://www.python.org/downloads/)
2. Clone the repository: `git clone https://github.com/wolfhound905/member-compare-bot`
3. Navigate to the project directory: `cd member-compare-bot`
4. Install the required Python packages: `pip install -r requirements.txt` or `poetry install && poetry shell`
5. Create a new Discord bot: [Discord Developer Portal](https://discord.com/developers/applications)
6. Make a bot and give it the guild member intent
7. At the top of `main.py` put in your 2 guild ids
8. Run main.py (time varies on member count): `python3.11 main.py`
9. At the top of `compare.py` put the file names generated
10. You should get out your results!

### Example of the output

*common_members.csv*

```csv
member_id,tag
1069471801127751791,Robert#0583
1069470903353745418,Kyle#1657
1069489016300371998,Charlie#0175
1069470903353745418,Yogart#8431
```
*uncommon_members.csv*

```csv
guild_id,member_id,tag
672991877007409173,1069469699370393611,echo#5146
672991877007409173,1069469683356549172,operator#2793
672991877007409173,1069470008746455070,bingus#2004
672991877007409173,1069468400960680026,thelegend27#2733
```


