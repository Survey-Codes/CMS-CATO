# Generated by Django 2.2.3 on 2021-03-28 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20210328_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='page_url',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='updated_by',
        ),
        migrations.AlterUniqueTogether(
            name='menuitemlanguage',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='menuitemlanguage',
            name='language',
        ),
        migrations.RemoveField(
            model_name='menuitemlanguage',
            name='menu_item',
        ),
        migrations.AlterUniqueTogether(
            name='menulanguage',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='menulanguage',
            name='language',
        ),
        migrations.RemoveField(
            model_name='menulanguage',
            name='menu',
        ),
        migrations.AlterField(
            model_name='page',
            name='inner_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menus.Menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='section',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.SectionTemplate', verbose_name='Section template'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='MenuItemLanguage',
        ),
        migrations.DeleteModel(
            name='MenuLanguage',
        ),
    ]
