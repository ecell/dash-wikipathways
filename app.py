import dash
import dash_cytoscape as cyto
import dash_html_components as html
import wp2cyjs

app = dash.Dash(__name__)

wp3604=wp2cyjs.wp2cyjs("WP3604")

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '800px'},
        elements=wp3604['nodes'] + wp3604['edges']
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
