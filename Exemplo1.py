import streamlit as st
from ACTlib import *
from PIL import Image # Lib para carregar imagem 

def main():
    Configurar_Pagina(
        "Exemplo 1", 
        "amplo", 
        "auto", 
        "https://docs.streamlit.io", 
        "mailto:informacoes.actsp@gmail.com", 
        "ACT - Soluções para Pessoas. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*",
        "©️")
    
    cor = "azul"
    
    coluna0 = Colunas(3)    
    with coluna0[0]:
        Escrever(" ", "subtitulo")        
        #image = Image.open('imgs/teclado.jpg')
        #st.image(image, caption="Teclado", width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
        Imagem(caminho='imgs/www.png', rotulo = "Web", dimensao = 100, formato_saida = "auto")
    with coluna0[1]:
        MKD("MEU 1º APLICATIVO WEB PYTHON", alinhamento = "centro", tamanho_fonte = 44, cor_fonte = "azul")
    with coluna0[2]:
        Escrever("")

    Divisor()
    
    coluna1 = Colunas(3)
    with coluna1[0]:
        Escrever("")
    with coluna1[1]:
        Titulo("ACTlib Versão 0.1")
        nome = Ler(rotulo = "Nome:", nmax=30, tipo="padrao", info="Inserção de Nome", autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder="Não esqueça de preencher seu nome", desabilitada="falso", visibilidade="visivel")
        if nome:     
            Escrever("Seja Bem vinda(o), " + nome + "!")
    with coluna1[2]:
        Escrever("")
    
        
    MKD("A vida não é um conto de fadas, mas pode ser repleta de momentos mágicos!", alinhamento = "justificado", tamanho_fonte = 64, cor_fonte = cor)
    

    
    Barra_Lateral_Imagem(caminho='imgs/teclado.jpg', preencher = "verdadeiro")
    Barra_Lateral_Divisor()
    Barra_Lateral_Texto("Desenvolvido por Massaki de O. Igarashi")
    Barra_Lateral_Texto("Em Maio/2024", "auto")
if __name__ == '__main__':
    main()