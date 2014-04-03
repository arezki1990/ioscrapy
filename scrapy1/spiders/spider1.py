from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy1.items import ItemImmobilier

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
        item=ItemImmobilier()
        item["url"]=response.url
        item["name"]=sel.xpath('//div[@id="annonce"]/h1[@id="Title"]/text()').extract()
        item["category"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/p[re:test(@id, "Cat\w.*$")]/span/text()').extract()
        item["contrat"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/p[re:test(@id, "Dur\we minimale du contrat$")]/span/text()').extract()
        item["nombre_de_piece"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/p[re:test(@id, "Nombre de pi\wces$")]/span/text()').extract()
        item["superficie"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/p[re:test(@id, "Nombre de pi\wces$")]/span/text()').extract()
        item["nombre_d_etage"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/p[re:test(@id, "Nombre\.*tage$")]/span/text()').extract()
        item["prix"]=sel.xpath('//*[@id="Prix"]/span/text()').extract()
        item["specification"]=sel.xpath('//div[@id="annonce"]/div[@id="Description"]/psel[re:test(@id, "Sp\wcifications$")]/span/text()').extract()
        item["date"]=sel.xpath('//*[@id="menu"]/div/span[3]/text()').extract()
        item["description"]=sel.xpath('//*[@id="GetDescription"]/text()').extract()
        item["images"]=sel.xpath('//*[@id="gallery"]/a[1]/img/@src').extract()
        url_image=[]
        # for i in img:#Nombre\20 d
        # 	url_image.append(i.xpath('/@src').extract())
        
        yield item