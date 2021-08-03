from motion import my_data
from bokeh.plotting import figure,output_file,show

data_graph=figure(x_axis_type="datetime")

graph_fill=data_graph.quad(left=my_data["Enter Time"],right=my_data["Exit Time"],bottom=0,top=1,color='blue')

output_file("Motion_Graph.html")
show(data_graph)