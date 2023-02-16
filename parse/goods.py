from parse.parse_utils import description_unpack, parse_descriptions, parse_links, parse_images

urls = ["https://master-kamnerez.ru/shar", "https://master-kamnerez.ru/shar/page/2",
        "https://master-kamnerez.ru/shar/page/3",
        "https://master-kamnerez.ru/yajco", "https://master-kamnerez.ru/yajco/page/2",
        "https://master-kamnerez.ru/shkatulka"]

links = parse_links(urls)
images = parse_images(urls)
descriptions = parse_descriptions(urls)
prices = description_unpack(descriptions)[0]
kinds = description_unpack(descriptions)[1]
sizes = description_unpack(descriptions)[2]
materials = description_unpack(descriptions)[3]
goods = []

for link, image, price, kind, size, material in zip(links, images, prices, kinds, sizes, materials):
    goods.append((link, image, kind, material, size, price))
