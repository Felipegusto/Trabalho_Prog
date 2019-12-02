import os 
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq="bla.bd"
db=SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Camisa(BaseModel):
	cor_camisa = CharField()
	tamanho_camisa = CharField()
	marca_ camisa = CharField()
	preco_camisa = CharField()

class Calca(BaseModel):
	cor_calca = CharField()
	tamanho_calca = CharField()
	marca_calca = CharField()
	preco_calca = CharField()

class Bermuda(BaseModel):
	cor_bermuda = CharField()
	tamanho_bermuda = CharField()
	marca_bermuda = CharField()
	preco_bermuda = CharField()

class Meia(BaseModel):
	cor_meia = CharField()
	tipo_meia = CharField()
	preco_meia = CharField()

class Sapato(BaseModel):
	nome_sapato = CharField()
	cor_sapato = CharField()
	marca_sapato = CharField()
	tamanho_sapato = CharField()
	preco_sapato = CharField()

class Cliente(BaseModel):
	nome_cliente = CharField()
	telefone_cliente = CharField()
	cpf_cleinte = CharField()
	conta_cliente = CharField()

class Funcionario(BaseModel):
	nome_funcionário = CharField()
	telefone_funcionario = CharField()
	codigo_funcioario = CharField()
	comissao_funcionario = CharField()


db.connect()
db.create_tables([Camisa, Calca, Bermuda,Meia, Sapato, Clienten Funcionario, Compra])
camisa1= Camisa.create(cor_camisa = "Amarelo" , tamanho_camisa = "GG" , marca_camisa = "Adidas" , preco_camisa = "R$ 69,99")
calca1= Calca.create(cor_calca = "Azul" , tamanho_calca = "M" , marca_calca = "Knoten" , preco_calca = "R$89,99")
bermuda1= Bermuda.create(cor_bermuda = "Verde" , tamanho_bermuda = "P" , marca_bermuda = "BlackStar", preco_bermuda = "49,99")
meia1= Meia.create(cor_meia = "Vermelho" , tipo_meia = "Basebol" , preco_meia = "R$5,00")
sapato1= Sapato.create(nome_sapato = "Tênis Wave Prophecy 8 Masculino" , cor_sapato = "Preto" , marca_sapato = "Mizuno" , tamanho_sapato "38" , preco_sapato = "R$799,99"
cliente1= (nome_cliente = "Rafael" , telefone_cliente = "12 93456-7890" , cpf_cliente = "084.428.909-47" , conta_cliente = "Não")
funcionario1 = nome_funcionario = "Felipe" , telefone_funcionario = "47 99165-5700" , codigo_funcionario = "548642" , comissao_funcionario = "2,5 %")

print(funcionario1, cliente1, camisa1, calca1, bermuda1, meia1, sapato1)



