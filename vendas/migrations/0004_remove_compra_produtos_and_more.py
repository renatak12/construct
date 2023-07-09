# Generated by Django 4.2.1 on 2023-06-09 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_compra_itemcompra_compra_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='produtos',
        ),
        migrations.RemoveField(
            model_name='itemcompra',
            name='preco_unitario',
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itenscompra', to='vendas.compra'),
        ),
    ]
