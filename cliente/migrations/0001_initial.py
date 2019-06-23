# Generated by Django 2.2.2 on 2019-06-19 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(default='', max_length=100)),
                ('rg_cliente', models.CharField(default='0000000', max_length=7)),
                ('endereco_cliente', models.CharField(default='', max_length=50)),
                ('telefone_cliente', models.CharField(default='00000000', max_length=11)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Erros',
            fields=[
                ('id_erro', models.AutoField(primary_key=True, serialize=False)),
                ('nome_relato', models.CharField(max_length=50)),
                ('descricao_erro', models.TextField()),
            ],
            options={
                'verbose_name': 'Erro',
                'verbose_name_plural': 'Erros',
            },
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.CharField(default='', max_length=100)),
                ('rg_funcionario', models.CharField(default='0000000', max_length=7)),
                ('endereco_funcionario', models.CharField(default='', max_length=50)),
                ('telefone_funcionario', models.CharField(default='00000000000', max_length=11)),
                ('data_admissao', models.DateTimeField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(default='', max_length=100)),
                ('quantidade_produto', models.IntegerField()),
                ('valor_produto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('observacao', models.TextField(blank=True, default='-', null=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id_venda', models.AutoField(primary_key=True, serialize=False)),
                ('nome_venda', models.CharField(default='', max_length=100)),
                ('quantidade_venda', models.IntegerField(default=10)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Clientes')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Funcionarios')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Produtos')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]