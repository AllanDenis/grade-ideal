import banco
from peewee import *

class ModeloBase(Model):
    class Meta:
        database = banco.db

class Curso(ModeloBase):
    aulas_por_dia = IntegerField()
    dias_por_semana = IntegerField()

class disciplinas(ModeloBase):
    nome = CharField(unique=True)
    sigla = CharField(unique=True)
    periodo = IntegerField()
    cursos = ForeignKeyField(Curso, related_name='disciplinas')
    ativa = BooleanField()

class Horario(ModeloBase):
    disciplina_id = ForeignKeyField(disciplinas, related_name='disciplinas')
    aulas = IntegerField()
