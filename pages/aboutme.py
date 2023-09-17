from dash import register_page, html
import dash_mantine_components as dmc

register_page(__name__, name="aboutme")

about_me_text = ('In the digital age, the world revolves around software, and at the heart of software is the programmer. A programmer, often referred to as a developer or coder, is a craftsman of the digital age, skilled in translating human ideas into a language computers can understand. ')
layout = dmc.Grid([

        dmc.Grid([
            dmc.Col([
                dmc.Divider(label="Who am I?", size="sm")]),
        dmc.Col(
            dmc.Grid([
            dmc.Col(dmc.Text(about_me_text), span=8),
            dmc.Col(dmc.Image(src='/assets/profile_picture_pingu.svg'), sm=4)
        ]), sm=6, offsetSm=3, offset=1, span=10
    )])])