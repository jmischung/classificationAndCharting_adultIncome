# Imports
# -------

# Dash-Plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# System
from joblib import load

# Modeling
from pandas import DataFrame
# from category_encoders.woe import WOEEncoder

# Components
# ----------

# Set stylesheetgs
yeti = dbc.themes.YETI

# Initialize app
app = dash.Dash(__name__, external_stylesheets=[yeti])

# Inputs

slider_age = dbc.FormGroup([
	dbc.Col(
		[
			dbc.Label("Age", html_for="slider_age", style={"fontWeight": "bold"}),
			dcc.Slider(
				id="slider_age",
				min=17, max=90, step=1, value=53,
				marks={
					17: {"label": "17"},
					90: {"label": "90"}
				},
				tooltip={"always_visible": False, "placement": "bottom"}
			)
		],
		width=12
	)
])

dropdown_education = dbc.FormGroup([
	dbc.Col(
		[
			dbc.Label("Education", html_for="dropdown_education", style={"fontWeight": "bold"}),
			dbc.Select(
			id="dropdown_education",
			options=[
				{"label": "Preschool", "value": " Preschool"},
				{"label": "1st-4th", "value": " 1st-4th"},
				{"label": "5th-6th", "value": " 5th-6th"},
				{"label": "7th-8th", "value": " 7th-8th"},
				{"label": "9th", "value": " 9th"},
				{"label": "10th", "value": " 10th"},
				{"label": "11th", "value": " 11th"},
				{"label": "12th", "value": " 12th"},
				{"label": "High School Graduate", "value": " HS-grad"},
				{"label": "Some College", "value": " Some-college"},
				{"label": "Professional School", "value": " Prof-school"},
				{"label": "Associate - Vocational", "value": " Assoc-voc"},
				{"label": "Associate - Academic", "value": " Assoc-acdm"},
				{"label": "Bachelors", "value": " Bachelors"},
				{"label": "Masters", "value": " Masters"},
				{"label": "Doctorate", "value": " Doctorate"},
			]
		)
	],
	width=8
	)
])

radio_marital_status = dbc.FormGroup([
	dbc.Col(
		[
			dbc.Label("Marital Status", html_for="radio_marital_status", style={"fontWeight": "bold"}),
			dbc.RadioItems(
				id="radioitems-input",
				className="form-check",
				labelClassName="form-check-label",
				inputClassName="form-check-input",
				options=[
					{"label": "Never married", "value": " Never-married"},
					{"label": "Married, civil-spouse", "value": " Married-civ-spouse"},
					{"label": "Married, spouse absent", "value": " Married-spouse-absent"},
					{"label": "Married, armed forces spouse", "value": " Married-AF-spouse"},
					{"label": "Separated", "value": " Separated"},
					{"label": "Divorced", "value": " Divorced"},
					{"label": "Widowed", "value": " Widowed"},
				]
			)
		]
	)],
	className="form-group"
)

dropdown_relationship_items = [
	dbc.DropdownMenuItem("Not-in-family", id=" Not-in-family"),
	dbc.DropdownMenuItem("Husband", id=" Husband"),
	dbc.DropdownMenuItem("Wife", id=" Wife"),
	dbc.DropdownMenuItem("Own-child", id=" Own-child"),
	dbc.DropdownMenuItem("Unmarried", id=" Unmarried"),
	dbc.DropdownMenuItem("Other-relative", id=" Other-relative")
]

dropdown_relationship = dbc.FormGroup(
	[
		dbc.Col(
			[
				dbc.InputGroup([
					dbc.DropdownMenu(
						dropdown_relationship_items,
						className="input-group-prepend",
						label="Relationship",
						addon_type="prepend"
					),
					dbc.Input(id="dropdown_relationship_input", className="form-control")
				]),
			],
			width=10
		),
	],
	className="form-group"
)

dropdown_occupation = dbc.FormGroup([
	dbc.Col(
		[
			dbc.Label("Occupation", html_for="dropdown_occupation", style={"fontWeight": "bold"}),
			dbc.Select(
				id="dropdown_occupation",
				options=[
					{"label": "Adm-clerical", "value": " Adm-clerical"},
					{"label": "Exec-managerial", "value": " Exec-managerial"},
					{"label": "Handlers-cleaners", "value": " Handlers-cleaners"},
					{"label": "Prof-specialty", "value": " Prof-specialty"},
					{"label": "Other-service", "value": " Other-service"},
					{"label": "Sales", "value": " Sales"},
					{"label": "Craft-repair", "value": " Craft-repair"},
					{"label": "Transport-moving", "value": " Transport-moving"},
					{"label": "Farming-fishing", "value": " Farming-fishing"},
					{"label": "Machine-op-inspct", "value": " Machine-op-inspct"},
					{"label": "Tech-support", "value": " Tech-support"},
					{"label": "Protective-serv", "value": " Protective-serv"},
					{"label": "Armed-Forces", "value": " Armed-Forces"},
					{"label": "Priv-house-serv", "value": " Priv-house-serv"},
				]
			)
		],
		width=8
	)
])

input_hours = dbc.FormGroup([
	dbc.Col(
		[
			dbc.Label("Hours Per Week", className="control-label", html_for="input_hours",
					  style={"fontWeight": "bold"}),
			dbc.InputGroup([
				dbc.Input(id="input_hours", className="form-control", type="number", min=1, max=99, step=1),
				dbc.InputGroupAddon("avg. hrs/wk", className="input-group-append", addon_type="append")
			]),
			dbc.FormText("Must be a whole number from 1-99")
		],
		width=8
	)
])

button_run = dbc.Col(
	dbc.Button("Run", id="button_run", color="primary", style={"margin-bottom": "10px"})
)

output_card = dbc.Card(
	[
		dbc.CardHeader("Probability", style={"fontWeight": "bold"}),
		dbc.CardBody([
			html.H1("0", id="output_probability", className="card-title"),
			html.P(
				[
					"The model generating the probabilities is the highest performing model given the presented features"
					" (82.3% accuracy). The overall highest performing model by accuracy, F1, and ROC-AUC scores (89.7%,"
					" 89.7%, and 96.7 respectively) can be viewed at the linked ",
					html.A(
						"GitHub repo.",
						href="https://github.com/jmischung/classificationAndCharting_adultIncome",
						target="_blank"
					)
				],
				className="card-text"
			)
		])
	],
	color="light",
	outline=True
)

alert = dbc.Alert(
			[
				html.H5("Oops!", className="alert-heading"),
				html.P("One or more of the inputs hasn't been completed or is invalid...", className="mb-0")
			],
			className="alert alert-dismissable alert-danger",
			color="danger",
			dismissable=True,
			is_open=True,
			duration=6000)


# Modeling
woe = load("./model_components/woe_transformer.sav")
clf = load("./model_components/gbm_model.sav")


def model(list_feats):
	# Create df
	cols = ['age', 'education', 'marital_status', 'occupation', 'relationship', 'hours_per_week']
	X = DataFrame(list_feats).transpose()
	X.columns = cols

	# Encode categorical
	X.iloc[:, 1:5] = woe.transform(X.iloc[:, 1:5])

	# Predict probability
	return clf.predict_proba(X)[0][1]


# Layout
form = dbc.Form([slider_age, dropdown_education, radio_marital_status, dropdown_relationship,
				 dropdown_occupation, input_hours, button_run])
app.layout = dbc.Container(
	[
		html.H1("Adult Income | Probability of Earning More Than $50K Per Year"),
		html.Hr(),
		dbc.Row(
			[
				dbc.Col(form, md=4),
				dbc.Col(output_card, id="output_card", md=4)
			],
		)
	],
	fluid=True
)

# Interactivity
@app.callback(
	Output("dropdown_relationship_input", "value"),
	[
		Input(" Not-in-family", "n_clicks"),
		Input(" Husband", "n_clicks"),
		Input(" Wife", "n_clicks"),
		Input(" Own-child", "n_clicks"),
		Input(" Unmarried", "n_clicks"),
		Input(" Other-relative", "n_clicks"),
	]
)
def dropdown_menu(r1, r2, r3, r4, r5, r6):
	context = dash.callback_context

	if not context.triggered:
		return ""
	else:
		menu_item = context.triggered[0]["prop_id"].split(".")[0]
		return menu_item


@app.callback(
	Output("output_probability", "children"),
	[Input("button_run", "n_clicks")],
	state=[
		State("slider_age", "value"),
		State("dropdown_education", "value"),
		State("radioitems-input", "value"),
		State("dropdown_occupation", "value"),
		State("dropdown_relationship_input", "value"),
		State("input_hours", "value")
	]
)
def run_model(n_clicks, age, education, marital, occupation, relationship, hours):
	inputs = [age, education, marital, occupation, relationship, hours]
	list_relationship = [" Not-in-family", " Husband", " Wife", " Own-child", " Unmarried", " Other-relative"]
	context = dash.callback_context

	if not context.triggered:
		return "0"
	elif (None in inputs) or ("" in inputs) or (relationship not in list_relationship):
		return alert
	else:
		prob = model(inputs) * 100
		return f"{round(prob, 1)}%"


# Main block
if __name__ == '__main__':
	app.run_server(debug=True, host='127.0.0.1', port='8050')