# Generated by Django 3.1.2 on 2020-10-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    """ operations = [
        migrations.RenameModel(
            old_name='Keys',
            new_name='Words',
        ),
        migrations.RenameField(
            model_name='words',
            old_name='keys',
            new_name='words',
        ),
        migrations.RenameField(
            model_name='words',
            old_name='keys_date',
            new_name='words_date',
        ),
    ] """

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=50)),
                ('words_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'db_table': 'Words',

            },
        ),
    ]