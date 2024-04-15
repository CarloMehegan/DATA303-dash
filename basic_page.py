import plotly.express as px
import plotly.graph_objects as go

#Dash: the dash app class
#dcc: dash core components (slider bars, buttons, etc)
#html: dash html components
from dash import Dash, dcc, html

from datetime import datetime as dt
import numpy as np

print("Hello world!")

TITLE = "Hello World!"

if __name__ == '__main__':
    my_app = Dash(__name__)
    print(f"Started running at {str(dt.now())}")

    #the title will appear as the browser tab name
    my_app.title = TITLE

    #run the app in debug mode
    #dont have debug turned on when you send someone your code
    my_app.run(debug=True)
    