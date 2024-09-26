def image_projection(testimage, im_average, eigen_images, row_num, col_num):
    """
    Funcion que aplica el algoritmo de la proyeccion de una eigenimagen
    como en el paper de Turck y Pentland: 
    http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf
    
    Entradas:
        testimage  : Imagen que se proyectara en el eigenespacio
        im_average : Imagen promedio del eigenespacio generado
        eigen_image: Eigenespacio
        row_num    : Nùmero de filas de la imagen que se proyectara
        col_num    : Nùmero de filas de la imagen que se proyectara
        
    Salidas:
        omegatest  : Vector con los pesos de la imagen proyectada
        im_proy   : Imagen proyectada en el eigenespacio
    """
    
    #Se adquiere el nùmero de eiegenfaces en el eigenespacio
    k = eigen_images.shape[1]
    #Se ingresa la imagen a proyectar y se le resta la imagen promedio del eigenespacio
    testface = testimage - im_average
    
    return omegatest, im_proy