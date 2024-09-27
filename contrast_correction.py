def contrast_correction_per_sample(testimage, sampleimage, sigma = 1.5, graph = 1):
    """
    Funcion para corregir el contraste de una imagen a partir de un
    segmento de otra imagen.
    Esta funcion ayuda a extraer los valores de la dispersion de los
    valores de grisde una muestra de la imagen que estara centrado
    en (cx, cy), de tamaño lado x lado y en funcion d, se ajustarane la desviacion
    estandar de los valores de esta muestra se ajustaran los niveles
    de gris de la imagen a evaluar.
    
    Entradas:
    testimage   : Imagen a evaluar
    sampleimage : Segmento de una imagen con los valores de gris a ajustar
    sigma       : valor para ajustar la correccion de contraste
    graph       : Si se asigna 1 se muestra la sampleimage en consola
    
    Salidas:
    image_correction : Imagen resultante con contraste corregido
    """
    
    sample = sampleimage
    if graph == 1:
        plt.title('Sample')
        plt.imshow(sample, cmap = 'gray')
        plt.show()
    
    x, y = sample.shape
    sample = sample.reshape(x * y, 1)
    mean = np.mean(sample)
    StdDvt = np.std(sample, axis = 0)
    minA = mean - (StdDvt * sigma)
    maxA = mean + (StdDvt * sigma)
    image_correction = 255 * (testimage - minA) / (maxA - minA) + 2.2250738585072014e-308
    image_correction = np.clip(image_correction, 0, 255)
    
    return image_correction.astype(np.uint8)