class Codec:
    def __init__(self):
        self.code = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        """
        url = self.convert(longUrl)
        shortUrl = "http://tinyurl.com/" + url
        self.code[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        """
        return self.decode[shortUrl]
    
    def convert(self, url):
        res = ''
        for i in range(0, len(url), 10):
            temp = 0
            for c in url[i:10]:
                temp += ord(c)
            while temp > 122:
                temp -= 122
            res += chr(temp)
        return res

sol = Codec()
sol.encode('https://leetcode.com/problems/design-tinyurl')
# sol.decode(sol.convert('https://leetcode.com/problems/design-tinyurl'))
