import re

#Question 2.1
product_count_text = "381 Products found"
product_count_int = int(re.search('[0-9]+',product_count_text).group())

#Question 2.2
generic_urls = [
    "https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img",
    "https://www.genericdomain.com/ab-c/31287bdwakj-jkl.img",
    "https://www.genericdomain.com/19unioawd02-jkl.img"
]

for url in generic_urls:
    special_sequence = re.findall(r"/\w+-",url)[-1].replace("/","").replace("-","")