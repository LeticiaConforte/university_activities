# Histograma CMYK com Python

## Descrição
Este projeto é uma ferramenta para gerar histogramas dos canais de cor **CMYK** de uma imagem utilizando Python. Ele carrega uma imagem, converte para o espaço de cor CMYK e gera gráficos para analisar a distribuição dos valores de pixel em cada canal (Ciano, Magenta, Amarelo e Preto).

## Funcionalidades
- Carregar imagens no formato RGB e converter para CMYK.
- Extrair e exibir valores de pixel dos canais de cor CMYK.
- Gerar histogramas individuais para cada canal.
- Visualizar a imagem original junto com os gráficos.

## Tecnologias Utilizadas
- **Python 3**
- Bibliotecas:
  - `Pillow (PIL)`: Para manipulação e conversão de imagens.
  - `Matplotlib`: Para plotar os histogramas.
  - `Numpy`: Para operações de manipulação e cálculo com arrays.

## Como Executar

1. **Pré-requisitos**:
   - Python 3 instalado no sistema.
   - Instalar as bibliotecas necessárias:
     ```bash
     pip install pillow matplotlib numpy
     ```

2. **Configurar o Caminho da Imagem**:
   - Substitua o valor da variável `image_path` no código pelo caminho da sua imagem.

3. **Executar o Código**:
   - Rode o script Python:
     ```bash
     python histogramaCMYK.py
     ```

4. **Visualizar os Resultados**:
   - O programa exibirá:
     - A imagem original.
     - Histogramas para os canais Ciano (C), Magenta (M), Amarelo (Y) e Preto (K).

## Exemplo de Saída
1. Imagem original exibida.
2. Histogramas individuais mostrando a frequência dos valores de pixel em cada canal CMYK.

## Melhorias Futuras
- Adicionar suporte para diferentes formatos de imagem (ex.: PNG, TIFF).
- Implementar a opção de salvar os histogramas como arquivos de imagem.
- Adicionar interface gráfica para facilitar a interação.

---

**Autor**: Desenvolvido para fins acadêmicos e de aprendizado em Processamento de Imagens.

**Licença**: MIT