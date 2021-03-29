import scrapy
from ..items import AldiItem

class AldiSpider(scrapy.Spider):
    name = "aldi"
    start_urls = [
        "https://www.aldi.com.au/",
    ]

    def parse(self,response):
        for category in response.xpath("//li[2]/div[2]/ul/li"):
            yield scrapy.Request(url=category.xpath("./div/a/@href").extract_first(),callback=self.product_details)

    def product_details(self,response):
        items = AldiItem()
        all_products = response.xpath("//div[@class='tx-aldi-products']/div/a")

        for product in all_products:
            product_title=product.xpath("normalize-space(.//div[@class='box--description--header'])").extract()[0].replace("\xa0", " ").strip()
            packsize = product.xpath(".//span[@class='box--amount']/text()").extract()
            price = product.xpath(".//span[@class='box--value']/text()").extract()
            price_decimal = product.xpath(".//span[@class='box--decimal']/text()").extract()
            price_per_unit = product.xpath(".//span[@class='box--baseprice']/text()").extract()
            product_image = product.xpath(".//div/div/div/img/@src").extract()[0]

            # join the price and decimal price together
            if price != [] and price_decimal != []:
                price = price[0] + price_decimal[0]
            elif price != [] and price_decimal == []:
                price = price[0] + "c"
            
            #saving the data into items list
            items["product_title"] = product_title
            items["product_image"] = product_image
            items["packsize"] = packsize
            items["price"] = price
            items["price_per_unit"] = price_per_unit

            #return the data
            yield {
                "product_title": product_title,
                "product_image": product_image,
                "packsize":packsize,
                "price":price,
                "price_per_unit" : price_per_unit
            }

        #Subcategories pages
        for subcategory in response.xpath("//div[@class='csc-textpic-imagewrap']/div/div/a"):
            yield scrapy.Request(url=subcategory.xpath("./@href").extract_first(), callback=self.product_details)