from flask import Flask, render_template, request
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Bar, Page, Pie, Timeline, Line
import csv
import pandas as pd
import plotly, pandas as cf
import plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po
po.init_notebook_mode()
cf.set_config_file(offline=True, theme="ggplot")

app = Flask(__name__, static_folder="templates")


# 首页

@app.route('/', methods=['GET'])
def entry():
    return render_template('entry.html')


# 国际旅游收入（地图）

# 数据准备
df = pd.read_csv("API_ST.INT.RCPT.XP.ZS_DS2_en_csv_v2_629965.csv")
国家 = df.CountryName


# 页面
@app.route('/国际旅游收入世界地图', methods=['POST'])
def G():
    return render_template('G.html',
                           story='678',
                           the_plot_all=timeline_map())


def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2009, 2018):
        map0 = (
            Map()
                .add(
                "国际旅游收入", list(zip(list(国家), list(df["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="2009-2017年世界各国国际旅游收入（占总出口的百分比）".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=10,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(series_index=0, max_=20),

            )
        )
        tl.add(map0, "{}".format(i))
    return tl.render_embed()


# 国际旅游收入（折线图）

# 数据准备
df = pd.read_csv("API_ST.INT.RCPT.XP.ZS_DS2_en_csv_v2_629965.csv")
# 只读取数据中‘world’（257）行的数据
data = df[-7:-6]
# 缺失值用0代替但下面无缺失值
# data1=data.fillna(0)
# data1
data2 = data[['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']]
# 整理每年的世界平均值
data3 = data2.iloc[-1]


# 页面
@app.route('/国际旅游收入折线图', methods=['POST'])
def 国际旅游收入():
    return render_template('G.html',
                           the_plot_all=Line_base())


def Line_base() -> Line:
    x = ["{}".format(i) for i in range(2009, 2018)]
    c = (
        Line()
            .add_xaxis(x)
            .add_yaxis("国家旅游收入（占总出口的百分比）", data3,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),

                       )
            .set_global_opts(title_opts=opts.TitleOpts(title="国家旅游收入（占总出口的百分比）", subtitle="2009年～2018年"))
    )
    return c.render_embed()


# 中国运输客运量

# 数据准备
df1 = pd.read_csv("passenger capacity.csv")
df1 = df1.fillna(0)
df1.index
df1.columns
df2 = df1.set_index('指标')
x轴 = [int(x) for x in df2.columns.values[:]]
旅客运输量 = list(df2.loc['旅客运输量'].values)[:]
铁路客运量 = list(df2.loc['旅客运输量'].values)[:]
公路客运量 = list(df2.loc['旅客运输量'].values)[:]
水运客运量 = list(df2.loc['旅客运输量'].values)[:]
航空客运量 = list(df2.loc['旅客运输量'].values)[:]


# 页面
@app.route('/中国运输客运量', methods=['POST'])
def 中国运输客运量():

    def bar_base() -> Bar:

        c = (
            Bar()
            .add_xaxis(x轴)
            .add_yaxis("旅客运输量", 旅客运输量)
            .add_yaxis("铁路客运量", 铁路客运量)
            .add_yaxis("公路客运量", 公路客运量)
            .add_yaxis("水运客运量", 水运客运量)
            .add_yaxis("航空客运量", 航空客运量)
            .set_global_opts(title_opts=opts.TitleOpts(title="中国运输客运量"))
        )
        return c.render_embed()
    return render_template('G.html',
                           the_plot_all=bar_base())

# 中国旅游业收入（折线图）

# 数据准备
中国旅游业收入 = pd.read_csv("tourism develop.csv")


# 页面
@app.route('/中国旅游业', methods=['POST'])
def CHINA_TOUR():
    fig = 中国旅游业收入.T.iplot(kind="scatter", xTitle="年份", yTitle="金额", title="中国旅游业收入", asFigure=True)
    py.offline.plot(fig, filename="中国旅游业.html", auto_open=False)
    with open("中国旅游业.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('G.html',
                           the_plot_all=plot_all)


# 国民总收入

# 数据准备
df = pd.read_csv("Household consumption level.csv")

# 页面


@app.route('/国民总收入', methods=['POST'])
def CHINA_GNI():
 fig = 中国旅游业收入.T.iplot(kind="scatter", xTitle="年份", yTitle="金额", title="中国旅游业收入", asFigure=True)
 py.offline.plot(fig, filename="国民总收入.html", auto_open=False)
 with open("国民总收入.html", encoding="utf8", mode="r") as f:
     plot_all = "".join(f.readlines())
 return render_template('G.html',the_plot_all=plot_all)


if __name__ == '__main__':
    app.run(debug=True)
