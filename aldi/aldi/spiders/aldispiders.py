import scrapy
from ..items import AldiItem

class AldiSpider(scrapy.Spider):
    name = "aldi"
    start_urls = [
        "https://www.aldi.com.au/en/groceries/super-savers/",
        "https://www.aldi.com.au/en/groceries/fresh-produce/",
        "https://www.aldi.com.au/en/groceries/baby/",
        "https://www.aldi.com.au/en/groceries/beauty/",
        "https://www.aldi.com.au/en/groceries/freezer/",
        "https://www.aldi.com.au/en/groceries/health/",
        "https://www.aldi.com.au/en/groceries/laundry-household/",
        "https://www.aldi.com.au/en/groceries/liquor/",
        "https://www.aldi.com.au/en/groceries/pantry/"
    ]

    def parse(self,response):
        items = AldiItem()

        all_products = response.css("div.m-text-image")

        for product in all_products:
            product_title = product.css("div.box--description--header::text").extract()
            product_image = product.css('.m-no-ratio-on-phone img').css('::attr(src)').extract()
            packsize = product.css("span.box--amount::text").extract()
            price = product.css(".box--decimal , .ym-hideme+ .box--value").css('::text').extract()
            price_per_unit = product.css("span.box--baseprice::text").extract()

            items["product_title"] = product_title
            items["product_image"] = product_image
            items["packsize"] = packsize
            items["price"] = price
            items["price_per_unit"] = price_per_unit
        
            yield items