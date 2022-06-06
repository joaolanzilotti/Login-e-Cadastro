# ----------------------É USADO PARA DIMINUIR O TAMANHO DE UMA IMAGEM OU COLOCAR IMAGEM EM UM BOTÃO----------------------
# imagem = Image.open('interfacepythonaula/imagens-icones/botao.png') => Abre a Imagem
# imagem = imagem .resize((110,40)) => mudar o tamanho da imagem
# imagem = ImageTk.PhotoImage(imagem )

# imagem_label = Label(janela, image=imagem, anchor='nw',bd=0,activebackground="#3b3b3b") => Cria a Label Para colocar a imagem
# imagem_label.place(x=50,y=410) => Posiciona a Imagem

# botaoPil = Image.open('interfacepythonaula/imagens-icones/botao.png')
# botaoPil  = botao .resize((90,40))
# botaoPil  = ImageTk.PhotoImage(botao )


# botao_cadastro= Button(janela, image=botao, anchor='nw',bd=0,activebackground="#3b3b3b")
# botao_cadastro.place(x=50,y=210)

# Para executar uma def use: tela_inicial()


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import time

def voltarlogin():
    janela.destroy()
    time.sleep(0.2)
    janela_nova()

def voltarcadastro():
    janela_login.destroy()
    time.sleep(0.2)
    tela_inicial()
def janela_nova():
    global janela_login
    janela_login = Tk()
    janela_login.geometry('415x550+750+250')
    janela_login.title('LOGIN JP')
    janela_login.iconbitmap('imagens-icones/login.ico')
    janela_login.configure(bg='#151515')

    janela_login2 = Frame(janela_login, width=400, height=600, bg='#151515', bd=0)
    janela_login2.place(x=30,y=20)

    imagem_titulo = Image.open('imagens-icones/Titulo imagem3.png')
    imagem_titulo  = imagem_titulo.resize((300,500))
    imagem_titulo  = ImageTk.PhotoImage(imagem_titulo)
    imagem_titulo2 = Label(janela_login2, image=imagem_titulo, bg='#151515', bd=0)
    imagem_titulo2.place(x=25, y=0)
    texto_titulo = Label(janela_login, text='Seja Bem Vindo',bg='#242424',foreground='white', font=('Lucky Skirt Regular',16))
    texto_titulo.place(x=135,y=120)

    Imagem_Email = Image.open('imagens-icones/Figura Usuario.png')
    Imagem_Email  = Imagem_Email .resize((250,40))
    Imagem_Email  = ImageTk.PhotoImage(Imagem_Email)
    Imagem_Email1 = Label(janela_login2, image=Imagem_Email,bg='#242424', bd=0)
    Imagem_Email1.place(x=50, y=205)
    texto_Email = Label(janela_login2, text='Email: * ',font=('Simply Olive Regular',17), background='#242424', bd=0, foreground='white')
    texto_Email.place(x=70, y=171)
    Caixa_Email = Entry(janela_login2)
    Caixa_Email.config(width=22,bd=0,  relief='solid', font=('',12),justify='left')
    Caixa_Email.focus()
    Caixa_Email.place(x=90, y=215)

    Imagem_Senha = Image.open('imagens-icones/Figura Senha.png')
    Imagem_Senha  = Imagem_Senha .resize((250,40))
    Imagem_Senha  = ImageTk.PhotoImage(Imagem_Senha)
    Imagem_Senha1 = Label(janela_login2, image=Imagem_Senha, bg='#242424')
    Imagem_Senha1.place(x=50, y=300)
    texto_senha = Label(janela_login2, text='Senha: *',font=('Simply Olive Regular',17), background='#242424', bd=0, foreground='white')
    texto_senha.place(x=70, y=265)
    caixa_senha = Entry(janela_login2)
    caixa_senha.config(width=22,bd=0,  relief='solid', font=('',12),justify='left', show='*')
    caixa_senha.place(x=90, y=313)

    imagemlogin = Image.open('imagens-icones/botao login.png')
    imagemlogin  = imagemlogin .resize((130,45))
    imagemlogin  = ImageTk.PhotoImage(imagemlogin )
    botao_login= Button(janela_login2, image=imagemlogin,bg='#242424', anchor='nw',bd=0,activebackground="#242424", command='')
    botao_login.place(x=110,y=360)

    botao_esqueceusenha = Button(janela_login2,text='Esqueceu a sua Senha?',font=('Arial',11),bd=0, background='#242424', activebackground='#242424', foreground='white')
    botao_esqueceusenha.place(x=90, y=435)

    botao_criarconta = Button(janela_login2,text='Criar Conta',font=('Arial',11),bd=0, background='#242424', activebackground='#242424', foreground='white', command=voltarcadastro)
    botao_criarconta.place(x=130, y=458)
    janela_login.mainloop()


def tela_inicial():
    global janela
    janela = Tk()
    janela.geometry('415x550+750+250')
    janela.title('Cadastro JP')
    janela.iconbitmap('imagens-icones/login.ico')
    janela.configure(bg='#151515')

    janela_cadastro = Frame(janela, width=400, height=600, bg='#151515', bd=0)
    janela_cadastro.place(x=30,y=20)



    def inserir():
        if (caixa_nome.get()==""):
            print("nada")
        
        else:

            conexao = mysql.connector.connect(host='localhost',user='root',password='',database='cadastro')
            cursor = conexao.cursor()
            comando = f'INSERT INTO clientes (Nome, Email, Senha) VALUES ("{caixa_nome.get()}", "{caixa_email.get()}", "{caixa_senha.get()}")'
            try: 
                cursor.execute(comando)
                conexao.commit()
                cursor.close()
                conexao.close()
                janela.destroy()
                janela_nova() 
            except:
                print("erro ao cadastrar")      


    Imagem_Titulo = Image.open('imagens-icones/Titulo imagem3.png')
    Imagem_Titulo  = Imagem_Titulo .resize((300,500))
    Imagem_Titulo  = ImageTk.PhotoImage(Imagem_Titulo)

    Imagem_Titulo1 = Label(janela_cadastro, image=Imagem_Titulo, bg='#151515', bd=0)
    Imagem_Titulo1.place(x=25, y=0)

    texto_titulo = Label(janela, text='Crie Sua Conta',bg='#242424',foreground='white', font=('Lucky Skirt Regular',16))
    texto_titulo.place(x=135,y=120)

    Imagem_usuario = Image.open('imagens-icones/Figura Usuario.png')
    Imagem_usuario  = Imagem_usuario .resize((250,40))
    Imagem_usuario  = ImageTk.PhotoImage(Imagem_usuario)

    Imagem_usuario1 = Label(janela_cadastro, image=Imagem_usuario,bg='#242424', bd=0)
    Imagem_usuario1.place(x=50, y=185)

    nome = Label(janela_cadastro, text='Nome: * ',font=('Simply Olive Regular',17), background='#242424', bd=0, foreground='white')
    nome.place(x=70, y=150)
    caixa_nome = Entry(janela_cadastro)
    caixa_nome.config(width=22,bd=0,  relief='solid', font=('',12),justify='left')
    caixa_nome.focus()
    caixa_nome.place(x=90, y=194)

    Imagem_email = Image.open('imagens-icones/Figura email.png')
    Imagem_email  = Imagem_email .resize((250,40))
    Imagem_email  = ImageTk.PhotoImage(Imagem_email)

    Imagem_email1 = Label(janela_cadastro, image=Imagem_email, bg='#242424', bd=0)
    Imagem_email1.place(x=50, y=265)

    email = Label(janela_cadastro, text='E-mail: *',font=('Simply Olive Regular',17), background='#242424', bd=0, foreground='white')
    email.place(x=70, y=230)
    caixa_email = Entry(janela_cadastro)
    caixa_email.config(width=22,bd=0, font=('',12),justify='left')
    caixa_email.place(x=90, y=274)

    Imagem_Senha = Image.open('imagens-icones/Figura Senha.png')
    Imagem_Senha  = Imagem_Senha .resize((250,40))
    Imagem_Senha  = ImageTk.PhotoImage(Imagem_Senha)

    Imagem_Senha1 = Label(janela_cadastro, image=Imagem_Senha, bg='#242424')
    Imagem_Senha1.place(x=50, y=345)

    senha = Label(janela_cadastro, text='Senha: *',font=('Simply Olive Regular',17), background='#242424', bd=0, foreground='white')
    senha.place(x=70, y=312)
    caixa_senha = Entry(janela_cadastro)
    caixa_senha.config(width=22,bd=0,  relief='solid', font=('',12),justify='left', show='*')
    caixa_senha.place(x=90, y=358)

    #botao_cadastro = Button(janela, text='Cadastrar', bd = '5', width=15, bg='#909090', foreground='white',font=('BubbleGum',10))
    #botao_cadastro.place(x=78, y=300)

    # --------------------------- Imagem e Tamanho --------------------------- #
    #imagem = Image.open('interfacepythonaula/imagens-icones/botao.png')
    #imagem = imagem .resize((110,40)) 
    #imagem = ImageTk.PhotoImage(imagem )

    #imagem_label = Label(janela, image=imagem, anchor='nw',bd=0,activebackground="#3b3b3b")
    #imagem_label.place(x=50,y=410)
    # --------------------------- BOTÃO POSSUI CONTA --------------------------- #
    botao_facalogin = Button(janela_cadastro,text='Já possui conta? Faça Login',font=('Arial',11),bd=0, background='#242424', activebackground='#242424', foreground='white',command=voltarlogin)
    botao_facalogin.place(x=78, y=458)
    # --------------------------- BOTÃO CADASTRO COM IMAGEM --------------------------- #
    imagemcadastro = Image.open('imagens-icones/botao2.png')
    imagemcadastro  = imagemcadastro .resize((110,45))
    imagemcadastro  = ImageTk.PhotoImage(imagemcadastro )

    botao_cadastro= Button(janela_cadastro, image=imagemcadastro,bg='#242424', anchor='nw',bd=0,activebackground="#242424", command=inserir)
    botao_cadastro.place(x=120,y=393)
    janela.mainloop()


tela_inicial()
