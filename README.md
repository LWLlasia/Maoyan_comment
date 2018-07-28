# Maoyan_comment

get_comment.py:

                get_movie_from_data()　# 从csv文件中获取电影名字进行搜索
                get_comment_page_url() # 从搜索页面中得到电影的ｉｄ
                get_comment()  # 用电影ｉｄ进入到电影评论的手机版,获取５０页的评论信息
                get_source()  #得到用户评分
                save_data_to_csv()  # 存储数据到csv文件
                
           
 get_MaoYan_dataFromCSV.py:
 
                get_Maoyan_from_csv()# 从csv文件中读取猫眼的数据


使用前记得更改读取数据的路径！！！

需要有phantomjs插件

从csv文件中获取电影名字






![image](https://github.com/LWLlasia/Maoyan_comment/blob/master/139944849.jpg)



猫眼手机版评论
    http://m.maoyan.com/movie/1212592/comments?_v_=yes
    
获取以下数据








![image](https://github.com/LWLlasia/Maoyan_comment/blob/master/image.png)








存成以下格式


![image](https://github.com/LWLlasia/Maoyan_comment/blob/master/295885059.jpg)

