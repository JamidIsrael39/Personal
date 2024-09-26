def image_projection(testimage, im_average, eigen_images, row_num, col_num):
    """
    Funcion que aplica el algoritmo de la proyeccion de una eigenimagen
    como en el paper de Turck y Pentland: 
    http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf
    
    Entradas:
        testimage  : Imagen que se proyectara en el eigenespacio
        im_average : Imagen promedio del eigenespacio generado
        
    Ejemplos
    """
    print("Imprimiendo")