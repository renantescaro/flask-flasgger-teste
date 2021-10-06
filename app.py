from flask import Flask, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/pessoas')
@swag_from('validacao.yml')
def pessoas():
	pessoas = [
		{
			'id'  : 1,
			'nome':'Renan'
		},{
			'id'  : 2,
			'nome':'Ana'
		}
	]
	return jsonify(pessoas)


app.run(debug=True)