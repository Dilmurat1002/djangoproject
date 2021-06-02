# Generated by Django 3.2.4 on 2021-06-02 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(max_length=50)),
                ('end_date', models.DateTimeField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(max_length=50)),
                ('start_date', models.DateTimeField(max_length=50)),
                ('end_date', models.DateTimeField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ManyToManyField(to='polls.Project'),
        ),
    ]