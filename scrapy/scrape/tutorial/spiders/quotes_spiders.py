import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [##'http://quotes.toscrape.com/',
                 ##'https://en.wikipedia.org/wiki/Machine_learning'
                 'http://up.gov.in/'
    ]
    def parse(self, response):
        yield {
                'link':response.url,
                'text1':response.css('p::text').extract(),
                'text': response.css('span.text::text').extract(),
                'author': response.css('small.author::text').extract_first(),
                'tags': response.css('div.tags a.tag::text').extract(),
                }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
