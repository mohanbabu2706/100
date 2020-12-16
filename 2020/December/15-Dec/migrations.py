

from django.db import migrations,models


class Migration(migrations.Migration):

    initial = True

    dependencies = []


    operations = [
        migrations.CreateModel(
            name = "Banner",
            fields = [
                (
                    "id",
                    models.Autofield(
                        auto_created = True,
                        primary_key = True,
                        serialize = False,
                        verbose_name = "ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text = "Text to display in the banner's buttton",
                        max_length = 1024,
                    ),
                ),
                (
                    "message",
                    models.CharField(
                        help_text = "Message to display in the banner",max_length = 2048
                    ),
                ),
                (
                    "link",
                    models.CharField(
                        help_text = "Link the button will go to",max_length = 1024
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default = False,help_text = "Make the banner active on the site"
                    ),
                ),
                (
                    "psf_pages_only",
                    models.BooleanField(
                        default = True,help_text = "Display the bannr on/psf pages only"
                    ),
                ),
            ],
        )
    ]
    
        
                
                        