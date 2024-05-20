import streamlit as st
from types import FunctionType
from deep_translator import GoogleTranslator
from PIL import Image # Lib para carregar imagem 

#Ref colors: https://hexcolorpedia.com/color/?q=ffffff

def Versao():
    return "ACTlib Versão 0.1"

def Indice():
    Configuracoes_de_Pagina = st.sidebar.popover("Configurações de Página")
    Configuracoes_de_Pagina.page_link("pages/Configurar_Pagina.py", label="	📄 Configurar_Pagina")
    Configuracoes_de_Pagina.page_link("pages/Barra_Lateral_Texto.py", label="⬜ Barra_Lateral_Texto")

def Pt2En(palavraPT):
    tradutor = GoogleTranslator(source= "pt", target= "en")
    traducaoEN = tradutor.translate(palavraPT)
    return traducaoEN
    
def En2Pt(palavraEN):
    tradutor = GoogleTranslator(source= "en", target= "pt")
    traducaoPT = tradutor.translate(palavraEN)
    return traducaoPT
    
#├──CONFIGURAÇÕES DE PÁGINA
#   └── Configurar_Pagina
#   └── Barra_Lateral_Texto
#   └── Barra_Lateral_Botao_M
#   └── Barra_Lateral_Botao_Colorido
#   └── Barra_Lateral_Divisor
#   └── Divisor

def Configurar_Pagina(titulo  = "ACT - Soluções para Pessoas", layout="amplo", barra_lateral = "auto", ajuda = "https://docs.streamlit.io", bug = "mailto:informacoes.actsp@gmail.com",sobre="#### **ACT - Soluções para Pessoas**. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*", icone = "	©️"):
    #https://docs.streamlit.io/develop/concepts/architecture/app-chrome
    Configurar_Pagina.titulo = titulo    
    if layout == "amplo":
        Configurar_Pagina.layout = "wide"
    elif layout == "centralizado":
        Configurar_Pagina.layout = "centered"
    else:
        Configurar_Pagina.layout = "wide"
        
    Configurar_Pagina.barra_lateral = barra_lateral
    Configurar_Pagina.icone = icone
    st.set_page_config(page_title=titulo,                        
                        layout = Configurar_Pagina.layout,
                        initial_sidebar_state = barra_lateral,
                        menu_items={
                            'Get Help': (ajuda),
                            'Report a bug': (bug),
                            'About': (sobre)
                        },
                        page_icon=icone)

def Barra_Lateral_Texto(texto = "Texto exibido na Barra Lateral", estilo = "auto"):
    Barra_Lateral_Texto.texto = texto
    Barra_Lateral_Texto.estilo = estilo
    if estilo.lower()=="auto":
        st.sidebar.write(texto)
    elif estilo.lower() =="codigo":
        st.code(texto)
    elif estilo.lower()=="subcabecalho":
        st.sidebar.subheader(texto)
    elif estilo.lower()=="cabecalho":
        st.sidebar.header(texto)
    elif estilo.lower()=="titulo":
        resp = st.title(texto)
    elif estilo.lower()=="destaque1":
        st.sidebar.info(texto)          
    elif estilo.lower()=="destaque2":
        st.sidebar.warning(texto) 
    elif estilo.lower()=="destaque3":
        st.sidebar.success(texto)
    elif estilo.lower()=="erroexc":
        e = RuntimeError(texto)
        st.sidebar.exception(e)
    elif estilo.lower()=="erro":
        st.sidebar.error(texto, icon="❌")
    else:
        st.sidebar.write(texto)
  
def Barra_Lateral_Botao(rotulo, chave = 1, info="", tipo="secundário", desabilitado="falso", expandido="falso"):
    Barra_Lateral_Botao.rotulo = rotulo
    
    if  desabilitado.lower()=="verdadeiro":
        des = True
    else:
        des = False
      
    if  expandido.lower()=="verdadeiro":
        exp = True
    else:
        exp = False
    respBTNbarra_lateral = st.sidebar.button(label=rotulo, key=chave, help=info, type=Pt2En(tipo), disabled=des, use_container_width=exp)
    Barra_Lateral_Botao.estado = respBTNbarra_lateral
    return respBTNbarra_lateral

def Barra_Lateral_Botao_Colorido(texto, cor = "#7e7b7b"):
    Botao_Colorido.rotulo = texto
    Botao_Colorido.cor = cor
    st.sidebar.markdown("""<style>  .element-container:has(style){display: none;} #button-afterL {display: none;}
                            .element-container:has(#button-afterL) {display: none;}
                            .element-container:has(#button-afterL) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.sidebar.markdown('<span id="button-afterL"></span>', unsafe_allow_html=True)
    respBTNColorL = st.sidebar.button(texto)
    return respBTNColorL
def Barra_Lateral_Container(borda = "ativa"):
    if borda == "desativa":
        Border = False
    else:
        Border = True
    return st.sidebar.container(border = Border)

def Barra_Lateral_Divisor():
    st.sidebar.divider()

def Barra_Lateral_Imagem(caminho='imgs/Webapp1.png', rotulo = None, dimensao=300, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto"):
    if preencher.lower() == "verdadeiro":
        preencher = True
    else:
        preencher = False
        
    if clamp.lower() == "verdadeiro":
        clamp = True
    else:
        clamp = False
        
    image = Image.open(caminho)
    st.sidebar.image(image, caption=rotulo, width=dimensao, use_column_width=preencher, channels=padrao_cor, output_format=formato_saida)

def Colunas(ncol):
    return st.columns(ncol)
    
def Container(borda = "ativa"):
    if borda == "desativa":
        Border = False
    else:
        Border = True
    return st.container(border = Border)
    
def Divisor():
    st.divider()
def Imagem(caminho='imgs/Webapp1.png', rotulo = None, dimensao=None, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto"):
    if preencher.lower() == "verdadeiro":
        preencher = True
    else:
        preencher = False
        
    if clamp.lower() == "verdadeiro":
        clamp = True
    else:
        clamp = False
        
    image = Image.open(caminho)
    st.image(image, caption=rotulo, width=dimensao, use_column_width=preencher, channels=padrao_cor, output_format=formato_saida)

def Link(caminho, rotulo = "Link de Página"):
    Link.caminho = caminho
    Link.rotulo = rotulo
    st.page_link(caminho, label=rotulo)

def Mudar_Tema():
    #REF: https://discuss.streamlit.io/t/customize-theme/39156/4
    dark = '''
    <style>
        .stApp {
        background-color: black;  
        }
    </style>
    '''

    light = '''
    <style>
        .stApp {
        background-color: gray;
        }
    </style>
    '''
    st.markdown(light, unsafe_allow_html=True)

    # Create a toggle button
    toggle = st.button("Mudar Tema")

    # Use a global variable to store the current theme
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Change the theme based on the button state
    if toggle:
        if st.session_state.theme == "light":
            st.session_state.theme = "dark"
        else:
            st.session_state.theme = "light"

    # Apply the theme to the app
    if st.session_state.theme == "dark":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)

    # Display some text
    st.write("This is a streamlit app with a toggle button for themes.")

#├──BOTÕES
#   └── Botao_M
#   └── Botao_Colorido
def Botao(rotulo, chave = 1, info=None, tipo="secundário", desabilitado="falso", expandido="falso"):
    
    if  desabilitado.lower()=="verdadeiro":
        des = True
    else:
        des = False
      
    if  expandido.lower()=="verdadeiro":
        exp = True
    else:
        exp = False
    respBTNMono = st.button(label=rotulo, key=chave, help=info, type=Pt2En(tipo), disabled=des, use_container_width=exp)
    return respBTNMono
    
def Botao_Colorido(rotulo, cor = "#7e7b7b"):
    Botao_Colorido.cor = cor
    st.markdown("""<style>  .element-container:has(style){display: none;} #button-after {display: none;}
                            .element-container:has(#button-after) {display: none;}
                            .element-container:has(#button-after) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    respBTNColor = st.button(rotulo)
    return respBTNColor
    
#├──RECURSOS DE ENTRADA
#   └── Ler
#   └──   

def Ler(rotulo = "", valor=None, nmax=None, chave=None, tipo="padrão", info=None, autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder=None, desabilitada="falso", visibilidade="visivel"):
    Ler.rotulo = rotulo
    Ler.valor = valor 
    Ler.nmax = nmax 
    Ler.chave = chave, 
    Ler.tipo = tipo 
    Ler.info = info
    Ler.autocompletar = autocompletar
    Ler.na_mudanca = na_mudanca
    Ler.desabilitada = desabilitada
    Ler.visibilidade = visibilidade
    #visibilidade: "visível", "oculto" ou "recolhido"
    if tipo.lower() == "senha":
        tipo = "password"
    else:
        tipo = "default"

    if desabilitada.lower() == "falso":
        desabilitada = False
    else:
        desabilitada = True
    
    if visibilidade.lower()=="oculto":
        visibilidade = "hidden"
    elif visibilidade.lower()=="recolhido":
        visibilidade = "collapsed"
    else:
        visibilidade = "visible"   

    return st.text_input(label = rotulo, value=valor, max_chars=nmax, key=chave, type=Pt2En(tipo), help=info, autocomplete=autocompletar, on_change=na_mudanca, args=args, kwargs=kwargs, placeholder=placeholder, disabled=desabilitada, label_visibility=visibilidade)
    
#├──RECURSOS DE SAÍDA
#   └── Escrever
#   └── Subcabecalho
#   └── Cabecalho
#   └── Texto_em_Coluna
#   └── Titulo

def Escrever(texto, estilo = "auto"):
    Escrever.texto = texto
    Escrever.estilo = estilo
    if estilo.lower()=="auto":
        st.write(texto)
    elif estilo.lower() =="codigo":
        st.code(texto)
    elif estilo.lower()=="subcabecalho":
        st.subheader(texto)
    elif estilo.lower()=="cabecalho":
        st.header(texto)
    elif estilo.lower()=="titulo":
        resp = st.title(texto)
    elif estilo.lower()=="destaque1":
        st.info(texto)          
    elif estilo.lower()=="destaque2":
        st.warning(texto) 
    elif estilo.lower()=="destaque3":
        st.success(texto)
    elif estilo.lower()=="erroexc":
        e = RuntimeError(texto)
        st.exception(e)
    elif estilo.lower()=="erro":
        st.error(texto, icon="❌")
    else:
        st.write(texto)
        
def Subcabecalho(texto):
    Subcabecalho.texto = texto
    st.subheader(texto)

def Cabecalho(texto):
    Cabecalho.texto = texto
    st.header(texto)
    
def MKD(texto, alinhamento = "esquerda", tamanho_fonte = 28, cor_fonte = "preto"):
    if alinhamento.lower()=="justificado":
        alinhamento = "justified" 
    elif alinhamento.lower()=="esquerda":
        alinhamento = "left"
    elif alinhamento.lower()=="direita":
        alinhamento = "right"
    elif alinhamento.lower()=="centro":
        alinhamento = "center"
    elif alinhamento.lower()=="centralizado":
        alinhamento = "center"        
    else:
        alinhamento = "justified"
        
    conteudo = '<p style="font-weight: bolder; color:%s; font-size: %spx;">%s</p>'%(Pt2En(cor_fonte), tamanho_fonte, texto)    
    st.markdown(conteudo, unsafe_allow_html=True)
    mystyle0 = '''<style> p{text-align:%s;}</style>'''%(alinhamento)
    st.markdown(mystyle0, unsafe_allow_html=True) 
    
def Texto_em_Colunas(TEXTO, estilo = "auto"):    
    ncol = len(TEXTO)
    if ncol>20:
        ncol = 20
    comando = []
    for c in range(ncol):
        label = TEXTO[c]
        if estilo=="auto":
            comando.append("st.write('%s')"%(label))
        elif estilo=="subcabecalho":
            comando.append("st.subheader('%s')"%(label))
        elif estilo=="cabecalho":
            comando.append("st.header('%s')"%(label))
        elif estilo=="titulo":
            comando.append("st.title('%s')"%(label)) 
        elif estilo=="destaque1":
            comando.append("st.info('%s')"%(label))           
        elif estilo=="destaque2":
            comando.append("st.warning('%s')"%(label))   
        elif estilo=="destaque3":
            comando.append("st.success('%s')"%(label)) 
        else:
            comando.append("st.write('%s')"%(label))
    colunas = st.columns(ncol) 
    for i in range(ncol):
        with colunas[i]:
            if i==0:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[0]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==1:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[1]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==2:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[2]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==3:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[3]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==4:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[4]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==5:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[5]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()           
            if i==6:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[6]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==7:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[7]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==8:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[8]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==9:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[9]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==10:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[10]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==11:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[11]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()  
            if i==12:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[12]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==13:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[13]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==14:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[14]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==15:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[15]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()           
            if i==16:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[16]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==17:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[17]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==18:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[18]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()
            if i==19:
                f_code = compile('''def FUNC(): 
                                        %s
                                '''%(comando[19]), "<int>", "exec") 
                f_func = FunctionType(f_code.co_consts[0], globals(), "FUNC")
                f_func()

def Titulo(texto):
    Titulo.texto = texto
    st.title(texto)
