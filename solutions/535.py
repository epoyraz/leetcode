import random
import string

class Codec:

    def __init__(self):
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        while True:
            short_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            short_url = self.base_url + short_key
            if short_url not in self.url_map:
                self.url_map[short_url] = longUrl
                return short_url

    def decode(self, shortUrl):
        return self.url_map.get(shortUrl, "")
