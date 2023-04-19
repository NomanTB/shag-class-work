from playwright.sync_api import sync_playwright
import requests, lxml,time
from bs4 import BeautifulSoup



def run(playwright):
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://www.booking.com/searchresults.uk.html?ss=%D0%9A%D0%B8%D1%97%D0%B2%2C+%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0&efdco=1&label=bookings-naam-B9ObXm1VJOAq2ho0czzpIQS267754536176%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1012849%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YTQUGSsRwx9_piJbnTYecvA&aid=376445&lang=uk&sb=1&src_elem=sb&src=index&dest_id=-1044367&dest_type=city&checkin=2023-05-03&checkout=2023-05-06&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
    time.sleep(3)

    soup = BeautifulSoup(page.content(),'lxml')

    for hotel in soup.select('.a4225678b2'):
        title = hotel.select_one('[data-testid="title"]').text
        link = hotel.select_one('a').get('href')
        print(title, link)

with sync_playwright() as playwright:
    run(playwright)





























# html = requests.get('https://www.booking.com/searchresults.uk.html?ss=%D0%9A%D0%B8%D1%97%D0%B2%2C+%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0&efdco=1&label=bookings-naam-B9ObXm1VJOAq2ho0czzpIQS267754536176%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1012849%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YTQUGSsRwx9_piJbnTYecvA&aid=376445&lang=uk&sb=1&src_elem=sb&src=index&dest_id=-1044367&dest_type=city&checkin=2023-05-03&checkout=2023-05-06&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
#
# # print(html.status_code)
# # print(html.text)
#
# soup = BeautifulSoup(html.text,'lxml')
#
#
# hotels = soup.select('[data-testid="title"]')
#
# for hotel in hotels:
#     print(hotel)
#
