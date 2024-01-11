import dash
from dash import html, Input, Output, State
import dash_bootstrap_components as dbc
app = dash.Dash()
server = app.server
app.layout = html.Div([

    #Div1 Header Info
    html.Div([

        html.H1("My Python 3.x Portfolio", id="header_text")

        ],id="header_div"),


    #Div2 Card Holder
    html.Div([

    # CARD APP 1
        dbc.Card([
            dbc.CardImg(src=dash.get_asset_url("fig1.png"), top=True),
            
            dbc.CardBody([
                
                html.H4("Earthquake Stats Viewer", className="card-title"),
                html.P(["Displays Spatial, Magnitude and Depth",html.Br(),
                        "Distribution of Earthquakes",html.Br(),
                        "(Python, Tkinter, Matplotlib)"
                        ],className="card1-text"),
                
                dbc.Button("Play Preview", id="button_1"),

                dbc.Modal([

                    dbc.ModalBody([

                        html.Video(controls = True,
                                   autoPlay = False,
                                   height=550,
                                   width=550,
                                   src=dash.get_asset_url("eq_viewer.mp4")
                                   )
                        ]),
                    
                    dbc.ModalFooter(dbc.Button("Close",
                                               id="close-centered",
                                               className="ms-auto",
                                               n_clicks=0
                                               )
                                    )
                    ],id="modal-centered",
                          centered=True,
                          is_open=False,
                          size="xl",
                          style={"width": "760px", "height": "760px","background":"white","margin-left":"500px"},
                          ),

                ])

            ],id="card_1"),







    # CARD APP 2
        dbc.Card([

            dbc.CardImg(src=dash.get_asset_url("fig2.png"), top=True),

            dbc.CardBody([

                html.H4("PT Log Viewer", className="card-title"),
                
                html.P(["Displays Pressure and Temperature Graphs",html.Br(),
                        "and Lithology",html.Br(),
                        "(Python, Dash, Plotly)"
                       
                  
                        ],className="card2_text"),

                dbc.Button("Play Preview", id="button_2"),

                dbc.Modal([

                    dbc.ModalBody([

                        html.Video(controls = True,
                                   autoPlay = False,
                                   height=550,
                                   width=550,
                                   src=dash.get_asset_url("pt_log.mp4")
                                   )
                        ]),
                    
                    dbc.ModalFooter(dbc.Button("Close",
                                               id="close-centered2",
                                               className="ms-auto",
                                               n_clicks=0
                                               )
                                    )
                    ],id="modal-centered2",
                          centered=True,
                          is_open=False,
                          size="xl",
                          style={"width": "760px", "height": "760px","background":"white","margin-left":"500px"},
                          ),

                ])

            ],id="card_2"),

  # CARD APP 3
        dbc.Card([

            dbc.CardImg(src=dash.get_asset_url("fig3.png"), top=True),

            dbc.CardBody([

                html.H4("Earthquake Animations", className="card-title"),
                
                html.P(["Displays Earthquake Animations",html.Br(),
                        "Colored by Magnitude or Depth",html.Br(),
                        "(Python, Dash, Plotly)"
                       
                  
                        ],className="card3_text"),

                dbc.Button("Play Preview", id="button_3"),
                                dbc.Modal([

                dbc.ModalBody([

                        html.Video(controls = True,
                                   autoPlay = False,
                                   height=550,
                                   width=550,
                                   src=dash.get_asset_url("maras_quake.mp4")
                                   )
                        ]),
                    
                    dbc.ModalFooter(dbc.Button("Close",
                                               id="close-centered3",
                                               className="ms-auto",
                                               n_clicks=0
                                               )
                                    )
                    ],id="modal-centered3",
                          centered=True,
                          is_open=False,
                          size="xl",
                          style={"width": "760px", "height": "760px","background":"white","margin-left":"500px"},
                          ),

                ])

            ],id="card_3"),



  # CARD APP 4
        dbc.Card([

            dbc.CardImg(src=dash.get_asset_url("fig4.png"), top=True),

            dbc.CardBody([

                html.H4("Earthquake Animations (3D)", className="card-title"),
                
                html.P(["Displays Earthquake Animations",html.Br(),
                        "Colored by Magnitude or Depth",html.Br(),
                        "(Python, Matplotlib)"
                       
                  
                        ],className="card4_text"),

                dbc.Button("Play Preview", id="button_4"),

                dbc.Modal([

                    dbc.ModalBody([

                        html.Video(controls = True,
                                   autoPlay = False,
                                   height=550,
                                   width=550,
                                   src=dash.get_asset_url("anim_3d.mp4")
                                   )
                        ]),
                    
                    dbc.ModalFooter(dbc.Button("Close",
                                               id="close-centered4",
                                               className="ms-auto",
                                               n_clicks=0
                                               )
                                    )
                    ],id="modal-centered4",
                          centered=True,
                          is_open=False,
                          size="xl",
                          style={"width": "760px", "height": "760px","background":"white","margin-left":"500px"},
                          ),

                ])

            ],id="card_4"),








    ],id="card_holder_div")


 ])



@app.callback(
    Output("modal-centered", "is_open"),
    [Input("button_1", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-centered2", "is_open"),
    [Input("button_2", "n_clicks"), Input("close-centered2", "n_clicks")],
    [State("modal-centered2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-centered3", "is_open"),
    [Input("button_3", "n_clicks"), Input("close-centered3", "n_clicks")],
    [State("modal-centered3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open








@app.callback(
    Output("modal-centered4", "is_open"),
    [Input("button_4", "n_clicks"), Input("close-centered4", "n_clicks")],
    [State("modal-centered4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open






if __name__ == '__main__':
    app.run_server(debug=True,host='127.0.0.1',port=8050)
