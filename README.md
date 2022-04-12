# MeLi Challenge isMutant
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar
contra los X-Men.


Para eso te ha pedido crear un programa con un método o función con la siguiente firma (En
alguno de los siguiente lenguajes: Java / Golang / C-C++ / Javascript (node) / Python / Ruby):

boolean isMutant(String[] dna); // Ejemplo Java

En donde recibirás como parámetro un array de Strings que representan cada fila de una tabla
de (NxN) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las
cuales representa cada base nitrogenada del ADN.

Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras
iguales, de forma oblicua, horizontal o vertical.


## API

Se implementa api dentro de Google Cloud Platform y desarrollada en Flask, el cual es un microframework en Python.

```bash
Url: https://mutant-test-api-346804.rj.r.appspot.com/
```

El servicio cuenta con dos endpoints mutant y stats.

### Endpoint Mutant

```bash
endpoint: mutant/
method: POST
```
#### Input
```python
{
	"dna": [secuencia]
}
```

#### Output positivo

```python
status_code = 200
{
	"result": True
}
```

#### Output negativo

```python
status_code = 403
{
	"result": False
}
```
### Endpoint Stats
```bash
endpoint: stats/
method: POST
```

#### Output

```python
status_code = 200
{
    "count_human_dna": int,
    "count_mutant_dna": int,
    "ratio": float
}
```

#Instalacion

Para instalación realizar git clone del proyecto dentro de enviroment con python 3.7 o superior

```bash
git clone https://github.com/mezdri/MeLi_Challenge_isMutant.git
```

Ejecutar los siguientes comando para instalar dependencias e iniciar el servicio

```bash
cd MeLi_Challenge_isMutant
pip install -r requirements.txt
python main.py
```

Una vez realizados estos comandos nuestra aplicacion estara escuchando por el puerto 8080


# Testing
Ejecutar en la ruta base del proyecto el siguiente comando para ejecutar las pruebas
```bash
coverage run --source ./ -m unittest discover -s tests/
```

Para obtener un report por consola podemos ejecutar 
```bash
coverage report
```

Y si queremos visualizar de forma mas interactiva dicho reporte ejecutamos

```bash
coverage html
```

Con este ultimo nos creara una ruta dentro del proyecto llamada `htmlcov`