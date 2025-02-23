# Generated by Django 5.1.2 on 2025-02-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asi', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_asi', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_asi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('atraso_asi', models.CharField(max_length=25)),
                ('valor_atraso_asi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creacion_asi', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_asi', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'asistencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id_com', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_com', models.DateField()),
                ('mensaje_com', models.CharField(max_length=200)),
                ('actualizacion_com', models.DateTimeField(blank=True, null=True)),
                ('creacion_com', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comunicado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id_con', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_con', models.CharField(max_length=250)),
                ('ruc_con', models.CharField(max_length=13)),
                ('logo_con', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono_con', models.CharField(max_length=50)),
                ('direccion_con', models.CharField(max_length=50)),
                ('email_con', models.CharField(max_length=50)),
                ('servidor_con', models.CharField(max_length=50)),
                ('puerto_con', models.CharField(max_length=50)),
                ('password_con', models.CharField(max_length=50)),
                ('creacion_con', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_con', models.DateTimeField(blank=True, null=True)),
                ('anio_inicial_con', models.CharField(blank=True, max_length=15, null=True)),
                ('mes_inicial_con', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'configuracion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id_consumo', models.AutoField(primary_key=True, serialize=False)),
                ('anio_consumo', models.IntegerField(blank=True, null=True)),
                ('mes_consumo', models.CharField(blank=True, max_length=25, null=True)),
                ('estado_consumo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion_consumo', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_consumo', models.DateTimeField(blank=True, null=True)),
                ('numero_mes_consumo', models.IntegerField(blank=True, null=True)),
                ('fecha_vencimiento_consumo', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'consumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_det', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_det', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('detalle_det', models.CharField(blank=True, max_length=1500, null=True)),
                ('valor_unitario_det', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('subtotal_det', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('iva_det', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_eve', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_eve', models.TextField(blank=True, null=True)),
                ('fecha_hora_eve', models.DateTimeField(blank=True, null=True)),
                ('lugar_eve', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Excedente',
            fields=[
                ('id_ex', models.AutoField(primary_key=True, serialize=False)),
                ('limite_minimo_ex', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('limite_maximo_ex', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tarifa_ex', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_actualizacion_ex', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion_ex', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'excedente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialPropietario',
            fields=[
                ('id_his', models.AutoField(primary_key=True, serialize=False)),
                ('actualizacion_his', models.DateTimeField(blank=True, null=True)),
                ('estado_his', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion_his', models.TextField(blank=True, null=True)),
                ('fecha_cambio_his', models.DateTimeField(blank=True, null=True)),
                ('creacion_his', models.DateTimeField(blank=True, null=True)),
                ('propietario_actual_his', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'historial_propietario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id_imp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_imp', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_imp', models.TextField(blank=True, null=True)),
                ('porcentaje_imp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('retencion_imp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado_imp', models.CharField(blank=True, max_length=50, null=True)),
                ('creacion_imp', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_imp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'impuesto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id_lec', models.AutoField(primary_key=True, serialize=False)),
                ('anio_lec', models.IntegerField(blank=True, null=True)),
                ('mes_lec', models.CharField(blank=True, max_length=25, null=True)),
                ('estado_lec', models.CharField(blank=True, max_length=50, null=True)),
                ('lectura_anterior_lec', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lectura_actual_lec', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_creacion_lec', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_lec', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lectura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medidor',
            fields=[
                ('id_med', models.AutoField(primary_key=True, serialize=False)),
                ('numero_med', models.CharField(blank=True, max_length=50, null=True)),
                ('serie_med', models.CharField(blank=True, max_length=100, null=True)),
                ('marca_med', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion_med', models.TextField(blank=True, null=True)),
                ('estado_med', models.CharField(blank=True, max_length=25, null=True)),
                ('foto_med', models.CharField(blank=True, max_length=500, null=True)),
                ('creacion_med', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_med', models.DateTimeField(blank=True, null=True)),
                ('lectura_inicial_med', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'medidor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_per', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_per', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion_per', models.TextField(blank=True, null=True)),
                ('estado_per', models.CharField(blank=True, max_length=25, null=True)),
                ('creacion_per', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_per', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recaudacion',
            fields=[
                ('id_rec', models.AutoField(primary_key=True, serialize=False)),
                ('numero_factura_rec', models.CharField(blank=True, max_length=250, null=True)),
                ('numero_autorizacion_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_hora_autorizacion_rec', models.DateTimeField(blank=True, null=True)),
                ('ambiente_rec', models.CharField(blank=True, max_length=50, null=True)),
                ('emision_rev', models.CharField(blank=True, max_length=50, null=True)),
                ('clave_acceso_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('email_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('observacion_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('nombre_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('identificacion_rec', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion_rec', models.CharField(blank=True, max_length=500, null=True)),
                ('estado_rec', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_emision_rec', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion_rec', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_rec', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recaudacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id_rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rut', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion_rut', models.TextField(blank=True, null=True)),
                ('estado_rut', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'ruta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id_soc', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_soc', models.CharField(blank=True, max_length=25, null=True)),
                ('identificacion_soc', models.CharField(blank=True, max_length=13, null=True)),
                ('primer_apellido_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('segundo_apellido_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('nombres_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('email_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('foto_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('telefono_soc', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion_soc', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_nacimiento_soc', models.DateField(blank=True, null=True)),
                ('discapacidad_soc', models.CharField(blank=True, max_length=25, null=True)),
                ('estado_soc', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'socio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id_tar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tar', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion_tar', models.TextField(blank=True, null=True)),
                ('estado_tar', models.CharField(blank=True, max_length=25, null=True)),
                ('m3_maximo_tar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tarifa_basica_tar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tarifa_excedente_tar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_mora_tar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'tarifa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id_te', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_te', models.CharField(blank=True, max_length=150, null=True)),
                ('estado_te', models.CharField(blank=True, max_length=50, null=True)),
                ('creacion_te', models.DateTimeField(blank=True, null=True)),
                ('actualizacion_te', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usu', models.AutoField(primary_key=True, serialize=False)),
                ('apellido_usu', models.CharField(blank=True, max_length=150, null=True)),
                ('nombre_usu', models.CharField(blank=True, max_length=150, null=True)),
                ('email_usu', models.CharField(blank=True, max_length=150, null=True)),
                ('password_usu', models.CharField(blank=True, max_length=500, null=True)),
                ('estado_usu', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
