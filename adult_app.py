# Imports
# -------

# Dash-Plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# App Layout
# ----------

# Set stylesheetgs
yeti = dbc.themes.YETI

# Initialize app
app = dash.Dash(__name__, external_stylesheets=[yeti])

# Input components
dropdown_sex = dbc.FormGroup([
	dbc.Label("Sex", html_for="dropdown_sex", style={"fontWeight": "bold"}),
	dbc.Col(
		dbc.Select(
		id="dropdown_sex",
		options=[
			{"label": "Male", "value": "Male"},
			{"label": "Female", "value": "Female"}
		]
	),
	width=6
	)
])

slider_age = dbc.FormGroup([
	dbc.Label("Age", html_for="slider_age", style={"fontWeight": "bold"}),
	dbc.Col(
		dcc.Slider(
			id="slider_age",
			min=17, max=90, step=1, value=53,
			marks={
				17: {"label": "17"},
				90: {"label": "90"}
			},
			tooltip={"always_visible": False, "placement": "bottom"}
		),
		width=12
	)
])

dropdown_workclass = dbc.FormGroup([
	dbc.Label("Workclass", html_for="dropdown_workclass", style={"fontWeight": "bold"}),
	dbc.Col(
		dbc.Select(
		id="dropdown_workclass",
		options=[
			{"label": "State-gov", "value": "State-gov"},
			{"label": "Self-emp-not-inc", "value": "Self-emp-not-inc"},
			{"label": "Private", "value": "Private"},
			{"label": "Federal-gov", "value": "Federal-gov"},
			{"label": "Local-gov", "value": "Local-gov"},
			{"label": "Self-emp-inc", "value": "Self-emp-inc"},
			{"label": "Without-pay", "value": "Without-pay"},
			{"label": "Never-worked", "value": "Never-worked"},
		]
	),
	width=6
	)
])

dropdown_education = 1

radio_marital_status = dbc.FormGroup([
	dbc.Label("Marital Status", html_for="radio_marital_status", style={"fontWeight": "bold"}),
	dbc.Col(
		dbc.RadioItems(
			id="radioitems-input",
			className="form-check",
			labelClassName="form-check-label",
			inputClassName="form-check-input",
			options=[
				{"label": "Never-married", "value": "Never-married"},
				{"label": "Married-civ-spouse", "value": "Married-civ-spouse"},
				{"label": "Divorced", "value": "Divorced"},
				{"label": "Married-spouse-absent", "value": "Married-spouse-absent"},
				{"label": "Separated", "value": "Separated"},
				{"label": "Married-AF-spouse", "value": "Married-AF-spouse"},
				{"label": "Widowed", "value": "Widowed"},
			]
	),
	)],
	className="form-group"
)

button_run = dbc.Button("Run", color="primary", style={"margin-bottom": "10px"})

display_probability = html.Div(
	[
		html.H3(
			"Probability",
			style={
				"fontWeight": "bold",
				"textDecoration": "underline"
			}
		),
		html.H1("87.38%")
	],
	style={"marginLeft": "10px"}
)

card_content = [
	dbc.CardHeader("Probability", style={"fontWeight": "bold"}),
	dbc.CardBody([
		html.H2("87.38%", className="card-title"),
		html.P(
			"Do I want to write a few things here...",
			className="card-text"
		)
	])
]

# App layout
form = dbc.Form([dropdown_sex, slider_age, dropdown_workclass, radio_marital_status, button_run])
app.layout = dbc.Container(
	[
		html.H1("Adult Income | Probability of Earning More Than $50K Per Year"),
		html.Hr(),
		dbc.Row(
			[
				dbc.Col(form, md=4),
				dbc.Col(dbc.Card(card_content, color="light", outline=True), md=4)
			],
		)
	],
	fluid=True
)

# Main block
if __name__ == '__main__':
	app.run_server(debug=True, host='127.0.0.1', port='8050')