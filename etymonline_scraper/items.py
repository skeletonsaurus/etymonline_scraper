# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Etymology(Item):
    # define the fields for your item here like:
    entry_word = Field()
    entry_link = Field()
    description_word = Field()
    description_link = Field()
