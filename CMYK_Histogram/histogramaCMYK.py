import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Função para carregar a imagem e gerar histogramas
def plot_cmyk_histogram(image_path):
    # Carregar a imagem
    img = Image.open(image_path)

    # Converter a imagem para CMYK
    cmyk_img = img.convert('CMYK')

    # Extrair os canais C, M, Y e K
    c, m, y, k = cmyk_img.split()

    # Converter os canais para arrays numpy
    c_arr = np.array(c)
    m_arr = np.array(m)
    y_arr = np.array(y)
    k_arr = np.array(k)

    # Verificar valores de exemplo dos pixels (por exemplo, o primeiro pixel)
    print("Valores do primeiro pixel:")
    print("Ciano (C):", c_arr[0, 0])
    print("Magenta (M):", m_arr[0, 0])
    print("Amarelo (Y):", y_arr[0, 0])
    print("Preto (K):", k_arr[0, 0])

    # Função para gerar histogramas
    def plot_histogram(channel_array, color, channel_name):
        hist, bins = np.histogram(channel_array.ravel(), bins=256, range=[0, 256])
        bin_centers = (bins[:-1] + bins[1:]) / 2  # Cálculo dos centros dos bins

        plt.plot(bin_centers, hist, color=color, linewidth=2)  # Gráfico de linha
        plt.title(f"Histograma do Canal {channel_name}")
        plt.xlabel("Valor do Pixel")
        plt.ylabel("Frequência")
        
        # Ajustar limites dos eixos
        plt.xlim([-5, 260])  # Adiciona margem no eixo x
        plt.ylim([-10, np.max(hist) * 1.1 + 15])  # Ajuste para aumentar a margem superior e inferior

        # Adicionar linha horizontal no eixo y
        plt.axhline(y=0, color='k', linestyle='--', linewidth=1)  # Linha horizontal no eixo x

    # Criar uma figura para mostrar a imagem e os histogramas
    plt.figure(figsize=(12, 12))

    # Exibir a imagem original
    plt.subplot(3, 2, (1, 2))  # Ocupa as duas colunas da primeira linha
    plt.imshow(img)
    plt.axis('off')  # Desativar os eixos
    plt.title("Imagem Original")

    # Gerar os gráficos dos quatro canais
    plt.subplot(3, 2, 3)
    plot_histogram(c_arr, 'cyan', 'Ciano (C)')

    plt.subplot(3, 2, 4)
    plot_histogram(m_arr, 'magenta', 'Magenta (M)')

    plt.subplot(3, 2, 5)
    plot_histogram(y_arr, 'yellow', 'Amarelo (Y)')

    plt.subplot(3, 2, 6)
    plot_histogram(k_arr, 'black', 'Preto (K)')

    plt.tight_layout()
    plt.show()

# Caminho da imagem
image_path = r"C:\Users\victo\Documents\UNIP - Ciencia da Computação\Processamento de Imagem\Histograma_CMYK\Imagens\floresta_cmyk.jpg"

# Chamar a função
plot_cmyk_histogram(image_path)
 
