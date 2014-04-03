# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ItemImmobilier(Item):
	date=Field()
	id=Field()
	url=Field()
	name=Field()
	category=Field()
	description=Field()
	contrat=Field()
	nombre_de_piece=Field()
	superficie=Field()
	specification=Field()
	nombre_d_etage=Field()
	prix=Field()
	description=Field()
	images=Field()
class ItemInformatique(Item):
	id=Field()



