# Aplicação de Suavização Gaussiana em Python

## Descrição
Este projeto utiliza a técnica de **Suavização Gaussiana** para reduzir ruídos em imagens. A suavização é aplicada com diferentes tamanhos de kernel, permitindo observar os efeitos do filtro em uma imagem carregada. O resultado é exibido lado a lado com a imagem original.

## Funcionalidades
- Carregar uma imagem no formato RGB.
- Aplicar a suavização gaussiana com tamanhos de kernel variados:
  - Kernel 5x5.
  - Kernel 25x25.
  - Kernel 99x99.
- Comparar os resultados da suavização com a imagem original.

## Tecnologias Utilizadas
- **Python 3**
- Bibliotecas:
  - `OpenCV`: Para manipulação de imagens e aplicação do filtro gaussiano.
  - `Matplotlib`: Para exibir as imagens e seus resultados.

## Como Executar

1. **Pré-requisitos**:
   - Python 3 instalado no sistema.
   - Instalar as bibliotecas necessárias:
     ```bash
     pip install opencv-python matplotlib
     ```

2. **Configurar o Caminho da Imagem**:
   - Substitua o caminho `'C:/Users/victo/Downloads/Imagens/monte.jpg'` pela localização da imagem desejada no seu sistema.

3. **Executar o Código**:
   - Rode o script Python:
     ```bash
     python Aplicação_Suavização_Gaussiana.py
     ```

4. **Visualizar os Resultados**:
   - O programa exibirá:
     - A imagem original.
     - As imagens suavizadas com os kernels de 5x5, 25x25 e 99x99.

## Exemplo de Uso
- Imagem original exibida ao lado de suas versões suavizadas para facilitar a comparação.

## Melhorias Futuras
- Adicionar suporte para seleção de imagens via interface gráfica.
- Implementar a opção de salvar as imagens suavizadas.
- Permitir ajustes dinâmicos no tamanho do kernel durante a execução.

---

**Autor**: Desenvolvido para aprendizado e demonstração de processamento de imagens com filtros gaussianos.

**Licença**: MIT
