# Generated by Django 4.2.3 on 2023-07-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_alter_produto_descricao_alter_produto_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='media/imagens'),
        ),
    ]