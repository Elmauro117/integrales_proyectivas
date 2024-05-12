
class procesar_imagenes():
    
    def divide_into_tiles(image, num_rows, num_cols):
        height, width, _ = image.shape
        tiles_height = height // num_rows
        tiles_width = width // num_cols

        tiles = []

        for r in range(num_rows):
            for c in range(num_cols):
                x1 = c * tiles_width
                y1 = r * tiles_height
                x2 = x1 + tiles_width
                y2 = y1 + tiles_height

                tile = image[y1:y2, x1:x2]
                tiles.append(tile)

        return tiles


    def procesar_new_img(image_path):
        image_path = image_path
        for file_name in image_files:
            # Check if the file is an image file (optional)
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.JPG'):
                image_path = os.path.join(folder_path, file_name)
                img = Image.open(image_path)
                img = img.resize((70,95), Image.LANCZOS)
                img = img.convert('L')
                ## los horizontales:
                image = cv2.imread(image_path)
                resized_img = cv2.resize(image, (70,95), interpolation= cv2.INTER_AREA)

            # define el tamaño de cada región a 8 filas
            width, height = img.size[0], img.size[1] // 8

            # Descomponemos la imagen
            bins = []

            for i in range(8):
                img_part = img.crop((0, i*height, width, (i+1)*height))
                imagen_mat = np.array(list(img_part.getdata(band=0)), int)
                bins.append(imagen_mat)

            x_bins = []
            for bin in bins[2:-1]:
                x_bin = sum(bin)/len(bin)
                x_bins.append(x_bin)

            # Dividimos en "placas" definir las rows y cols para ello.
            num_rows = 5
            num_cols = 7

            # Dividimos en placas
            tiles = divide_into_tiles(resized_img, num_rows, num_cols)

            # Convertimos a un numpy array
            tiles_as_matrices = [np.array(tile) for tile in tiles]

            ojos_tiles_medias_top = []
            ojos_tiles_medias_bottom = []
            for i, z in zip(range(7,12), range(14,19)):
                flattenMatrix = tiles_as_matrices[i].flatten()
                flattenMatrix_2 = tiles_as_matrices[z].flatten()
                flattenMatrix = sum(flattenMatrix) / len(flattenMatrix)
                flattenMatrix_2 = sum(flattenMatrix_2) / len(flattenMatrix_2)
                ojos_tiles_medias_top.append(flattenMatrix)
                ojos_tiles_medias_bottom.append(flattenMatrix_2)

            ojos_sum_media_list = []
            for i,z in zip(ojos_tiles_medias_top,ojos_tiles_medias_bottom):
                tile_sum_media = (i + z) /2
                ojos_sum_media_list.append(tile_sum_media)

            boca_tiles_medias = []
            for i in range(22,26):
                flattenMatrix = tiles_as_matrices[i].flatten()
                flattenMatrix = sum(flattenMatrix) / len(flattenMatrix)
                boca_tiles_medias.append(flattenMatrix)
        print("Vertical, Hist_ojos, Hist_boca"),
        return x_bins, ojos_sum_media_list, boca_tiles_medias


    def procesar_imagenes(image_path):
        image_files = image_path

        for file_name in image_files:
            # Check if the file is an image file (optional)
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.JPG'):
                image_path = os.path.join(folder_path, file_name)
                img = Image.open(image_path)
                img = img.resize((70,95), Image.LANCZOS)
                img = img.convert('L')
                ## los horizontales:
                image = cv2.imread(image_path)
                resized_img = cv2.resize(image, (70,95), interpolation= cv2.INTER_AREA)

            # define el tamaño de cada región a 8 filas
            width, height = img.size[0], img.size[1] // 8

            # Descomponemos la imagen
            bins = []

            for i in range(8):
                img_part = img.crop((0, i*height, width, (i+1)*height))
                imagen_mat = np.array(list(img_part.getdata(band=0)), int)
                bins.append(imagen_mat)

            x_bins = []
            for bin in bins[2:-1]:
                x_bin = sum(bin)/len(bin)
                x_bins.append(x_bin)
            print(x_bins)
            print(file_name)

            with open('histograms_vertical.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(x_bins)
            # with open('histograms_vertical.csv', 'w', newline='') as file:
            #   pass

            # with open('histograms_vertical.csv', 'a', newline='') as file:
            #   writer = csv.writer(file)
            #   writer.writerow(x_bins)


            # Dividimos en "placas" definir las rows y cols para ello.
            num_rows = 5
            num_cols = 7

            # Dividimos en placas
            tiles = divide_into_tiles(resized_img, num_rows, num_cols)

            # Convertimos a un numpy array
            tiles_as_matrices = [np.array(tile) for tile in tiles]

                # Podemos observar la cantidad de placas y su forma
                # for i, tile_matrix in enumerate(tiles_as_matrices):
                #     print(f'Tile {i} shape:', tile_matrix.shape)

            ojos_tiles_medias_top = []
            ojos_tiles_medias_bottom = []
            for i, z in zip(range(7,12), range(14,19)):
                flattenMatrix = tiles_as_matrices[i].flatten()
                flattenMatrix_2 = tiles_as_matrices[z].flatten()
                flattenMatrix = sum(flattenMatrix) / len(flattenMatrix)
                flattenMatrix_2 = sum(flattenMatrix_2) / len(flattenMatrix_2)
                ojos_tiles_medias_top.append(flattenMatrix)
                ojos_tiles_medias_bottom.append(flattenMatrix_2)

            ojos_sum_media_list = []
            for i,z in zip(ojos_tiles_medias_top,ojos_tiles_medias_bottom):
                tile_sum_media = (i + z) /2
                ojos_sum_media_list.append(tile_sum_media)

            boca_tiles_medias = []
            for i in range(22,26):
                flattenMatrix = tiles_as_matrices[i].flatten()
                flattenMatrix = sum(flattenMatrix) / len(flattenMatrix)
                boca_tiles_medias.append(flattenMatrix)

            with open('histograms_horizontal_ojos.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(ojos_sum_media_list)

            with open('histograms_horizontal_boca.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(boca_tiles_medias)

        return print("CVS creadoss")