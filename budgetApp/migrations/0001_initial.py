# Generated by Django 2.0.3 on 2018-08-10 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('amout', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('budget', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='poject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetApp.Project'),
        ),
        migrations.AddField(
            model_name='category',
            name='poject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetApp.Project'),
        ),
    ]
