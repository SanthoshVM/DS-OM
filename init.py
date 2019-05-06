from flask import Flask, render_template, request

import module_review as mr

import csv
import json


app = Flask(__name__,template_folder='./')
app.jinja_env.filters['zip'] = zip
app.secret_key = 'some_secret'

@app.route('/')
def home():
    return render_template('side_bar_page.html')

@app.route('/test_recipe_page.html')
def test_recipe_page():
    return render_template('test_recipe_page.html',flag=1)

@app.route('/test_recipe',methods=['post'])
def test_recipe():
    #param_list=[]
    main_url=(request.form['page_main_url']).strip()
    url=(request.form['page_url']).strip()
    tag=(request.form['main_tag']).strip()
    tag_class=(request.form['main_class_name']).strip()
    sub_tag = (request.form['sub_tag']).strip()
    sub_tag_class = (request.form['sub_class_name']).strip()
    review_title_tag=(request.form['review_title_tag']).strip()
    review_title_class=(request.form['review_title_class']).strip()
    pd_tag=(request.form['pd_tag']).strip()
    pd_class=(request.form['pd_class']).strip()
    nav_tag=(request.form['nav_tag']).strip()
    nav_tag_class=(request.form['nav_tag_class']).strip()
    page_limit = (request.form['page_limit']).strip()

    param_list=[main_url,url,tag,tag_class,sub_tag,sub_tag_class,review_title_tag,review_title_class,pd_tag,pd_class,nav_tag,nav_tag_class,page_limit]

    print(param_list)

    ans = mr.getproductlinks(main_url,url,tag,tag_class,sub_tag,sub_tag_class,review_title_tag,review_title_class,pd_tag,pd_class,nav_tag,nav_tag_class,page_limit)
    # print(ans)

    with open('review.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        for i in ans:
            try:
                writer.writerow([i])
                print(k)
                k = k + 1
                print("Title + Cont = " + i)
                print(" ")
            except:
                print("Decode Error")
    csvFile.close()
    return render_template('create_recipe_page_1.html')



if __name__ == "__main__":
     #app.run(host='0.0.0.0', port=8080, debug=True)
     app.run(debug=True)
