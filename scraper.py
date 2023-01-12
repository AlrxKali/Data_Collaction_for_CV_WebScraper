import bs4
import requests
import shutil
import os
import argparse

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


def extract(searchterm, quantity):
    
    if not os.path.exists(searchterm):
        os.mkdir(searchterm)
    
    URL_input = GOOGLE_IMAGE + 'q=' + searchterm
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")
    ImgTags = soup.find_all('img')
    i = 0
    print('Please wait..')
    while i < quantity:

        for link in ImgTags:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                filename = str(i) + ext
                with open(os.path.join(searchterm, filename), 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
            except:
                pass
    print('\t\t\t Downloaded Successfully..\t\t ')
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--size", type=int, help="Setting how many pictures you want to get", default=1000) # This number is the amount images that will be downloaded; change the value if you need more or fewer pictures.
    
    args = parser.parse_args()
    
    list_test = [] # Enter the words or objects that you want to search for and download images e.i ["banana", "apple fruit"].

    for item in list_test:
        extract(item, args.size)
         

    
