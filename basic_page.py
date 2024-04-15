import plotly.express as px
import plotly.graph_objects as go

#Dash: the dash app class
#dcc: dash core components (slider bars, buttons, etc)
#html: dash html components
from dash import Dash, dcc, html

from datetime import datetime as dt
import numpy as np


TITLE = "Hello World!"

def apply_main_layout(app: Dash) -> None:
    layout = html.Div(id = 'main-div',
                      children = [
                          html.H1("Welcome to my website!"),
                          html.Hr()
                      ]                  
    )
    app.layout = layout

    return

if __name__ == '__main__':
    my_app = Dash(__name__)
    print(f"Started running at {str(dt.now())}")

    #the title will appear as the browser tab name
    my_app.title = TITLE

    #apply the layout
    apply_main_layout(my_app)

    #run the app in debug mode
    #dont have debug turned on when you send someone your code
    my_app.run(debug=True)

