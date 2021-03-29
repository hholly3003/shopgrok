# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AldiItem(scrapy.Item):
    # define the fields for your item here like:
    product_title = scrapy.Field()
    product_image = scrapy.Field()
    packsize = scrapy.Field()
    prize = scrapy.Field()
    prize_per_unit = scrapy.Field()
