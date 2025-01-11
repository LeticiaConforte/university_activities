import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('C:/Users/victo/Downloads/Imagens/monte.jpg')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converter para RGB, pois o OpenCV lê em BGR

# Aplicar a suavização gaussiana com diferentes tamanhos de kernel
gauss_5x5 = cv2.GaussianBlur(imagem_rgb, (5, 5), 0)
gauss_25x25 = cv2.GaussianBlur(imagem_rgb, (25, 25), 0)
gauss_99x99 = cv2.GaussianBlur(imagem_rgb, (99, 99), 0)

# Plotar as imagens
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

ax[0].imshow(imagem_rgb)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(gauss_5x5)
ax[1].set_title('Gaussiana 5x5')
ax[1].axis('off')

ax[2].imshow(gauss_25x25)
ax[2].set_title('Gaussiana 25x25')
ax[2].axis('off')

ax[3].imshow(gauss_99x99)
ax[3].set_title('Gaussiana 99x99')
ax[3].axis('off')

plt.show()
