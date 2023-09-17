# from utils import priprava_dat
# from dash import register_page, dcc, callback, Input, Output
# import dash_mantine_components as dmc
# from plotly.express import bar
#
# df = priprava_dat()
#
# layout = dmc.Stack([
#     dmc.Select([
#         {
#             'id': 'vyber-uzemi',
#             'value': 'Česká republika',
#             'label': 'Vyber-oblast:',
#             'data': [
#                 {'value': moznost, 'label': moznost}
#                 for moznost in df["uzemi_txt"].drop_duplicates().sort_values()
#             ]
#         }
#     ]),
#     dmc.Grid(id="G")
# ])
#
# @callback(
#     Output("G", component_property="figure"),
#     Input("vyber-uzemi", component_property="value")
# )
#
# def data_to_graph(uzemi):
#     w_df = df.copy()
#     w_df = w_df[df["uzemi_txt"] == uzemi]
#     w_df = w_df.groupby(by=["vzdelani_txt"])['hodnota'].sum().reset_index()
#     fig = bar(w_df, x="vzdelani_txt", y="hodnota")
#     return fig