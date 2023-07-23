from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Zhiting",
                          email="zhitinglu@outlook.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="664829900",
                          gender="Female")

        user.set_password("Meow1234")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]