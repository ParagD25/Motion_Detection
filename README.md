# Motion Detection 📹
Detecting person's motion using webcam 📷 and storing information ℹ️ like timeframe during which one enters and exits the frame (Camera Frame).<br>
Timeframe Information is Stored in :
- `Timings.csv` : Excel Sheet
- `Motion_Graph.html` : Graphical Representation
  <p align="center">
    <img src="https://github.com/ParagD25/Motion_Detection/blob/master/Images/motion_graph.png" alt="Graph" width="45%">
  </p>

## Libraries Used 📋:

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

<li><b><i>cv2</i></b> - To Read Data from .xml file and capture motion.</li>
<li><b><i>Bokeh</i></b> - To create graph.</li>
<li><b><i>pandas</i></b> - To convert data into .csv file.</li><br>

## How To Use 🖥️:


- Clone this repository<br>
`git clone https://github.com/ParagD25/Motion_Detection`

- Go into the repository<br>
`cd Motion_Detection`

- Remove current origin repository<br>
`git remote remove origin`
- Create new virtual python environment<br>
`python3 -m venv venv`
- Activate virtual python environment<br>
`source venv/bin/activate`
- Install all the libraries mentioned above
- Run Python file<br>
`python motion.py` - For motion detection <br>
`python motion_graph.py` - For motion detection + Having Graph as an output.


## Contributing ©️:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
