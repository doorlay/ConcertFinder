import requests

SPOTIFY_API_KEY = "BQBDFPH8h6gexAhfIXg2slqGshdgt2z5bomRuYdyA4alSGA74J8XYuaJ_RmTH36lQ-LHJxdGqccnyPEYq1WEbdeWFykgIg_w31gFzmUB9FBQ_YfKGc3cbTJ1gXquw1urICNZot-QHEJTwbOe0wk"
TICKETMASTER_API_KEY = "qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4"


def send_spotify_request(time_range, limit, api_key):
        url = f"https://api.spotify.com/v1/me/top/artists?time_range={time_range}&limit={limit}"
        headers = {
                "Accept": "application/json", 
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
                }
        return requests.get(url, headers=headers)


def extract_artists(api_response):
        return [entry["name"] for entry in api_response.json()["items"]]


def get_top_artists(time_range, limit, api_key):
        return extract_artists(send_spotify_request(time_range, limit, api_key))


print(get_top_artists("medium_term", 30, SPOTIFY_API_KEY))


def send_ticketmaster_request(api_key):
        url = f"https://app.ticketmaster.com/discovery/v2/events.json?attractionId=K8vZ917Gku7&apikey={api_key}"
        return requests.get(url)

print(send_ticketmaster_request(TICKETMASTER_API_KEY))

"""

The spotify api key expires every hour. Set up the whole workflow thing to get around this: https://developer.spotify.com/documentation/general/guides/authorization-guide/


The TicketMaster Discovery API lets your search for events by artist.

Gets all events for Adele in Canada

https://app.ticketmaster.com/discovery/v2/events.json?attractionId=K8vZ917Gku7&countryCode=CA&apikey=qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4


curl \
--include 'https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=qznGGwwSp4QK23CGqcXOOSB2DIHR2Zg4'


If top 30 doesn't include enough local shows, you can expand the search in either distance from zip or limit of artists returned (or maybe both)

"""