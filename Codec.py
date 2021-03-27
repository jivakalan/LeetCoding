# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:54:18 2021

@author: kalan
"""

# =============================================================================
# 535. Encode and Decode TinyURL
# Medium
# 
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
# =============================================================================
import random

class Codec:
    def __init__(self):
        self.dic={}
        self.dic2={}
        self.dist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.shortUrl = ''
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        #if longUrl not in self.dic:
        shortUrl=''.join(random.choice(self.dist) for i in range(6))
        if shortUrl not in self.dic:
            self.dic[shortUrl]= longUrl
            self.dic2[longUrl]= shortUrl
            self.shortUrl = shortUrl
        return 'http://tinyurl.com/'+shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """        
        return self.dic[self.shortUrl]

longUrl='https://leetcode.com/problems/design-tinyurl'
url='https://leetcode.com/problems/design-tinyurl'


codec = Codec()
codec.decode(codec.encode(url))
