# deleted-message-bot

A very simple bot to log deleted messages to a channel of your choice.

## Configuration and Launch

- Include your token and desired log channel in the following env variables. Ensure that your bot can send messages and embeds to this channel. It will not log deleted messages from channels it does not have read access to.
    - `TOKEN`
    - `LOG_CHANNEL`
### Running directly

- Run `pip install -r requirements.txt` to download the required modules.
- Run `python bot.py`. 

### Running and building via Docker

- Build with `docker build . -tag deleted-message-bot`.
- Run with `docker run deleted-message-bot`.


