from bs4 import BeautifulSoup
import requests


def parse_descriptions(pages: list) -> list:
    """
    The function collects all product descriptions from the page and adds them to a list.
    Return the list with descriptions.
    """
    descriptions = []
    for page in pages:
        page = requests.get(page).text
        soup = BeautifulSoup(page, "lxml")
        for description in soup.find_all("a", class_="woocommerce-LoopProduct-link woocommerce-loop-product__link"):
            descriptions.append(description.text.replace("\xa0р", "р").strip())
    return descriptions


def remove_sale_from_description(description: list) -> None:
    description.remove("Распродажа!")
    description.pop(-2)


def add_mm_to_size(description: list, kind: str) -> str:
    if kind.lower() != "шкатулка":
        description.pop()
        size = description.pop() + "мм"
    else:
        size = ""
    return size


def description_unpack(descriptions: list) -> tuple[list, list, list, list]:
    """
    The function takes a list with product descriptions and
    returns a tuple in which the descriptions are divided into parts.
    """
    prices = []
    kinds = []
    sizes = []
    materials = []
    for description in descriptions:
        description = description.split()
        if "Распродажа!" in description:
            remove_sale_from_description(description)
        if "мм" not in description and "шкатулка" not in description and "Шкатулка" not in description:
            description.append(description[-1])
            description[3] = "мм"
        price = description.pop()
        kind = description.pop(0)
        size = add_mm_to_size(description, kind)
        material = " ".join(description)
        prices.append(price)
        kinds.append(kind)
        sizes.append(size)
        materials.append(material)
    return prices, kinds, sizes, materials


def parse_links(pages: list) -> list:
    """
    The function collects all product descriptions from the page and adds them to a list.
    Return the list with links.
    """
    links = []
    for page in pages:
        page = requests.get(page).text
        soup = BeautifulSoup(page, "lxml")
        for link in soup.find_all('a'):
            link = link.get('href')
            if "mm" in link \
                    or link.endswith(("37206", "72")) \
                    or ("shkatulka-" in link and not "товарный" in link):
                links.append(link)
    return links


def parse_images(pages: list) -> list:
    """
    The function collects all product descriptions from the page and adds them to a list.
    Return the list with images.
    """
    images = []
    for page in pages:
        page = requests.get(page).text
        soup = BeautifulSoup(page, "lxml")
        for image in soup.find_all('img'):
            if image.get("data-lazy-srcset"):
                images.append(image.get("data-lazy-srcset").split(",")[-1].strip(" 900w"))
    return images
