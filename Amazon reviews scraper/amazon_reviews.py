import cloudscraper
from bs4 import BeautifulSoup
import requests as re
import pandas as pd


dataList=[]
for page in range(1,501):

    url=f'https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/product-reviews/B07GBZ4Q68/ref=cm_cr_arp_d_paging_btm_{page}?ie=UTF8&pageNumber={page}&reviewerType=all_reviews'
    try:

        heading={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        cookies=dict(name='zubair',value='888')
        r= re.get(url,headers=heading,cookies=cookies)
        html=r.content

    except Exception as p:
        print(p)
        break
    
    soup=BeautifulSoup(html,'html.parser')

    allReviewsOfPage=soup.find('div',id='cm_cr-review_list')
    oneReviewList=allReviewsOfPage.find_all('div',class_='a-section review aok-relative')
    
    for i in oneReviewList:
        try:
            name=i.find('span',class_='a-profile-name').text
            reviewHeading=i.find('a',class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').text
            stars=i.find('span',class_='a-icon-alt').text[0]

            data={
                'Name':name,
                'stars':stars,
                'Review Heading':reviewHeading
            }

            dataList.append(data)
        except:
            pass



df= pd.DataFrame(dataList)

df.to_excel('Reviews.xlsx',index=False)



