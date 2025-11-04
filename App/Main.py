from flask import Flask, render_template, request
from jinja2.filters import sync_do_sum

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')
@app.route('/ejercicio1')
def ejercicio1():
     return render_template('ejercicio1.html')

@app.route('/Calculo',methods=['POST'])
def Calculo():
    try:
        num1 = int(request.form['nota1'])
        num2 = int(request.form['nota2'])
        num3 = int(request.form['nota3'])
        Porcentaje_Asistencia = int(request.form['asistencia'])

        if not (10 <= num1 <= 70) or not (10 <= num2 <= 70) or not (10 <= num3 <= 70):
            resultado = 'No se pudo calcular promedio'
            resultado2 = 'Error: Las notas solo pueden ser entre 10 a 70'
            return render_template('ejercicio1.html', resultado=resultado,
                                   resultado2=resultado2)

        elif not (0 <= Porcentaje_Asistencia <= 100):
            resultado = 'No se pudo calcular promedio'
            resultado2 = 'Error: la asistencia solo pueden ser entre 0 a 100'
            return render_template('ejercicio1.html', resultado=resultado,
                                   resultado2=resultado2)


        Prom = (num1 + num2 + num3) / 3
        resultado = Prom
        if Porcentaje_Asistencia >=75 and Prom >= 40:
            Estado = 'APROBADO'
            resultado2 = Estado
        elif Porcentaje_Asistencia <75:
            Estado = 'REPROBADO POR ASISTENCIA'
            resultado2 = Estado
        else:
            Estado = 'REPROBADO'
            resultado2 = Estado    
        return render_template('ejercicio1.html',resultado=resultado,
                               resultado2=resultado2)
    except ValueError:
        resultado = 'No se pudo calcular promedio'
        resultado2 = ('Error: Debe ingresar un número entero valido, recuerde '
                      'no dejar numeros o la asistencia sin completar')
        return render_template('ejercicio1.html', resultado=resultado,
                               resultado2=resultado2)
    except Exception as e:
        resultado = 'No se pudo calcular promedio'
        resultado2 = f"El error es: {e}"
        return render_template('ejercicio1.html', resultado=resultado,
                               resultado2=resultado2)



@app.route('/ejercicio2')
def ejercicio2():
     return render_template('ejercicio2.html')

@app.route('/Conteo',methods=['POST'])
def Conteo():
    try:
        nom1 = (request.form['nombre1'])
        nom2 = (request.form['nombre2'])
        nom3 = (request.form['nombre3'])
        if(nom1 == '' or nom2 == '' or nom3 == ''):
            resultado = ('Error: Debe ingresar un nombre valido, recuerde '
                          'no dejar nombres sin completar')
            return render_template('ejercicio2.html', resultado=resultado)
        lista = [nom1, nom2, nom3]
        contador = 0
        caracterMax = 0
        Nombre = ''
        cantidadNombres = 0
        for i in range(0,3):
            contador = len(lista[i].strip())
            if contador > caracterMax:
                caracterMax = contador
                Nombre = lista[i].strip()
                cantidadNombres = 1
            elif contador == caracterMax:
                Nombre =Nombre+ " y "+lista[i].strip()
                cantidadNombres = 2

        if cantidadNombres == 1:
            resultado = f'El nombre con mayor cantidad de caracteres es: {Nombre}'
            resultado2 = f'El nombre tiene: {caracterMax} caracteres'
        else:
            resultado = f'Los nombres con mayor cantidad de caracteres son: {Nombre}'
            resultado2 = f'Los nombres tienen: {caracterMax} caracteres'
        return render_template('ejercicio2.html', resultado=resultado,
                               resultado2=resultado2)
    except Exception as e:
        resultado = ''
        resultado2 = f"Ocurrió un error: {e}"
        return render_template('ejercicio2.html', resultado=resultado,
                               resultado2=resultado2)

if __name__ == '__main__':
    app.run()
