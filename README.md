##  python 期末项目：[pythonanywhere链接](http://ljc.pythonanywhere.com/)
### html档描述
* 一共使用了三个HTML文档，base.html、entry.html、G.html
* base.html为基础文档，保证整个flask的框架可以在网页中显示，并且连接到css文件，保证css样式可以在webapp中成功显示
* G.html 为结果输出文档，包含输出的交互数据图表以及相关的文字分析，能够帮助更清楚的了解数据的含义
* entry.html为进入页面的设计文档，本次使用button按钮进行引导选择不同数据种类
  * entry中的action设置需要与app.py中的路径吻合，否则会出现无法进入数据显示页面
  * 可以单独设置class，设计进入跳转页面的样式
***
### Python文档描述
* app-1.py为主要使用文档，其中包括图片和相对的结论
* 其中含有少数循环（for）
* 输出为交互可视化图表，包括地图、条形图、点线图、对比图
* 读取文档需要绝对路径
* 不同是路径设置为不同的页面显示，使用方法为post，封装函数可以帮助数据有更好的输出显示
> *ipython notebook是无法正常运行的，需要我们输出html文件后，读取HTML文件显示*
* 交互式数据图表使用了bar、map、line进行数据绘制
***
### webapp动作描述
* 设置了button，点击button跳转至可视化数据
* 数据界面含有返回上一页按钮，可以帮助整个数据查看的返回操作
* 每一页的数据皆为交互式数据，用户可以点击相应部位进行不同的数据显示输出
### pythonanywehere部署
1. 需要构建一个虚拟环境，并在环境中```pip insatll '你需要的模块包'```所有用到的都要模块都需要pip install，否则将无法成功部署
2. 在读取文档时```df = pd.read_csv("xxxx.csv")```需要csv文件的绝对路径才能被正确识别
### 本地运行效果图
![运行效果图](https://github.com/Pjx759/final/blob/master/%E6%9C%AC%E5%9C%B0%E6%95%88%E6%9E%9C%E5%91%88%E7%8E%B0.png)
#### 项目细则文件
* 仓库路径：[彭靖茜_finall](https://github.com/Pjx759/final/tree/master/%E5%BD%AD%E9%9D%96%E8%8C%9C-finall)
