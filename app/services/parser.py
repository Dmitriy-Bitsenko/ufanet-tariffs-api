
import aiohttp
import asyncio
from bs4 import BeautifulSoup



URL = "https://www.ufanet.ru/#"

async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            html_text = await response.text()
            return html_text


def parse_tariffs_from_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    all_target_block_links = soup.find_all("ul", class_="list")
    target_ul_block = all_target_block_links[0]
    list_links = []
    list_items_in_block = target_ul_block.find_all('li')

    for item in list_items_in_block:
        anchor_tag = item.find('a')
        if anchor_tag:
            href_value = anchor_tag['href']
            list_links.append(f'https://www.ufanet.ru{href_value}')
    return list_links


async def parse_detailed_tariff_page(tariff_url):
    for link in tariff_url:
        html = await fetch_url(link)
        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all("div", class_="tariff")
        for card in cards:
            name = card.find("div", class_="text").text
            options = card.find_all("div", class_="option")
            for option in options:
                strong = option.find("strong")
                if strong and strong.text.strip() == "Интернет":
                    details = option.find_all("div", class_="detail")
                    price = int(details[1].text.split()[0])
                    print(name, price)


async def main():
    result_fetch_url = await fetch_url(URL)
    result_parse_tariffs_from_html = parse_tariffs_from_html(result_fetch_url)
    # print(result_parse_tariffs_from_html)
    list_of_links = parse_tariffs_from_html(result_fetch_url)
    await parse_detailed_tariff_page(list_of_links)





if __name__ == "__main__":

    asyncio.run(main())
