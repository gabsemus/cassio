import streamlit as st

from datetime import datetime
from pytz import timezone

import random

data_hora = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_hora = data_hora.astimezone(fuso_horario)
data = data_hora.strftime('%d')
hora = data_hora.strftime('%H:%M')

def home():


   nome_local = 'Kingdom'
   st.title(f'Bem-vindo a {nome_local}')

   st.subheader(f"Hoje, dia {data}, temos as seguintes atrações: ")

   line = ['DJ Sande', 'DJ Stizi', 'DJ Aron Kawillian', 'DJ Gouveia']

   emoji = [':full_moon:', ':new_moon_with_face:', ':full_moon_with_face:', ':headphones:', ':hatched_chick:', ':lips:', ':fire:', '	:firecracker:']



   for dj in line:
      rand_idx = random.randrange(len(emoji))
      random_num = emoji[rand_idx]
      st.markdown(f'{str(random_num)} **{dj}**')


   st.subheader(f"Temos as seguintes promoções: ")

   promo = {
            'Bebida': 'Gin em dobro até as 21h',
            'Rosh': 'Rosh em dobro até as 24h'
   }
   col1, col2 = st.columns(2)

   for produto in promo:
      with col1:
         st.markdown(f'**{produto}**')
      with col2:
         st.markdown(f'{promo[produto]}')




def cadastro_usuario():
   st.subheader('Cadastro do Cliente')

   with st.form("CadastroUsuario"):
      st.write("Cadastro do Cliente")
      usuario_nome = st.text_input("Nome: ", placeholder = 'Informe o nome do cliente')
      usuario_celular = st.text_input("Celular", help = 'Informe o DDD + Número' ,placeholder = 'Informe o celular do cliente')

      # Every form must have a submit button.
      submitted = st.form_submit_button("Salvar")
      if submitted:
          # st.write("Nome: ", usuario_nome)
          # st.write("Celular: ", usuario_celular)
          st.write('Registro Salvo!')



def registrar_entrada():
   st.subheader('Registrar Entrada')

   with st.form("RegistrarEntrada"):
      st.write("Entrada do Cliente")
      usuario_nome = st.selectbox(label="Nome: ",options = ('gab', 'luiza', 'diego'), help  = 'Informe o nome do cliente')

      usuario_comanda = st.text_input("Pulseira" ,placeholder = 'Informe o número da pulseira')

      col1, col2 = st.columns(2)

      with col1:
         contato_usuario = st.text("Contato do Cliente:")

      with col2:
         contato_usuario = st.text('usuario_celular')

      atualizar_celular = st.text_input("Atualizar Celular", help = 'Informe o DDD + Número' ,placeholder = 'Informe o celular do cliente')

      # Every form must have a submit button.
      submitted = st.form_submit_button("Salvar")
      if submitted:
          # st.write("Nome: ", usuario_nome)
          # st.write("Celular: ", usuario_celular)
          st.write('Registro Salvo!')

def registrar_pedido():
   st.subheader('Registrar Pedido')

   with st.form("RegistrarPedido"):
      st.write("Registrar Pedido")

      usuario_comanda = st.selectbox(label="Pulseira: ",options = ('1', '2', '3'), help  = 'Informe o nome do cliente')

      col1, col2 = st.columns(2)

      with col1:
         contato_usuario = st.text("Nome do Cliente:")

      with col2:
         contato_usuario = st.text('usuario_nome')

      usuario_pedido = st.multiselect(label="Pulseira: ",options = ('1', '2', '3'), help  = 'Informe o nome do cliente', default = None)

      if usuario_pedido:
         for pedido in usuario_pedido:
            st.write(pedido)

      # Every form must have a submit button.
      submitted = st.form_submit_button("Salvar")
      if submitted:
          # st.write("Nome: ", usuario_nome)
          # st.write("Celular: ", usuario_celular)
          st.write('Registro Salvo!')

def saldo_cliente():
   st.subheader('Conta do Cliente')

   with st.form("SaldoUsuario"):
      st.write("Visualizar o saldo do cliente")

      usuario_comanda = st.selectbox(label="Pulseira: ",options = ('1', '2', '3'), help  = 'Informe o nome do cliente')

      col1, col2 = st.columns(2)

      with col1:
         contato_usuario = st.text("Nome do Cliente:")

      with col2:
         contato_usuario = st.text('usuario_nome')

      # total_comanda = 0
      #
      # if usuario_comanda:
      #    for pedido in usuario_pedido:
      #       st.write(pedido)
      #       total_comanda += pedido

      # Every form must have a submit button.
      submitted = st.form_submit_button("Salvar")
      if submitted:
          # st.write("Nome: ", usuario_nome)
          # st.write("Celular: ", usuario_celular)
          st.write('Registro Salvo!')

page_names_to_funcs = {
   "Home": home,
   "Cadastro do Usuário": cadastro_usuario,
   "Registrar Entrada": registrar_entrada,
   "Registrar Pedido": registrar_pedido,
   "Saldo do Cliente": saldo_cliente
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
