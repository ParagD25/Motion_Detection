from bokeh.models.annotations import Tooltip
from motion import my_data
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool,ColumnDataSource

my_data['Entry']=my_data["Enter Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
my_data['Exit']=my_data["Exit Time"].dt.strftime("%Y-%m-%d %H:%M:%S")

col_data=ColumnDataSource(my_data)

data_graph=figure(x_axis_type="datetime")

hover=HoverTool(tooltips=[("Enter Time","@Entry"),("Exit Time","@Exit")])
data_graph.add_tools(hover)

graph_fill=data_graph.quad(left="Enter Time",right="Exit Time",bottom=0,top=1,color='blue',source=col_data)

output_file("Motion_Graph.html")
show(data_graph)