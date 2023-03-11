# send a toot to Mastodon with Mastodon.py
import os
# import Mastodon.py
import mastodon
from mastodon import Mastodon


# Consumer keys and access tokens, use for Mastodon.Client authentication which are stored in Codespaces secrets prefix with MASTODON_
mastodon = Mastodon(
    client_id=os.environ['MASTODON_CLIENT_KEY'],
    client_secret=os.environ['MASTODON_CLIENT_SECRET'],
    access_token=os.environ['MASTODON_ACCESS_TOKEN'],
    api_base_url="https://hachyderm.io",
)

# create variable called toot with the text that says "I wrote this toot with Copilot!"
toot = "test test"

# Send toot to Mastodon
mastodon.toot(toot)
