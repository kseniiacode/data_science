from spyre import server
import pandas as pd

def getFrame():
    df=pd.read_csv(r'C:\Users\k_zah\Documents\GitHub\data_science\all_in_one_04302020-231120.csv')
    df.drop(df.columns[[0]], axis=1,inplace=True)
    return df

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
    tabs = ["PlotVHI", "PlotVCI", "PlotTCI", "PlotAll", "PlotMaxMin", "Table", 
        "Table2"]


    outputs = [
        dict(type = "plot", id = "Plot1", control_id = "refresh", tab = "PlotVHI"),
        dict(type = "plot", id = "Plot2", control_id = "refresh", tab = "PlotVHI"),
        dict(type = "plot", id = "Plot3", control_id = "refresh", tab = "PlotVHI"),
        dict(type = "plot", id = "Plot4", control_id = "refresh", tab = "PlotAll"),
        dict(type = "plot", id = "Plot5", control_id = "refresh", tab = "PlotMaxMin"),
        dict(type = "table", id = "table1", control_id = "refresh", tab = "Table", on_page_load = True),
        dict(type = "table", id = "table2", control_id = "refresh", tab = "Table2", on_page_load = True)
    ]

    def table1(self, params):
        prov = params['province']
        chyear = params['chyear']
        wfrom=params['wfrom']
        wto=params['wto']
        data = df[(df['provinceID'].astype('str') == str(prov)) & (df['year'] == chyear)]
        data = data[(data['week'] >= wfrom) & (data['week'] <= wto)]
        return data
    
    def table2(self, params):
        prov = params['province']
        chyear = params['chyear']
        wfrom=params['wfrom']
        wto=params['wto']
        data = df[(df['provinceID'].astype('str') == str(prov)) & (df['year'] == chyear)]
        data = data[(data['week'] >= wfrom) & (data['week'] <= wto)]
        print(data)
        datan = pd.DataFrame(data.groupby('week').VHI.agg(['max', 'min']).reset_index())
        print(datan)
        return datan
        

    def Plot1(self, params):
        df = self.table1(params)
        return df.plot(x='week',y='VHI')
    
    def Plot2(self, params):
        df = self.table1(params)
        return df.plot(x='week',y='VCI')
        
    def Plot3(self, params):
        df = self.table1(params)
        return df.plot(x='week',y='TCI')
    
    def Plot4(self, params):
        df = self.table1(params)
        df = df.drop(['year', 'provinceID', 'SMN', 'SMT'], axis=1)
        return df.plot(kind = 'bar', x = 'week', y = ['VHI', 'VCI', 'TCI'])  
    
    def Plot5(self, params):
        df = self.table2(params)
        return df.plot()
    
    
df = getFrame()    
app = MyApp()
app.launch(port=8801)