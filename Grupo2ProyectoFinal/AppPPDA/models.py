from django.db import models

# Create your models here.
MEDIDA_TIPO = [
    ('REGULACION','Regulación'),
    ('ECONOMICA','Fomento de actividades económicas'),
    ('GENERAL','Beneficios para impulsar acciones de interés general'),
    ('ESTUDIOS','Estudios'),
    ('EDUCACION','Educación y difusión'),
    ('PUBLICA','Política Pública'),
]
MEDIDA_FRECUENCIA = [
    ('UNICA','Única'),
    ('ANUAL','Anual'),
]

class Medida(models.Model):
    id_medida = models.AutoField(primary_key=True)
    planes_referencia = models.ManyToManyField('Plan', through='MedidaPlan')
    tipo = models.CharField(choices=MEDIDA_TIPO)
    nombre = models.CharField(unique=True, max_length=100)
    indicador = models.CharField(unique=True, max_length=100)
    formula = models.CharField(unique=True, max_length=100)
    frecuencia = models.CharField(choices=MEDIDA_FRECUENCIA)
    verificacion = models.CharField(unique=True, max_length=100)

class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)


class MedidaPlan(models.Model):
    id_medida = models.ForeignKey('Medida', models.DO_NOTHING, db_column='id_medida')
    id_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='id_plan')


class OrganismoSectorial(models.Model):
    id_organismo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)