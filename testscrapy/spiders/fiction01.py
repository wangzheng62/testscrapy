import scrapy
import os,re
from testscrapy.items import FictionItem
from scrapy.loader import ItemLoader

def ma(s):
    pattern=r'[\d\w\u4e00-\u9fff]'
    #汉字
    r'[\u4e00-\u9fff]'

    P1=r"[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]"
    p=re.compile(pattern)
    l=p.findall(s)
    res = ''.join(l)
    return res

class Fiction(scrapy.Spider):
    name = 't1'
    def start_requests(self):
        urls=['http://www.xiaoqiang520.cc/3/3085/41136.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #print(response.xpath('//title').get())
        title=response.xpath('//h2/text()').get()
        title=ma(title)
        filename = 'd:/downloads/%s.txt' % title
        bs=response.xpath('//div[@name="content"]/p')
        l=bs.re(r'[\s\S]')
        s=''.join(l)
        next=response.xpath('//div[@id="thumb"]/a[4]/@href').get()
        with open(filename, 'wb') as f:
            f.write(s.encode(encoding='utf8'))
        self.log('Saved file %s' % filename)
        if next is not None:
            #next = response.urljoin(next)
            #yield scrapy.Request(url=next, callback=self.parse)
            yield response.follow(url=next,callback=self.parse)
class Fiction01(scrapy.Spider):
    name = 't2'
    def start_requests(self):
        urls=['http://www.xiaoqiang520.cc/3/3085/41136.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        l=ItemLoader(item=FictionItem(),response=response)
        l.add_xpath('title','//h2/text()')
        l.add_xpath('content','//div[@name="content"]/p')
        l.add_xpath('next','//div[@id="thumb"]/a[4]/@href')
        path='d:/downloads/'
        print(l.load_item()['content'])
        with open(path+l.load_item()['title']+'.txt','wb') as f:
            f.write(l.load_item()['content'])
        if l.load_item()['content'] is not None:
            #next = response.urljoin(next)
            #yield scrapy.Request(url=next, callback=self.parse)
            yield response.follow(url=l.load_item()['next'],callback=self.parse)