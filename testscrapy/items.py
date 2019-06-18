# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#
from scrapy.loader.processors import Join,MapCompose
import re
def ma(s):
    pattern=r'[\d\w\u4e00-\u9fff]'
    #汉字
    r'[\u4e00-\u9fff]'

    P1=r"[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]"
    p=re.compile(pattern)
    l=p.findall(s)
    res = ''.join(l)
    return res
def en(s):
    return s.encode(encoding='utf8')
class Bytejoin():
    def __call__(self, values):
        return b''.join(values)
class FictionItem(scrapy.Item):
     title=scrapy.Field(input_processor=MapCompose(ma),output_processor=Join())
     content=scrapy.Field(input_processor=MapCompose(en),output_processor=Bytejoin())
     next=scrapy.Field(output_processor=Join())

class EyeItem(scrapy.Item):
    title=scrapy.Field()
    wish=scrapy.Field()
    sku=scrapy.Field()