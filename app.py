from dash import Dash, html, page_container, callback
from utils import navigacny_panel
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc

app = Dash(__name__, use_pages=True)
server = app.server

links = {
    'aboutme': {'label': 'About me'},
    'projects': {'label': 'Projects'},
    'contacts': {'label': 'Contacts'},
    'analysisadd': {'label': 'Add'}
}

app.layout = dmc.MantineProvider([
    html.Div(page_container, style={'margin-top': '40px'}),
    navigacny_panel(odkazy=links, logo='streamline:nature-ecology-flower-plant-tree-flower-petals-bloom')
    ], theme={'colorScheme': 'dark'}, withGlobalStyles=True, id="provider-theme")

@callback(
    Output("provider-theme", component_property="theme"),
    Input("tlacidlo-zmena-temy", component_property="n_clicks"),
    State("provider-theme", component_property="theme"),
    prevent_initial_call=True
)

def zmena_temy(n_clicks, theme):
    if theme['colorScheme'] == 'dark':
        return{'colorScheme': 'light'}
    else:
        return{'colorScheme': 'dark'}

if __name__ == '__main__':
    app.run_server(debug=False)
