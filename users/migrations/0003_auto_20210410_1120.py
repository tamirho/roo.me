# Generated by Django 3.1.7 on 2021-04-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_auto_20210405_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. A user will get all permissions granted to each of\
                their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.ManyToManyField(to='users.Hobby'),
        ),
    ]