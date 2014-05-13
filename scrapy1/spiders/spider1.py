from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy1.items import ImmobilierItem

class MySpider(CrawlSpider):
    name = 'immobilier'
    allowed_domains = ['ouedkniss.com']
    start_urls = ['http://www.ouedkniss.com/fr/annonces/categorie.php?c=immobilier']

    rules = (
         Rule (SgmlLinkExtractor(allow=('', ),restrict_xpaths=('//li[@class="bouton_details"]','//div[@id="divPages"]'))
         , callback='parse_item', follow= True),
)

    def parse_item(self, response):
    	sel=Selector(response)
        item=ImmobilierItem()
        item["url"]=response.url

        # for i in img:#Nombre\20 d
        # 	url_image.append(i.xpath('/@src').extract())
        
        yield item
