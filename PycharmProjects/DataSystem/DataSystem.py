from flask import Flask,render_template,Response
import pandas as pd
import psycopg2
import pygal as py
import seaborn
import matplotlib


app = Flask(__name__)
# global connection
conn = psycopg2.connect(database="swansea_db",
                        user="postgres",
                        password="nissangtr",
                        host="localhost",
                        port="5432")
# lets create a template for this route
@app.route('/')
def hello_world():
    return render_template('home.html')
    # We return our template

@app.route("/login")
def login():
    return 'my login page here'


@app.route("/Analysis")
def about():
    return render_template('graph1.html')

# Routes can accept variables
@app.route("/mydata/<id>")
def mydata(id):
    return  str(id)

# display salaries
# display loans
# joins tables

@app.route("/contactus")
def contactus():
    return ("modcom developers")

@app.route("/salaries")
def salaries():
    return ("modcom developers")

@app.route("/graph1")
def graph1():
    dataframe = \
        pd.read_sql_query("SELECT Gender,count(Gender) FROM emp_details GROUP BY Gender",conn)
    print(dataframe)
    pie = py.Pie()
    pie.title = "Gender Distribution in %"
    pie.add(dataframe['Gender'].tolist()[0],
             dataframe['count'].tolist()[0])

    pie.add(dataframe['Gender'].tolist()[1],
             dataframe['count'].tolist()[1])
    return Response(response=pie.render(), content_type='image/svg+xml')






@app.route("/box")
def box():
    box_plot = py.Box()
    box_plot.title = 'V8 benchmark results'
    box_plot.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    box_plot.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    box_plot.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    box_plot.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    return Response(response=box_plot.render(), content_type='image/svg+xml')


@app.route("/graph2")
def graph2():
    hist = py.Histogram()
    hist.add('Wide bars', [(5, 0, 10), (4, 5, 13), (2, 0, 15)])
    hist.add('Narrow bars', [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)])
    return Response(response=hist.render(), content_type='image/svg+xml')


@app.route("/gauge")
def gauge():
    gauge_chart = py.Gauge(human_readable=True)
    gauge_chart.title = 'DeltaBlue V8 benchmark results'
    gauge_chart.range = [0, 10000]
    gauge_chart.add('Chrome', 8212)
    gauge_chart.add('Firefox', 8099)
    gauge_chart.add('Opera', 2933)
    gauge_chart.add('IE', 41)
    return Response(response=gauge_chart.render(), content_type='image/svg+xml')


@app.route("/graph3")
def graph3():
       dataframe = pd.read_sql_query("SELECT emp_details.IDno,emp_details.Fname,emp_details.DoB,emp_salary.Amount,emp_salary.pay_date FROM emp_details INNER JOIN emp_salary ON emp_details.IDno=emp_salary.IDno", conn)
       print(dataframe)
       line_chart = py.StackedLine(fill=True)
       line_chart.title = 'Browser usage evolution (in %)'
       line_chart.x_labels = dataframe['DoB'].tolist()
       line_chart.add('SALARY', dataframe ['Amount'].tolist())
       return Response(response=line_chart.render(), content_type='image/svg+xml')










@app.route("/pyramid")
def pyramid():
    ages = [(364381, 358443, 360172, 345848, 334895, 326914, 323053, 312576, 302015, 301277, 309874, 318295, 323396,
             332736, 330759, 335267, 345096, 352685, 368067, 381521, 380145, 378724, 388045, 382303, 373469, 365184,
             342869, 316928, 285137, 273553, 250861, 221358, 195884, 179321, 171010, 162594, 152221, 148843, 143013,
             135887, 125824, 121493, 115913, 113738, 105612, 99596, 91609, 83917, 75688, 69538, 62999, 58864, 54593,
             48818, 44739, 41096, 39169, 36321, 34284, 32330, 31437, 30661, 31332, 30334, 23600, 21999, 20187, 19075,
             16574, 15091, 14977, 14171, 13687, 13155, 12558, 11600, 10827, 10436, 9851, 9794, 8787, 7993, 6901, 6422,
             5506, 4839, 4144, 3433, 2936, 2615),
            (346205, 340570, 342668, 328475, 319010, 312898, 308153, 296752, 289639, 290466, 296190, 303871, 309886,
             317436, 315487, 316696, 325772, 331694, 345815, 354696, 354899, 351727, 354579, 341702, 336421, 321116,
             292261, 261874, 242407, 229488, 208939, 184147, 162662, 147361, 140424, 134336, 126929, 125404, 122764,
             116004, 105590, 100813, 95021, 90950, 85036, 79391, 72952, 66022, 59326, 52716, 46582, 42772, 38509, 34048,
             30887, 28053, 26152, 23931, 22039, 20677, 19869, 19026, 18757, 18308, 14458, 13685, 12942, 12323, 11033,
             10183, 10628, 10803, 10655, 10482, 10202, 10166, 9939, 10138, 10007, 10174, 9997, 9465, 9028, 8806, 8450,
             7941, 7253, 6698, 6267, 5773),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 91, 412, 1319, 2984, 5816, 10053, 16045, 24240, 35066,
             47828, 62384, 78916, 97822, 112738, 124414, 130658, 140789, 153951, 168560, 179996, 194471, 212006, 225209,
             228886, 239690, 245974, 253459, 255455, 260715, 259980, 256481, 252222, 249467, 240268, 238465, 238167,
             231361, 223832, 220459, 222512, 220099, 219301, 221322, 229783, 239336, 258360, 271151, 218063, 213461,
             207617, 196227, 174615, 160855, 165410, 163070, 157379, 149698, 140570, 131785, 119936, 113751, 106989,
             99294, 89097, 78413, 68174, 60592, 52189, 43375, 35469, 29648, 24575, 20863),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 392, 1351, 3906, 7847, 12857, 19913, 29108, 42475,
             58287, 74163, 90724, 108375, 125886, 141559, 148061, 152871, 159725, 171298, 183536, 196136, 210831,
             228757, 238731, 239616, 250036, 251759, 259593, 261832, 264864, 264702, 264070, 258117, 253678, 245440,
             241342, 239843, 232493, 226118, 221644, 223440, 219833, 219659, 221271, 227123, 232865, 250646, 261796,
             210136, 201824, 193109, 181831, 159280, 145235, 145929, 140266, 133082, 124350, 114441, 104655, 93223,
             85899, 78800, 72081, 62645, 53214, 44086, 38481, 32219, 26867, 21443, 16899, 13680, 11508),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 17, 15, 31, 34, 38, 35, 45, 299, 295, 218, 247, 252,
             254, 222, 307, 316, 385, 416, 463, 557, 670, 830, 889, 1025, 1149, 1356, 1488, 1835, 1929, 2130, 2362,
             2494, 2884, 3160, 3487, 3916, 4196, 4619, 5032, 5709, 6347, 7288, 8139, 9344, 11002, 12809, 11504, 11918,
             12927, 13642, 13298, 14015, 15751, 17445, 18591, 19682, 20969, 21629, 22549, 23619, 25288, 26293, 27038,
             27039, 27070, 27750, 27244, 25905, 24357, 22561, 21794, 20595),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 8, 21, 34, 49, 84, 97, 368, 401, 414, 557, 654,
             631, 689, 698, 858, 1031, 1120, 1263, 1614, 1882, 2137, 2516, 2923, 3132, 3741, 4259, 4930, 5320, 5948,
             6548, 7463, 8309, 9142, 10321, 11167, 12062, 13317, 15238, 16706, 18236, 20336, 23407, 27024, 32502, 37334,
             34454, 38080, 41811, 44490, 45247, 46830, 53616, 58798, 63224, 66841, 71086, 73654, 77334, 82062, 87314,
             92207, 94603, 94113, 92753, 93174, 91812, 87757, 84255, 79723, 77536, 74173),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 11, 35, 137, 331, 803, 1580, 2361, 3632, 4866,
             6849, 8754, 10422, 12316, 14152, 16911, 19788, 22822, 27329, 31547, 35711, 38932, 42956, 46466, 49983,
             52885, 55178, 56549, 57632, 57770, 57427, 56348, 55593, 55554, 53266, 51084, 49342, 48555, 47067, 45789,
             44988, 44624, 44238, 46267, 46203, 36964, 33866, 31701, 28770, 25174, 22702, 21934, 20638, 19051, 17073,
             15381, 13736, 11690, 10368, 9350, 8375, 7063, 6006, 5044, 4030, 3420, 2612, 2006, 1709, 1264, 1018),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 11, 20, 68, 179, 480, 1077, 2094, 3581, 5151, 7047,
             9590, 12434, 15039, 17257, 19098, 21324, 24453, 27813, 32316, 37281, 43597, 49647, 53559, 58888, 62375,
             67219, 70956, 73547, 74904, 75994, 76224, 74979, 72064, 70330, 68944, 66527, 63073, 60899, 60968, 58756,
             57647, 56301, 57246, 57068, 59027, 59187, 47549, 44425, 40976, 38077, 32904, 29431, 29491, 28020, 26086,
             24069, 21742, 19498, 17400, 15738, 14451, 13107, 11568, 10171, 8530, 7273, 6488, 5372, 4499, 3691, 3259,
             2657)]

    types = ['Males single', 'Females single',
             'Males married', 'Females married',
             'Males widowed', 'Females widowed',
             'Males divorced', 'Females divorced']

    pyramid_chart = py.Pyramid(human_readable=True, legend_at_bottom=True)
    pyramid_chart.title = 'England population by age in 2010 (source: ons.gov.uk)'
    pyramid_chart.x_labels = map(lambda x: str(x) if not x % 5 else '', range(90))
    for type, age in zip(types, ages):
        pyramid_chart.add(type, age)
        #return Response(response=pyramid_chart.render(), content_type='image/svg+xml')



@app.route("/details")
def details():


    dataframe = \
        pd.read_sql_query("SELECT * FROM  emp_details", conn)

    # come up with your own data
    # analyze
    # visualize the data,
    #  2 graphs
    # selecting specific columns
    # convert a specific column to list
    # print(dataframe['Fname'.tolist()])
    # print (dataframe['amount'].mean())
    # print(dataframe['amount'].describe())
    # print(dataframe.shape) rows/columns
    # print(dataframe.ndim)
    # print(dataframe['Fname'].head(20))

    # matplotlib, seaborn, bokeh, ggplot, pygal, plotly, gleam, geoplotlib

    # return render_template('details.html', data = dataframe)



    # df_fname = pd.read_sql_query('select fname from emp_details', conn)
    # print(df_fname)

    # df_datejoined = pd.read_sql_query("SELECT * FROM employees_det WHERE datejoined BETWEEN '1986-08-28' and '1995-01-27' LIMIT 2", conn)
    # print(df_datejoined)





if __name__ == '__main__':
    app.run(debug=True,port=8000)


