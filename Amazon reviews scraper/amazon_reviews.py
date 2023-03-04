import cloudscraper
from bs4 import BeautifulSoup
import requests as re
import pandas as pd

your_url=f'' #here you will insert your link of that products reviews page . You will insert here link of seond page of your reviews that contains page number in link. (not first page)
numer_of_pages=10 # you can change number of pages.

'''
your link should like this:

https://www.amazon.com/BENGOO-G9000-Controller-Cancelling-Headphones/product-reviews/B01H6GUCCQ/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&pageNumber=2&reviewerType=all_reviews

'''
dataList=[]
for page in range(1,numer_of_pages+1):
    url=your_url
    url=your_url.replace('Number=2',f'Number={page}')
    url=url.replace('btm_2',f'btm_{page}')
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



