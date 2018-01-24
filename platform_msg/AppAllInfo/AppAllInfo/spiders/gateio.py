# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from AppAllInfo.items import *
from AppAllInfo.settings import APP_NAME
import codecs  
class gate_pider(scrapy.Spider):
    name = "gate_spider"
    allowed_domains = ["gate.io"]
    urls = [
        #"http://www.wandoujia.com/tag/视频",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"

        "https://gate.io/articlelist/ann"
       # "https://www.feixiaohao.com/currencies/bitcoin/"
    ]
    #urls.extend([ "https://gate.io/articlelist/ann/%d" % x for x in range(2,3) ])
    start_urls = urls
#rules = [Rule(LinkExtractor(allow=['/apps/.+']), 'parse')]
    def parse(self, response):
    	page = Selector(response)
    	#for link in page.xpath("//a/@href"):
        #    href=link.extract()

        #    if href.startswith("/article"):
        #        print "++++++++++++++++++++++",href
        #    	yield Request("https://gate.io" +href, callback=self.parse_new_page)
        linklist = [link for link in  page.xpath("//a/@href") if link.extract().startswith("/article")]
        href=linklist[0].extract()

            #if href.startswith("/hc/zh-cn/articles"):
        print "++++++++++++++++++++++",href
        yield Request("https://gate.io" +href, callback=self.parse_new_page)






    def parse_new_page(self, response):
        #for sel in response.xpath('//ul/li'):
         #   title = sel.xpath('a/text()').extract()
          #  link = sel.xpath('a/@href').extract()
           # desc = sel.xpath('text()').extract()
            #print title, link, desc
        item = GateItem()
        sel = Selector(response)
        title =  sel.css('body > div.content > div.main_content > div > div.dtl-title > h2').extract() #sel.xpath('/html/body/div[3]/div[2]/div/div[1]/h2/font/text()').extract()
        #upDate =    sel.css('body > div.content > div.main_content > div > div.new-dtl-info > span').extract()#sel.xpath('/html/body/div[3]/div[2]/div/div[2]/node()')[1].extract()
        content = sel.css('body > div.content > div.main_content > div > div.dtl-content').extract()
        #url =

        print title

        item["url"] = response.url
        item['title'] = self.process_item(title)
        item['content'] = self.process_item(content)





        yield item
    def process_item(self,item):
    	return item and item[0].strip() or ""
    def process_name(self,item):
    	return item and item[1].strip() or ""
