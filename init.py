from flask import Flask, render_template, request
import os
import module_review as mr
import verify_mr as vmr

import csv

app = Flask(__name__,template_folder='./')
app.jinja_env.filters['zip'] = zip
app.secret_key = 'some_secret'

@app.route('/')
def home():
    return render_template('side_bar_page.html')

@app.route('/download')
def download():
    path = os.getcwd() + "/static/Display"
    list_of_files = []
    rel_path = "/static/Display/"
    for filename in os.listdir(path):
        list_of_files.append(filename)
    return render_template('Download.html',lof=list_of_files,rf=rel_path)

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
    file_name = (request.form['file_name']).strip()

    param_list=[main_url,url,tag,tag_class,sub_tag,sub_tag_class,review_title_tag,review_title_class,pd_tag,pd_class,nav_tag,nav_tag_class,page_limit]

    print(param_list)

    verify = vmr.getproductlinks(main_url,url,tag,tag_class,sub_tag,sub_tag_class,review_title_tag,review_title_class,pd_tag,pd_class,nav_tag,nav_tag_class,int(page_limit))
    if verify != 0:
        return render_template('error_page.html')
    ans = mr.getproductlinks(main_url,url,tag,tag_class,sub_tag,sub_tag_class,review_title_tag,review_title_class,pd_tag,pd_class,nav_tag,nav_tag_class,int(page_limit))
    # print(ans)

    with open('static/Display/'+file_name, 'w+') as csvFile:
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
    return render_template('create_recipe_page_1.html',fl_name=file_name)



if __name__ == "__main__":
     #app.run(host='0.0.0.0', port=8080, debug=True)
     app.run(debug=True)
