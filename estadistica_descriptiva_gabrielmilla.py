# Librería con funciones que calculan medidas estadísticas. Abreviatura "gm"

# Promedio
def prom(datos):
  """Función que calcula la media aritmética
  de una lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (prom): La media aritmética de los números
          de la lista.
  """
  prom=sum(datos)/len(datos)
  return prom

# Mediana
def med(datos):
  """Función que calcula la mediana de una
  lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (med): La mediana de los números de la lista.
  """
  datos.sort() # Ordenamos la lista en caso de que venga desordenada
  if len(datos)%2 != 0: # Si la cantidad de datos es impar
    med=datos[(len(datos)-1)//2]
    return med
  else: # Cantidad par
    med=(datos[(len(datos)//2)-1]+datos[len(datos)//2])/2
    return med

# Moda
def mod(datos):
  """Función que calcula la moda de una
  lista de números o datos varios.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros, de-
  cimales o strings.
  SALIDA (beta): La moda de los datos de la lista.
  """
  dicMod={}
  for alfa in datos: # Creamos un diccionario vacío donde agregaremos los datos y se contará la cantidad de veces en la que estos aparecen. El valor mayor será la moda
    if alfa not in dicMod:
      dicMod[alfa]=1
    else:
      dicMod[alfa]+=1
  moda=max(dicMod.values()) # Encontramos el valor mayor usando max()
  for beta in dicMod:
    if dicMod[beta]==moda:
      return beta

# Rango
def rango(datos):
  """Función que calcula el rango de una
  lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (rango): El rango de los números de la lista
  como la diferencia entre el punto máximo y
  el mínimo.
  """
  puntoMax=max(datos) # Obtenemos el valor mayor de la lista
  puntoMin=min(datos) # Aquí el menor
  rango=puntoMax-puntoMin # El rango se obtiene a través de la diferencia de estos
  return rango

# Varianza
def varianza(datos):
  """Función que calcula la varianza de una
  lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (var): La varianza de los números de la lista.
  """
  suma_var=0
  media=prom(datos) # Obtenemos la media de la lista
  for i in datos:
    suma_var+=(i-media)**2
  var=suma_var/len(datos)
  return var

# Desviación Estándar
def desv(datos):
  """Función que calcula la desviación
  estándar de una lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (desv): La desviación estándar de los números
          de la lista.
  """
  desv=varianza(datos)**0.5
  return desv

# Cuartil
def cuartil(datos,q):
  """Función que calcula el cuartil de una
  lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
           (q): Cuartil que se desea obtener
  SALIDA (cuartil): El cuartil deseado de los números
          de la lista.
  """
  datos.sort() # Ordenamos la lista en caso de que venga desordenada
  cuartiles=[]
  n=len(datos)
  Pos_q1 = int(n * 0.25)
  Pos_q2 = int(n * 0.5)
  Pos_q3 = int(n * 0.75) # Índices de los cuartiles
  # Casos donde no obtengamos índices enteros (no es divisible por 4)
  if n%4 == 0:
      q1 = (datos[Pos_q1-1]+datos[Pos_q1])/2
      q3 = (datos[Pos_q3-1]+datos[Pos_q3])/2
  else:
      q1 = datos[Pos_q1]
      q3 = datos[Pos_q3]

  q2 = datos[Pos_q2]

  if q == 1:
    return q1
  elif q == 2:
    return q2
  elif q == 3:
    return q3
    
# Rango Intercuartílico
def iqr(datos):
  """Función que calcula el rango intercuartílico
  de una lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (iqr): El rango intercuartílico de los números
          de la lista.
  """
  iqr=cuartil(datos,3)-cuartil(datos,1) # Resta el tercer cuartil con el primero, obteniendo el IQR
  return iqr

# Desviación Mediana Absoluta
def MAD(datos):
  """Función que calcula la desviación mediana
  absoluta
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
  SALIDA (mad): La desviación mediana absoluta de los números
          de la lista.
  """
  mediana=med(datos) # Calculamos la mediana de los datos
  desvAbs=[] # Creamos una lista vacía para añadir el valor absoluto de las desviaciones estándar
  for i in datos:
    desvAbs.append(abs(i-mediana))
  mad=med(desvAbs) # La mediana de esta nueva lista es la MAD
  return mad

# Percentil
def percent(datos,p):
  """Función que calcula el percentil de una
  lista de números.
  ------------------------------------------
  ENTRADA (datos): Una lista con números enteros y/o
           decimales.
           (p): Percentil que se desea obtener
  SALIDA (percent): El percentil deseado de los números
          de la lista.
  """
  datos.sort() # Ordenamos la lista en caso de que venga desordenada
  if p==1: # Primer percentil
    percent=datos[len(datos)//100]
    return percent
  elif p>1: # Percentiles posteriores
    percent=datos[int(len(datos)*p/100)]
    return percent
    
# Coeficiente de correlación
def corr(datosX,datosY):
  """Función que calcula el coeficiente de correlación
  de dos magnitudes.
  ------------------------------------------
  ENTRADA (datosX): Una lista con números enteros y/o
           decimales del eje horizontal.
           (datosY): Una lista con números enteros y/o
           decimales del eje vertical.
  SALIDA (r): El coeficiente de correlación de los datos
  """
  mediaX=prom(datosX)
  mediaY=prom(datosY)
  sumaXY=0
  sumaX2=0
  sumaY2=0
  for i in range(len(datosX)): # Con este ciclo realizamos las sumatorias
    sumaXY+=datosX[i]*datosY[i]
    sumaX2+=datosX[i]**2
    sumaY2+=datosY[i]**2
  r=(len(datosX)*sumaXY-sum(datosX)*sum(datosY))/((len(datosX)*sumaX2-sum(datosX)**2)*(len(datosX)*sumaY2-sum(datosY)**2))**0.5
  return r
