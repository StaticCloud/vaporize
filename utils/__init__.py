import requests

class BannerHelper():
    def get_header_urls(self, game_ids):
        urls = []

        for id in game_ids:
            url = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{id}/header.jpg"

            request = requests.get(url)

            if request.status_code == 404:
                continue;

            urls.append(url)
        
        return urls

    def get_box_art_urls(self, game_ids):
        urls = []

        for id in game_ids:
            url = f"https://cdn.steamstatic.com/steam/apps/{id}/library_600x900.jpg"

            request = requests.get(url)

            if request.status_code == 404:
                continue;

            urls.append(url)
        
        return urls