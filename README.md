# integrales_proyectivas
Uso de integrales proyectivas para reconocer si se tiene rostros humanos o no


**Descripción**: Python code.

**Archivos**: 
* Imagenes: IMPORTNATE, las imágenes se colocan en una carpeta llamada "images/"
* Imagen Prueba: IMPORTANTE, la imagen de prueba se usa para ver si esta imagen que contiene una cara humana, según las integrales poryectivas es una cara humana o no.
* Script Integrales Proeyctivas: Script del Colab(principal)

**Solución**: 

1. Ingresamos a Colab y abrimos el archivo(`Tarea_extra/integrales_proyectivas_master_ccs.ipynb`)
2. Una vez abierto, ejecutamos en orden los comandos
3. Declaramos una función que nos divida la imagen en cuadrilateros.

4. Declaramos una función que procesará la nueva imagen.

5. La siguiente celda contiene prácticamente el mismo código que la anterior, con las llamadas a las librerías que nos van a ser de ayuda.

6. En esa celda se carga y redimensiona la imagen, para que todas las imagenes tengan al misma dimension.

7. Dividimos la imagen en 8 rows/filas. Este caso es para el histograma vertical de la cara.

8. Guardamos las listas de las rows en un csv.

9. Dividimos la imagen en caudrilateros. 

10. Elegimos las placas cuadrilateras que caen en las regiones de ojos y boca.

11. Convertimos las placas en matrices y las convertimos en listas para simplificar el proceso de sacar la media de la región. 

12. Guardamos las medias de las regiones de ojos y boca en dos CSV's diferentes.

13. Visualizamos los gráficos.

14. Con un bucle for procedemos a verificar si la nueva imagen es una cara humana o no, caso las medias caigan dentro de los rangos.

15. Con un bucle for procedemos a verificar si la nueva imagen es una cara humana o no, caso las medias caigan dentro de un rango de media de los puntos del dataset original.
