from dash import register_page
import dash_mantine_components as dmc

register_page(__name__, name="aboutme")

layout = dmc.Text("About me.")