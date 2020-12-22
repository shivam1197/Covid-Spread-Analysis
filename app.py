# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:56:20 2020

@author: Revo-Inc
"""

# import folium
# import pandas as pd
# from flask import Flask,render_template
# corona_df = pd.read_csv('dataset.csv')
# corona_df=corona_df.dropna()
# m=folium.Map(location=[34.223334,-82.461707],tiles='Stamen toner',zoom_start=8)
# by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
# cdf = by_country.nlargest(15,'Confirmed')[['Confirmed']]
# def circle_maker(x):
#     folium.Circle(location=(x[0],x[1]),radius=float(x[2])*10,color="red",popup='{}\n confirmed cases:{}'.format(x[3],x[2])).add_to(m)
#
# corona_df[['Lat','Long_','Confirmed','Combined_Key']].apply(lambda x:circle_maker(x),axis=1)
# html_map=m._repr_html_()
#
#
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return render_template("home.html",table=cdf, cmap=html_map)
# if __name__=="__main__":
#     app.run(debug=True)

# def find_top_confirmed(n = 15):
#     import pandas as pd
#     corona_df=pd.read_csv("dataset2.csv")
#     by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
#     cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
#     return cdf
#
# cdf=find_top_confirmed()
# pairs=[(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]
#
# import folium
# import pandas as pd
# corona_df = pd.read_csv("dataset2.csv")
# corona_df=corona_df[['Lat','Long_','Confirmed']]
# corona_df=corona_df.dropna()
# m=folium.Map(location=[34.223334,-82.461707],
#             tiles='Stamen toner',
#             zoom_start=8)
# def circle_maker(x):
#     folium.Circle(location=(x[0],x[1]),
#                  radius=float(x[2]),
#                  color="red",
#                  popup='confirmed cases:{}'.format(x[2])).add_to(m)
# corona_df.apply(lambda x:circle_maker(x),axis=1)
# html_map=m._repr_html_()
#
# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return render_template("home.html",table=cdf, cmap=html_map,pairs=pairs)
# if __name__=="__main__":
#     app.run(debug=True)
def find_top_confirmed(n = 15):
  import pandas as pd
  corona_df=pd.read_csv("dataset3.csv")
  by_country = corona_df.groupby('Province_State').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
  cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
  return cdf
cdf=find_top_confirmed()
pairs=[(province_state,confirmed) for province_state,confirmed in zip(cdf.index,cdf['Confirmed'])]
import folium
import pandas as pd
corona_df = pd.read_csv("dataset3.csv")
corona_df=corona_df[['Lat','Long_','Confirmed']]
corona_df=corona_df.dropna()
m=folium.Map(location=[34.223334,-82.461707],
            tiles='Stamen toner',
            zoom_start=8)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2]),
                 color="red",
                 popup='confirmed cases:{}'.format(x[2])).add_to(m)
corona_df.apply(lambda x:circle_maker(x),axis=1)
html_map=m._repr_html_()
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html",table=cdf, cmap=html_map,pairs=pairs)
if __name__=="__main__":
    app.run(debug=True)