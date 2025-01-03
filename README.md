# Envy Rebooter
Envy Rebooter is a open source reverse engineering project in Python to replicate Restarter v3, a popular Discord bot.
## How to self host Envy Rebooter
**You will need Python 3.8 or later to use Envy Rebooter. Download Python [here](https://www.python.org/).**

Once you have Python installed, you will need to install **discord.py**. You can do it by running the following:
```bash
pip install -U discord.py
```
Keep in mind that you will need superuser priveleges to run **pip** so put sudo/doas or whatever your favorite thing is to run **pip**.

Now run the following to clone the latest version of our repo:
```bash
git clone https://github.com/envyjs/rebooter.git && cd rebooter
```

Once that is done, open main.py in your favorite text editor and go to the bottom. You should see the following:

```python
bot.run('token')
```

Replace **token** inside **bot.run('token')** with your actual Discord bot token.

Now you should be able to start it. Start Envy Rebooter with the following command:

```bash
python3 main.py
```

and a message like this should show up:

```bash
Starting Envy Rebooter
```

Shall this message be shown and no errors occur, you are now self-hosting Envy Rebooter!
