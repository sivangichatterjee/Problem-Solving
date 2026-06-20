class Codec:
    def __init__(self):
        self.url_map={}
        #self.counter=0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # self.counter+=1
        # self.url_map[self.counter]=longUrl
        # return "http://tinyurl.com/"+str(self.counter)
        char=string.ascii_letters+string.digits
        key="".join(random.choices(char,k=6))
        while key in self.url_map:
            key="".join(random.choices(char,k=6))
        self.url_map[key]=longUrl
        return "http://tinyurl.com/"+key

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # key=int(shortUrl.split("/")[-1])
        # return self.url_map[key]
        key=shortUrl.split("/")[-1]
        return self.url_map[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))