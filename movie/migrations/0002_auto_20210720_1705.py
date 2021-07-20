# Generated by Django 3.2.5 on 2021-07-20 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='introducer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.user'),
        ),
        migrations.CreateModel(
            name='SepecialMovieWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_time', models.DateTimeField(auto_now_add=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='MovieTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.tag')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('prouser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.prouser')),
            ],
        ),
    ]
