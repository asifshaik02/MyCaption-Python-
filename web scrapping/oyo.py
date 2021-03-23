import requests
from bs4 import BeautifulSoup
import connect

pages = int(input("Enter no. of pages to be scrapped: "))

#creating table in database
connect.create()


def scrap(soup):
    hotel_list = soup.find_all("div",{"class":"hotelCardListing"})

    for hotel in hotel_list:
        hotel_dict={}
        hotel_dict["name"] = hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["price"] = int(hotel.find("span",{"class":"listingPrice__finalPrice"}).text[1:])
        hotel_dict["address"] = hotel.find("span",{"itemprop": "streetAddress"}).text
        hotel_dict["rating"] = hotel.find("span",{"class":"hotelRating__rating"}).text

        try:
            h_aminities = hotel.find("div",{"class":"amenityWrapper"})
            aminity_list = []
            for aminity in h_aminities.find_all("div",{"class":"amenityWrapper__amenity"}):
                aminity_list.append(aminity.find("span",{"class":"d-body-sm"}).text.strip())
        except:
            pass

        hotel_dict["aminity_list"] = ', '.join(aminity_list[:-1])
        #inserting into database
        connect.insert(tuple(hotel_dict.values()))

for i in range(1,pages+1):
    #url to be scraped
    url="https://www.oyorooms.com/hotels-in-hyderabad/?page="
    url=url+str(i)

    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

    req=requests.get(url,headers=headers)
    content=req.content

    soup = BeautifulSoup(content,"html.parser")
    scrap(soup)

print("Details of hotels:")
connect.print_details()