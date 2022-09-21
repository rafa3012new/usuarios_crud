from flask import Flask, render_template, redirect, request, session, flash
from datetime import datetime
from users import Userscrud


app = Flask(__name__)
app.secret_key = 'secretninja'

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    usuarios = Userscrud.get_all()

    for i in usuarios:
      print(str(i.id) + " " + i.first_name + " " + i.last_name + " " + i.email,flush=True)
    return render_template("index.html", usuarios_crud = usuarios)

@app.route('/mostrar/<int:id>')
def mostrar(id):
   usuario = Userscrud.get_by_id(id)
   return render_template("form_mostrar.html",usuario_crud = usuario)


@app.route("/limpiar")
def limpiar():
    session.clear()
    flash("se limpio la session","info")
    return redirect("/")


@app.route('/form_insert')
def insertar():
      return render_template("form_insertar.html")

@app.route('/form_update/<int:id>')
def actualizar(id):
      usuarior = Userscrud.get_by_id(id)
      return render_template("form_editar.html",usuario_crud = usuarior)

@app.route('/form_mostrar_eliminar')
def mostrar_eliminar():
      return render_template("form_mostrar_eliminar.html")


@app.route('/eliminar/<int:id>')
def eliminar(id):

  #se graba en el el objeto de la clase Userscr
  Userscrud.delete(id)

  return redirect('/limpiar')


@app.route('/grabari', methods=['POST'])
def grabari():

  datos =  {
    'first_name':request.form['nombre_usuario'],'last_name':request.form['apellido_usuario'],
    'email':request.form['email_usuario'],'created_at':datetime.today(),'updated_at':datetime.today()
  }

  print(datos,flush=True)

  #se graba en el el objeto de la clase Userscr
  Userscrud.save(datos)
  flash("se inserto el registro en la base de datos","info")

  return redirect("/limpiar")


@app.route('/grabare/<id>', methods=['POST'])
def grabare(id):

  datos =  {
    'first_name':request.form['nombre_usuario'],'last_name':request.form['apellido_usuario'],
    'email':request.form['email_usuario'],'created_at':datetime.today(),'updated_at':datetime.today(),
    'id':id
  }

  print(datos,flush=True)

  #se graba en el el objeto de la clase Userscr
  Userscrud.update(datos)
  flash("se modifico el registro en la base de datos","info")

  return redirect("/limpiar")


if __name__ == "__main__":
    app.run(debug=True)