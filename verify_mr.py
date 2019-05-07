import csv
import bs4 as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

condit = 2


def navigate_page(main_url, page_url, nav_tag, nav_tag_class):
    url_s = str(page_url)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
    # r=requests.get(url_s)
    driver.get(url_s)
    page_src = driver.page_source
    s = BeautifulSoup(page_src, 'lxml')
    l = []
    # Added bellow 3 lines to work pages which doesn't have navigation
    if (nav_tag == 'NA' or nav_tag == 'na' or nav_tag_class == 'na' or nav_tag_class == 'na'):
        l.append(page_url)
        return list(l)
    for paragraph in s.find_all(str(nav_tag), class_=str(nav_tag_class)):
        # print(paragraph)
        for a in paragraph("a"):
            if "http" in a['href']:
                l.append(a['href'])
                break
            if "http" not in a['href'] and a['href']:
                l.append(main_url + a['href'])
                break
    driver.close()
    return l


def getproductlink(main_url, page_url, tag, tag_class, sub_tag, sub_tag_class, rt_tag, rt_class, rc_tag, rc_class):
    try:
        # data=requests.get(page_url)
        # print("Page Title is : %s" %driver.title)
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
        # r=requests.get(url_s)
        driver.get(page_url)
        page_src = driver.page_source
    except Exception as error:
        driver.close()
        print('error: %s' % error)
        print("Couldn't access url at indivisual_product_links.py")

    try:
        soup = BeautifulSoup(page_src, 'lxml')
        time.sleep(2)
        driver.close()
    except Exception as error:
        driver.close()
        print("Couldn't access page source at indivisual_product_links.py")
        print(error)
    try:
        tag_l = soup.find_all(str(tag), {"class": str(tag_class)})
        st = '\n\n'.join(str(s) for s in tag_l)
        lin = BeautifulSoup(str(st), 'html.parser')
        if tag_l:
            link = lin.find_all(str(sub_tag), {"class": str(sub_tag_class)})
    except:
        print("Tag/link not found. Probable tag/class-mismatch error.")
        driver.close()
    try:
        global condit
        l = []
        if link:
            for i in link:
                review = []
                revt = i.find_all(str(rt_tag), {"class": str(rt_class)})
                if revt:
                    if revt[0].find('p'):
                        review.append(revt[0].find('p').text.strip())
                        condit = condit - 1
                    else:
                        review.append(revt[0].text.strip())
                        condit = condit - 1
                revc = i.find_all(str(rc_tag), {"class": str(rc_class)})
                if revc:
                    if revc[0].find('p'):
                        review.append(revc[0].find('p').text.strip().rstrip('READ MORE'))
                        condit = condit - 1
                    else:
                        review.append(revc[0].text.strip().rstrip('READ MORE'))
                        condit = condit - 1
                break

    except Exception as error:
        print(error)
        print("Cound not find the Sub_tag/link")
        driver.close()
    # s=set(l)
    j = 0
    if l:
        for i in l:
            # print(str(j)+" : "+i)
            j += 1
    return l


def getproductlinks(main_url, page_url, tag, tag_class, sub_tag, sub_tag_class, rt_tag, rt_class, rc_tag, rc_class,
                    nav_tag, nav_tag_class, pg_lim):
    all_links = []
    prev_list = [main_url]
    latest_links = navigate_page(main_url, page_url, nav_tag, nav_tag_class)
    while "https://www.snapdeal.comjavascript:void(0)" in latest_links:
        latest_links.remove("https://www.snapdeal.comjavascript:void(0)")
    while "https://www.snapdeal.comjavascript:void(0);" in latest_links:
        latest_links.remove("https://www.snapdeal.comjavascript:void(0);")
    # print(latest_links)
    repeat_cond = []
    ct = 1
    pg_lim = 1
    while prev_list[-1] != latest_links[-1]:
        repeat_cond = prev_list
        prev_list = latest_links
        all_links.extend(latest_links)
        if ct == pg_lim:
            break
        latest_links = navigate_page(main_url, prev_list[-1], nav_tag, nav_tag_class)
        while "https://www.snapdeal.comjavascript:void(0)" in latest_links:
            latest_links.remove("https://www.snapdeal.comjavascript:void(0)")
        while "https://www.snapdeal.comjavascript:void(0);" in latest_links:
            latest_links.remove("https://www.snapdeal.comjavascript:void(0);")
        if latest_links == repeat_cond:
            break
        if prev_list == repeat_cond:
            break
        ct = ct + 1

        # print(latest_links)

    # print(len(all_links))
    all_links = list(set(all_links))
    print(all_links)

    product_links = []
    for link in all_links:
        product_links.extend(
            getproductlink(main_url, link, tag, tag_class, sub_tag, sub_tag_class, rt_tag, rt_class, rc_tag, rc_class))
        break
    return condit

'''
#Flipkart
main="https://www.flipkart.com"
url=str("https://www.flipkart.com/taparia-ws-05-diagonal-plier/product-reviews/itmf4fbr6npdzwvh?pid=PLIF4FBRE6KHJHXR")
tag=str("div")
tag_c=str("_1HmYoV _35HD7C col-9-12")
sub_tag_class=str("_1PBCrt")
sub_tag=str("div")
review_title_tag = "p"
review_title_class = "_2xg6Ul"
review_cont_tag = "div"
review_cont_class = "qwjRop"
nav_tag = "nav"
nav_class = "_1ypTlJ"
'''

'''
#Amazon
main="https://www.amazon.com"
#url=str("https://www.amazon.com/COOLIFE-Luggage-Expandable-Suitcase-Spinner/product-reviews/B07JJ346MH/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews")
url=str("https://www.amazon.com/COOLIFE-Luggage-Expandable-Suitcase-Spinner/product-reviews/B07JJ346MH/ref=cm_cr_getr_d_paging_btm_prev_32?ie=UTF8&pageNumber=32&reviewerType=all_reviews")
tag=str("div")
tag_c=str("a-section a-spacing-none reviews-content a-size-base")
sub_tag_class=str("a-section review aok-relative")
sub_tag=str("div")
review_title_tag = "a"
review_title_class = "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"
review_cont_tag = "span"
review_cont_class = "a-size-base review-text review-text-content"
nav_tag = "ul"
nav_class = "a-pagination"
'''


'''
#Snapdeal
main="https://www.snapdeal.com"
#url=str("https://www.snapdeal.com/product/nike-epic-react-flyknit-silver/684460913725/reviews?&sortBy=HELPFUL#defRevPDP")
url="https://www.snapdeal.com/product/nike-epic-react-flyknit-silver/684460913725/reviews?page=10&sortBy=HELPFUL#defRevPDP"
tag=str("div")
tag_c=str("reviewareain clearfix")
sub_tag_class=str("commentlist first jsUserAction")
sub_tag=str("div")
review_title_tag = "div"
review_title_class = "head"
review_cont_tag = "p"
review_cont_class = ""
nav_tag = "ul"
nav_class = "LTblack"
'''

'''
ans,flag = getproductlinks(main,url,tag,tag_c,sub_tag,sub_tag_class,review_title_tag,review_title_class,review_cont_tag,review_cont_class,nav_tag,nav_class,1)
k = 0    
#print(ans)

print(flag)
'''



