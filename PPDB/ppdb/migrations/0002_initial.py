# Generated by Django 3.2.23 on 2024-03-17 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ppdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peserta',
            name='nisn',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siswa', to=settings.AUTH_USER_MODEL, verbose_name='NISN'),
        ),
        migrations.AddField(
            model_name='peserta',
            name='thn_ajaran',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ppdb.tahunajaran', verbose_name='Tahun Ajaran'),
        ),
        migrations.AddField(
            model_name='nilairaport',
            name='peserta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='raport', to='ppdb.peserta'),
        ),
        migrations.AddField(
            model_name='berkas',
            name='peserta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='berkas', to='ppdb.peserta'),
        ),
    ]
