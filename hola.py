from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/principal")
def principal():
	return render_template("template2PP.html",nombre="Citlally Herrera Méndez")
	

@app.route("/datos")
def datos():
	return render_template("datos.html",datos="Datos Personales")
	return redirect(redirect_template2PP())	

@app.route("/formacion")
def formacion():
	return render_template("formacion.html",formacion="Formación Académica")
	return redirect(redirect_template2PP())	

@app.route("/cursos")
def cursos():
	return render_template("cursos.html",cursos="Certificaciones")
	return redirect(redirect_template2PP())	

@app.route("/lenguajes")
def lenguajes():
	return render_template("lenguajes.html",lenguajes="Idiomas")
	return redirect(redirect_template2PP())	

@app.route("/interes")
def interes():
	return render_template("interes.html",interes="Datos de interés")
	return redirect(redirect_template2PP())	

@app.route("/pasatiempos")
def pasatiempos():
	return render_template("pasatiempos.html",hobbies="Pasatiempos")
	return redirect(redirect_template2PP())	

if __name__ == "__main__":
	app.run(debug=True)
