import matplotlib.pyplot as plt
import pygal

class DrawChart():
    def __init__(self,db):
        self.db = db
    
    def draw(self):
        items = self.db.flowrate_select()
        x_values = list(range(0,24))
        y_values = []
        for x in x_values:
            y_values.append(0)
        for item in items:
            value = item[2][11:13].replace(':','')
            temp = int(value)
            y_values[temp] += item[1]

        chart = pygal.Bar()
        chart.title = "SmartStore24-hours flowrate" 
        chart.x_labels = x_values
        chart.add('Number of customer',y_values)
        chart.render_to_file('Flowrate_Chart.svg')