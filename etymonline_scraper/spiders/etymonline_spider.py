from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from etymonline_scraper.items import Etymology

class EtymonlineSpider(CrawlSpider):
    name = "etymonline.com"
    allowed_domains = ["etymonline.com",
                       "www.etymonline.com"
    ]
    start_urls = ["http://www.etymonline.com/index.php"]
    rules = [Rule(SgmlLinkExtractor(allow=()), "parse_entry", follow=True)]

    def parse_entry(self, response):
        hxs = HtmlXPathSelector(response)

        etymology = Etymology()
        etymology['entry_word'] = hxs.select("//dt/a[1]/text()").extract()
        etymology['entry_link'] = hxs.select("//dt//a[1]/@href").extract()
        etymology['description_word'] = hxs.select('//dd/a/text()').extract()
        etymology['description_link'] = hxs.select('//dd/a/@href').extract()

        return etymology
