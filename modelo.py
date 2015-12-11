import banco
from peewee import *

class ModeloBase(Model):
    class Meta:
        database = banco.db

class Curso(ModeloBase):
    aulas_por_dia = IntegerField()
    dias_por_semana = IntegerField()

class Disciplina(ModeloBase):
    nome = CharField(unique=True)
    sigla = CharField(unique=True)
    periodo = IntegerField()
    curso = ForeignKeyField(Curso, related_name='Disciplina')
    ativa = BooleanField()

class Horario(ModeloBase):
    disciplina_id = ForeignKeyField(Disciplina, related_name='Disciplina')
    aulas = IntegerField()
    
