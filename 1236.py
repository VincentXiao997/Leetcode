# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostAddress = self.getHostAddress(startUrl)
        queue = collections.deque([startUrl])
        visited = set([startUrl])
        result = [startUrl]
        while queue:
            curUrl = queue.popleft()
            urls = htmlParser.getUrls(curUrl)
            for url in urls:
                if url not in visited:
                    visited.add(url)
                    if self.getHostAddress(url) == hostAddress:
                        result.append(url)
                        queue.append(url)
        return result
            
    def getHostAddress(self, url):
        thirdSlash = url.find('/', 7)
        if thirdSlash >= 0:
            return url[:thirdSlash]
        else:
            return url