from django.db import migrations,models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=32)),
            ],
            options = {
                'ordering': ['name']
            }
        ),
        migrations.CreateModel(
            name='SoftwareType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options = {
                'ordering': ['name']
            }
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('provider', models.ForeignKey(on_delete=models.deletion.CASCADE,to='SoftwareProvider')),
                ('type', models.ForeignKey(on_delete=models.deletion.CASCADE,to='SoftwareType')),
            ],
            options = {
                 'ordering': ['name']
            },
        ),
        migrations.CreateModel(
            name='Licences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('software', models.ForeignKey(on_delete=models.deletion.CASCADE,to='Software')),
            ],
            options = {
                'ordering': ['name']
            }
        ),
        # migrations.CreateModel(
        #     name='SoftwareSupport',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
        #         ('')
        #     ]
        # ),
        # migrations.CreateModel(
        #     name='HardwareSupport',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
        #         ('')
        #     ]
        # ),
    ]
