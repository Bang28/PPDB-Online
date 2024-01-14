# Generated by Django 3.2.23 on 2024-01-14 13:21

from django.db import migrations, models
import django.db.models.deletion
import ppdb.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berkas',
            fields=[
                ('id_berkas', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('file_kk', models.FileField(help_text='File bisa berupa gambar atau pdf', max_length=255, upload_to=ppdb.models.Berkas.file_kk, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='Kartu Keluarga')),
                ('file_akta', models.FileField(help_text='File bisa berupa gambar atau pdf', max_length=255, upload_to=ppdb.models.Berkas.file_akta, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='Akta Kelahiran')),
                ('file_raport', models.FileField(help_text='File bisa berupa gambar atau pdf', max_length=255, upload_to=ppdb.models.Berkas.file_raport, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='Nilai Raport Terakhir')),
                ('file_skl', models.FileField(help_text='File bisa berupa gambar atau pdf', max_length=255, upload_to=ppdb.models.Berkas.file_skl, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='Surat Keterangan Lulus')),
                ('file_ijazah', models.FileField(blank=True, help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', max_length=255, null=True, upload_to=ppdb.models.Berkas.file_ijazah, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='Ijazah Jenjang Sebelumnya')),
                ('file_skhun', models.FileField(blank=True, help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', max_length=255, null=True, upload_to=ppdb.models.Berkas.file_skhun, validators=[ppdb.models.file_extension, ppdb.models.file_size], verbose_name='SKHUN')),
            ],
            options={
                'verbose_name_plural': 'Berkas Siswa',
            },
        ),
        migrations.CreateModel(
            name='OrangTua',
            fields=[
                ('id_ortu', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nama_ayah', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nama Lengkap Ayah')),
                ('status_ayah', models.CharField(blank=True, choices=[('', 'Status'), ('Masih Hidup', 'Masih Hidup'), ('Sudah Meninggal', 'Sudah Meninggal'), ('Tidak Diketahui', 'Tidak Diketahui')], max_length=30, null=True, verbose_name='Status Ayah')),
                ('nik_ayah', models.CharField(blank=True, max_length=16, null=True, verbose_name='NIK Ayah')),
                ('status_ibu', models.CharField(blank=True, choices=[('', 'Status'), ('Masih Hidup', 'Masih Hidup'), ('Sudah Meninggal', 'Sudah Meninggal'), ('Tidak Diketahui', 'Tidak Diketahui')], max_length=30, null=True, verbose_name='Status Ibu')),
                ('tempat_lahir_ayah', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tempat Lahir Ayah')),
                ('tgl_lahir_ayah', models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir Ayah')),
                ('pendidikan_ayah', models.CharField(blank=True, choices=[('', 'Pendidikan'), ('Tidak Sekolah', 'Tidak Sekolah'), ('sd', 'SD/Sederajad'), ('smp', 'SMP/Sederajad'), ('sma', 'SMA/Sederajad'), ('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('s1', 'D4/S1'), ('s2', 'S2'), ('s3', 'S3')], max_length=25, null=True, verbose_name='Pendidikan Ayah')),
                ('pekerjaan_ayah', models.CharField(blank=True, choices=[('', 'Pekerjaan'), ('Tidak Bekerja', 'Tidak Bekerja'), ('Pensiunan', 'Pensiunan'), ('PNS', 'PNS'), ('TNI/POLRI', 'TNI/POLRI'), ('Guru/Dosen', 'Guru/Dosen'), ('Pegawai Swasta', 'Pegawai Swasta'), ('wiraswasta', 'Wiraswasta'), ('Pengacara/Jaksa/Hakim/Notaris', 'Pengacara/Jaksa/Hakim/Notaris'), ('Seniman/Pelukis/Artis/Sejenis', 'Seniman/Pelukis/Artis/Sejenis'), ('Dokter/Bidan/Perawat', 'Dokter/Bidan/Perawat'), ('Pilot/Pramugara', 'Pilot/Pramugara'), ('Pedagang', 'Pedagang'), ('Petani/Peternak', 'Petani/Peternak'), ('Nelayan', 'Nelayan'), ('Buruh(Tani/Pabrik/Bangunan)', 'Buruh(Tani/Pabrik/Bangunan)'), ('Sopir/Masinis/Kondektur', 'Sopir/Masinis/Kondektur'), ('Politikus', 'Politikus'), ('lainnya', 'Lainnya')], max_length=50, null=True, verbose_name='Pekerjaan Ayah')),
                ('penghasilan_ayah', models.CharField(blank=True, choices=[('', 'Penghasilan'), ('>500k', 'Kurang dari 500.000'), ('500-1000k', '500.000-1.000.000'), ('1000-2000k', '1.000.000-2.000.000'), ('2000-3000k', '2.000.000-3.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('4000-5000k', '4.000.000-5.000.000'), ('>5000k', 'Lebih dari 5.000.000')], max_length=30, null=True, verbose_name='Penghasilan Ayah')),
                ('nama_ibu', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nama Lengkap Ibu')),
                ('nik_ibu', models.CharField(blank=True, max_length=16, null=True, verbose_name='NIK Ibu')),
                ('tempat_lahir_ibu', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tempat Lahir Ibu')),
                ('tgl_lahir_ibu', models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir Ibu')),
                ('pendidikan_ibu', models.CharField(blank=True, choices=[('', 'Pendidikan'), ('Tidak Sekolah', 'Tidak Sekolah'), ('sd', 'SD/Sederajad'), ('smp', 'SMP/Sederajad'), ('sma', 'SMA/Sederajad'), ('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('s1', 'D4/S1'), ('s2', 'S2'), ('s3', 'S3')], max_length=25, null=True, verbose_name='Pendidikan Ibu')),
                ('pekerjaan_ibu', models.CharField(blank=True, choices=[('', 'Pekerjaan'), ('Tidak Bekerja', 'Tidak Bekerja'), ('Pensiunan', 'Pensiunan'), ('PNS', 'PNS'), ('TNI/POLRI', 'TNI/POLRI'), ('Guru/Dosen', 'Guru/Dosen'), ('Pegawai Swasta', 'Pegawai Swasta'), ('wiraswasta', 'Wiraswasta'), ('Pengacara/Jaksa/Hakim/Notaris', 'Pengacara/Jaksa/Hakim/Notaris'), ('Seniman/Pelukis/Artis/Sejenis', 'Seniman/Pelukis/Artis/Sejenis'), ('Dokter/Bidan/Perawat', 'Dokter/Bidan/Perawat'), ('Pilot/Pramugara', 'Pilot/Pramugara'), ('Pedagang', 'Pedagang'), ('Petani/Peternak', 'Petani/Peternak'), ('Nelayan', 'Nelayan'), ('Buruh(Tani/Pabrik/Bangunan)', 'Buruh(Tani/Pabrik/Bangunan)'), ('Sopir/Masinis/Kondektur', 'Sopir/Masinis/Kondektur'), ('Politikus', 'Politikus'), ('lainnya', 'Lainnya')], max_length=30, null=True, verbose_name='Pekerjaan Ibu')),
                ('penghasilan_ibu', models.CharField(blank=True, choices=[('', 'Penghasilan'), ('>500k', 'Kurang dari 500.000'), ('500-1000k', '500.000-1.000.000'), ('1000-2000k', '1.000.000-2.000.000'), ('2000-3000k', '2.000.000-3.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('4000-5000k', '4.000.000-5.000.000'), ('>5000k', 'Lebih dari 5.000.000')], max_length=25, null=True, verbose_name='Penghasilan Ibu')),
                ('no_hp_ortu', models.CharField(blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.', max_length=13, null=True, verbose_name='No Telp/Wa')),
                ('status_tmp_tinggal_ortu', models.CharField(blank=True, choices=[('', 'Status tinggal'), ('Milik Sendiri', 'Milik Sendiri'), ('Rumah Orangtua', 'Rumah Orangtua'), ('Rumah Saudara/Kerabat', 'Rumah Saudara/Kerabat'), ('Rumah Dinas', 'Rumah Dinas'), ('Sewa/Kontrak', 'Sewa/Kontrak'), ('lainnya', 'Lainnya')], max_length=25, null=True, verbose_name='Status Tempat Tinggal Orang Tua')),
            ],
            options={
                'verbose_name_plural': 'Data Ayah Siswa',
            },
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id_siswa', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('no_pendaftaran', models.CharField(blank=True, editable=False, max_length=12, unique=True, verbose_name='No Pendaftaran')),
                ('status', models.CharField(choices=[('Siswa Baru', 'Siswa Baru'), ('Pindahan', 'Pindahan')], default=1, max_length=10, verbose_name='Status')),
                ('nama', models.CharField(max_length=55, verbose_name='Nama Lengkap')),
                ('nik', models.CharField(max_length=16, verbose_name='NIK')),
                ('tempat_lahir', models.CharField(max_length=30, verbose_name='Tempat Lahir')),
                ('tgl_lahir', models.DateField(verbose_name='Tanggal Lahir')),
                ('agama', models.CharField(choices=[('', 'Pilih agama'), ('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Hindu', 'Hindu'), ('Budha', 'Budha'), ('Kong Hu Cu', 'Kong Hu Cu')], max_length=10, verbose_name='Agama')),
                ('asal_sekolah', models.CharField(max_length=60, verbose_name='Asal Sekolah')),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], default='', max_length=15, verbose_name='Jenis Kelamin')),
                ('anak_ke', models.CharField(blank=True, max_length=2, null=True, verbose_name='Anak Ke')),
                ('saudara', models.CharField(blank=True, max_length=2, null=True, verbose_name='Jumlah Saudara')),
                ('no_hp', models.CharField(blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.', max_length=13, null=True, verbose_name='No Telp/Wa')),
                ('email', models.EmailField(help_text='Pastikan email aktif dan dapat dihubungi.', max_length=254, verbose_name='Email')),
                ('status_tinggal', models.CharField(choices=[('', 'Pilih status tinggal'), ('Tinggal dengan ORTU/WALI', 'Tinggal dengan ORTU/WALI'), ('Ikut Saudara/Kerabat', 'Ikut Saudara/Kerabat'), ('Asrama', 'Asrama'), ('Kontrak/Kost', 'Kontrak/Kost'), ('Panti Asuhan', 'Panti Asuhan'), ('lainnya', 'Lainnya')], max_length=50, verbose_name='Status Tinggal')),
                ('alamat', models.TextField(verbose_name='Alamat')),
                ('kodepos', models.CharField(blank=True, max_length=6, null=True, verbose_name='Kode POS')),
                ('transportasi', models.CharField(blank=True, choices=[('', 'Pilih transportasi'), ('Jalan Kaki', 'Jalan Kaki'), ('Sepeda', 'Sepeda'), ('Sepeda Motor', 'Sepeda Motor'), ('Mobil Pribadi', 'Mobil Pribadi'), ('Angkutan Umum', 'Angkutan Umum'), ('lainnya', 'Lainnya')], max_length=30, null=True, verbose_name='Mode Transportasi')),
                ('biaya_sekolah', models.CharField(choices=[('', 'Biaya sekolah'), ('Orangtua', 'Orangtua'), ('Wali/Orangtua Asuh', 'Wali/Orangtua Asuh'), ('Tanggung Sendiri', 'Tanggung Sendiri'), ('Lainnya', 'Lainnya')], max_length=30, verbose_name='Biaya Sekolah')),
                ('keb_disabilitas', models.CharField(choices=[('', 'Kebutuhan disabilitas'), ('Tidak Ada', 'Tidak Ada'), ('Tuna Netra', 'Tuna Netra'), ('Tuna Rungu', 'Tuna Rungu'), ('Tuna Daksa', 'Tuna Daksa'), ('Tuna Grahita', 'Tuna Grahita'), ('Tuna Laras', 'Tuna Laras'), ('Lainnya', 'Lainnya')], max_length=20, verbose_name='Kebutuhan Disabilitas')),
                ('foto', models.ImageField(help_text='foto 3x4 dengan background merah', max_length=255, upload_to=ppdb.models.Siswa.image_upload_to, verbose_name='Foto')),
                ('verifikasi', models.CharField(choices=[('Pending', 'Pending'), ('Diterima', 'Diterima'), ('Ditolak', 'Ditolak')], default='Pending', max_length=10, null=True, verbose_name='Status Pendaftaran')),
                ('tgl_daftar', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tanggal Daftar')),
            ],
            options={
                'verbose_name_plural': 'Peserta PPDB',
            },
        ),
        migrations.CreateModel(
            name='TahunAjaran',
            fields=[
                ('id_thn_ajaran', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('tahun_ajaran', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('', 'Status PPDB'), ('Dibuka', 'Dibuka'), ('Ditutup', 'Ditutup')], max_length=10)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Tahun Ajaran',
            },
        ),
        migrations.CreateModel(
            name='Wali',
            fields=[
                ('id_wali', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nama_wali', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nama Wali')),
                ('nik_wali', models.CharField(blank=True, max_length=16, null=True, verbose_name='NIK Wali')),
                ('tempat_lahir_wali', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tempat Lahir Wali')),
                ('tgl_lahir_wali', models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir Wali')),
                ('pendidikan_wali', models.CharField(blank=True, choices=[('', 'Pendidikan'), ('Tidak Sekolah', 'Tidak Sekolah'), ('sd', 'SD/Sederajad'), ('smp', 'SMP/Sederajad'), ('sma', 'SMA/Sederajad'), ('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('s1', 'D4/S1'), ('s2', 'S2'), ('s3', 'S3')], max_length=25, null=True, verbose_name='Pendidikan Wali')),
                ('pekerjaan_wali', models.CharField(blank=True, choices=[('', 'Pekerjaan'), ('Tidak Bekerja', 'Tidak Bekerja'), ('Pensiunan', 'Pensiunan'), ('PNS', 'PNS'), ('TNI/POLRI', 'TNI/POLRI'), ('Guru/Dosen', 'Guru/Dosen'), ('Pegawai Swasta', 'Pegawai Swasta'), ('wiraswasta', 'Wiraswasta'), ('Pengacara/Jaksa/Hakim/Notaris', 'Pengacara/Jaksa/Hakim/Notaris'), ('Seniman/Pelukis/Artis/Sejenis', 'Seniman/Pelukis/Artis/Sejenis'), ('Dokter/Bidan/Perawat', 'Dokter/Bidan/Perawat'), ('Pilot/Pramugara', 'Pilot/Pramugara'), ('Pedagang', 'Pedagang'), ('Petani/Peternak', 'Petani/Peternak'), ('Nelayan', 'Nelayan'), ('Buruh(Tani/Pabrik/Bangunan)', 'Buruh(Tani/Pabrik/Bangunan)'), ('Sopir/Masinis/Kondektur', 'Sopir/Masinis/Kondektur'), ('Politikus', 'Politikus'), ('lainnya', 'Lainnya')], max_length=30, null=True, verbose_name='Pekerjaan Wali')),
                ('penghasilan_wali', models.CharField(blank=True, choices=[('', 'Penghasilan'), ('>500k', 'Kurang dari 500.000'), ('500-1000k', '500.000-1.000.000'), ('1000-2000k', '1.000.000-2.000.000'), ('2000-3000k', '2.000.000-3.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('3000-4000k', '3.000.000-4.000.000'), ('4000-5000k', '4.000.000-5.000.000'), ('>5000k', 'Lebih dari 5.000.000')], max_length=25, null=True, verbose_name='Penghasilan Wali')),
                ('no_hp_wali', models.CharField(blank=True, max_length=15, null=True, verbose_name='No Telp/Wa Wali')),
                ('siswa', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wali', to='ppdb.siswa')),
            ],
            options={
                'verbose_name_plural': 'Data Wali Siswa',
            },
        ),
    ]
