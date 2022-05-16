# Generated by Django 4.0.4 on 2022-05-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positioning_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='name',
            field=models.CharField(default='noname-institution', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='tutors',
            field=models.ManyToManyField(related_name='institutions', to='positioning_app.tutor'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='address',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='TutorInstitution',
        ),
    ]