# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

class ImmobilierItem(Item):
	id=Field()
	name=Field()
	prix=Field()
	category=Field()
	wilaya=Field()
	nbr_piece=Field()
	nbr_etage=Field()
	description=Field()
	surface=Field()
	url=Field()
	date=Field()
	ville=Field()
	source=Field()
	image=Field()



