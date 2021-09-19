import requests

SPOTIFY_API_KEY = "BQBkwLNZxvcjNPcsMD6zhSRe2mfWLGm2DBiReEErF7D3vuOz5v02fDZRX6JA-viy51vCHU5Tj2o4anvW285w2g6uMMJEqc_emKmKhkjNCZlsxx7U-EZ2stXPdqI49w1M_0vChy-SPJY3NpDnieM"
TICKETMASTER_API_KEY = "qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4"


def get_top_artists(time_range, limit, api_key):
        url = f"https://api.spotify.com/v1/me/top/artists?time_range={time_range}&limit={limit}"
        headers = {
                "Accept": "application/json", 
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
                }
        response = requests.get(url, headers=headers)
        return [entry["name"] for entry in response.json()["items"]]


def find_events(artist, api_key):
        url = f"https://app.ticketmaster.com/discovery/v2/events.json?keyword={artist}&apikey={api_key}"
        return requests.get(url).json()


top_artists = get_top_artists("medium_term", 30, SPOTIFY_API_KEY)
for artist in top_artists:
        print(find_events(artist, TICKETMASTER_API_KEY))


"""

Login to your Spotify and enter your zip code and ConcertFinder will find concerts near you for all of your top artists.


The spotify api key expires every hour. Set up the whole workflow thing to get around this: https://developer.spotify.com/documentation/general/guides/authorization-guide/


The TicketMaster Discovery API lets your search for events by artist.

Join the TicketMaster affiliate program once I can get this going and this will be a great way to make money.

Gets all events for Adele in Canada

https://app.ticketmaster.com/discovery/v2/events.json?attractionId=K8vZ917Gku7&countryCode=CA&apikey=qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4


curl \
--include 'https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4'


If top 30 doesn't include enough local shows, you can expand the search in either distance from zip or limit of artists returned (or maybe both)

"""