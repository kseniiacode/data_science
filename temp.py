from spyre import server
import numpy as np
import pandas as pd

class MyApp(server.App) :
    title = 'MyApp'
    inputs = [
        {
           "type": 'slider',
           "label" : 'year',
           "key": 'chyear', 
           "value": 1982, "min": 1982, "max": 2019,
           "action_id": "refresh"
        },
        {
            "type": 'slider',
            "label": 'from',
            "key": 'wfrom',
            "value": 1, "min": 1, "max": 52,
            "action_id": "refresh"
        }, 
        {
            "type": 'slider',
            "label": 'to',
            "key": 'wto',
            "value": 1, "min": 1, "max": 52,
            "action_id": "refresh"
        }, 
        {
            "type": 'dropdown',
            "label": 'province',
            "options": [
                {"label": "Vinnytsa", "value": 1},
                {"label": "Volyn", "value": 2},
                {"label": "Dripropetrovsk", "value": 3},
                {"label": "Donetsk", "value": 4},
                {"label": "Zhytomyr", "value": 5},
                {"label": "Transcarpathia", "value": 6},
                {"label": "Zaporyzhzhya", "value": 7},
                {"label": "Ivano-Frankivsk", "value": 8},
                {"label": "Kiev", "value": 9},
                {"label": "Kirovohrad", "value": 10},
                {"label": "Luhansk", "value": 11},
                {"label": "Lviv", "value": 12},
                {"label": "Mykolayiv", "value": 13},
                {"label": "Odessa", "value": 14},
                {"label": "Poltava", "value": 15},
                {"label": "Rivne", "value": 16},
                {"label": "Sumy", "value": 17},
                {"label": "Ternopol", "value": 18},
                {"label": "Kharkiv", "value": 19},
                {"label": "Kherson", "value": 20},
                {"label": "Khmelnytskyi", "value": 21},
                {"label": "Cherkasy", "value": 22},
                {"label": "Chernivtsi", "value": 23},
                {"label": "Chernigiv", "value": 24},
                {"label": "Crimea", "value": 25},
            ],
            "key": 'province',
            "value": 1,
            "action_id": "refresh"
        }, 
    ]

    controls = [dict(type = "hidden", id = "refresh")]
    tabs = ["PlotVHI", "PlotVCI", "PlotTCI", "PlotAll", "Table"]


    outputs = [
        dict(type = "plot", id = "Plot1", control_id = "refresh", tab = "PlotVHI"),
        dict(type = "plot", id = "Plot2", control_id = "refresh", tab = "PlotVCI"),
        dict(type = "plot", id = "Plot3", control_id = "refresh", tab = "PlotTCI"),
        dict(type = "plot", id = "Plot4", control_id = "refresh", tab = "PlotAll"),
        dict(type = "table", id = "table1", control_id = "refresh", tab = "Table", on_page_load = True)
    ]

    def getData(self, params):
        df=pd.read_csv(r'C:\Users\k_zah\Documents\python\all_in_one_04302020-133947.csv')
        df.drop(df.columns[[0]], axis=1,inplace=True)
        prov = params['province']
        chyear = params['chyear']
        wfrom=params['wfrom']
        wto=params['wto']
        data = df[(df['provinceID'].astype('int') == int(prov))]
        data = data[(data['week'] >= wfrom) & (data['week'] <= wto)]
        
        return data

    def getPlot1(self, params):
        df = self.getData(params)
        plt_obj = df.plot(kind='bar',x='week',y='VHI', legend=False)
        fig = plt_obj.get_figure()
        return fig   
    
    def getPlot2(self, params):
        df = self.getData(params)
        plt_obj = df.plot(kind='bar',x='week',y='VCI', legend=False)
        fig = plt_obj.get_figure()
        return fig  
    
    def getPlot3(self, params):
        df = self.getData(params)
        plt_obj = df.plot(kind='bar',x='week',y='TCI', legend=False)
        fig = plt_obj.get_figure()
        return fig  
    
    def getPlot4(self, params):
        df = self.getData(params)
        df = df.drop(['year', 'provinceID', 'SMN', 'SMT'], axis=1)
        return df.plot.bar()  
    
    
app = MyApp()
app.launch(port=8801)