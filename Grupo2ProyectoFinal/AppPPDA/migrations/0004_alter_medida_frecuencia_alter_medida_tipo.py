# Generated by Django 5.1.5 on 2025-01-29 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPPDA', '0003_remove_medida_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medida',
            name='frecuencia',
            field=models.CharField(choices=[('UNICA', 'Única'), ('ANUAL', 'Anual')]),
        ),
        migrations.AlterField(
            model_name='medida',
            name='tipo',
            field=models.CharField(choices=[('REGULACION', 'Regulación'), ('ECONOMICA', 'Fomento de actividades económicas'), ('GENERAL', 'Beneficios para impulsar acciones de interés general'), ('ESTUDIOS', 'Estudios'), ('EDUCACION', 'Educación y difusión'), ('PUBLICA', 'Política Pública')]),
        ),
    ]
