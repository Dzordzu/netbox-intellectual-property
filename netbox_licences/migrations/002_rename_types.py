
from django.db import migrations,models

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_licences', '001_base_initial')
    ]

    operations = [
        migrations.RenameField('Software', 'softtype', 'software_type'),
        migrations.RenameField('Licence', 'licencetype', 'licence_type')
    ]

