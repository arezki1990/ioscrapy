from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy1.items import ImmobilierItem
from scrapy.contrib.loader import ItemLoader

class MySpider(CrawlSpider):
    name = 'dlalaonline_Immobilier'
    allowed_domains = ['dlalaonline.com']
    start_urls = ['http://dlalaonline.com/categorie/immobilier/']

    rules = (
         # Rule (
              # SgmlLinkExtractor(
              #     allow=('/\d+', ),
              #     restrict_xpaths=('//div[@class="annonce"]/ul/li[@class="bouton_details"]')
              #     ),
              # follow= True,
              # callback='parse_item'
              # ), 
         Rule (
              SgmlLinkExtractor(
                 allow=('page/\d+/', ),
                 restrict_xpaths=('//div[@class="pages"]/a[@class="next page-numbers"]')
                 #  
                 ),
              callback='parse_item',
              follow= True
              ), 
         Rule (
              SgmlLinkExtractor(
                  allow=('', ),
                  restrict_xpaths=('//div[@class="post-left"]',)
                ),
                callback='parse_details',
              
          ),
          )
    def parse_item(self, response):
        print '***********************************************************************************'
        print response.url
        print '___________________________________________________________________________________'

    def parse_details(self,response):
        l = ItemLoader(item=ImmobilierItem(), response=response)
        l.add_value('url',response.url)
        l.add_value('source',self.allowed_domains)
        l.add_xpath('name', '//div[@class="shadowblock"]/h1[@class="single dotted"]/text()')
        l.add_xpath('prix', '//div[@class="shadowblock"]/div[@class="price-wrap"]/p[@class="post-price"]/text()')
        l.add_xpath('description', '//div[@class="shadowblock"]/div[@class="single-main"]/p/text()')
        l.add_xpath('id', '//div[@class="shadowblock"]/div[@class="single-main"]/h2[@class="description-area"]/text()',re='\d+')
        l.add_xpath('category', '//*[@id="cp_type_du_commerce"]/text()')
        l.add_xpath('wilaya', '//*[@id="cp_state"]/text()')
        l.add_xpath('date', '//*[@id="cp_listed"]/text()')
        l.add_xpath('nbr_piece', '//*[@id="cp_pices"]/text()')
        l.add_xpath('ville', '//*[@id="cp_city"]/text()')
        l.add_xpath('surface', '//*[@id="cp_surface_m"]/text()')
        l.add_xpath('image', '//div[@id="main-pic"]/a/img/@src')

        yield l.load_item()
        print response.url
