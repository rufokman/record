# Generated by Django 4.1.2 on 2022-10-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edit', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'config',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='card',
            name='fio',
            field=models.CharField(max_length=300, verbose_name='ФИО сотрудника'),
        ),
        migrations.AlterField(
            model_name='card',
            name='organization',
            field=models.CharField(choices=[(None, 'Выберите организацию'), ('ЦА', 'ЦА'), ('Балаковская АЭС', 'Балаковская АЭС'), ('Белоярская АЭС', 'Белоярская АЭС'), ('Билибинская АЭС', 'Билибинская АЭС'), ('Калининская АЭС', 'Калининская АЭС'), ('Кольская АЭС', 'Кольская АЭС'), ('Курская АЭС', 'Курская АЭС'), ('Ленинградская АЭС', 'Ленинградская АЭС'), ('Нововоронежская АЭС', 'Нововоронежская АЭС'), ('Ростовская АЭС', 'Ростовская АЭС'), ('Смоленская АЭС', 'Смоленская АЭС'), ('ПАТЭС', 'ПАТЭС'), ('Технологический филиал', 'Технологический филиал'), ('ОДИЦ ВВЭР', 'ОДИЦ ВВЭР'), ('ОДИЦ РБМК', 'ОДИЦ РБМК'), ('Строящаяся Балтийская АЭС', 'Строящаяся Балтийская АЭС'), ('ИЦ Аккую', 'ИЦ Аккую'), ('Воронежская АСТ', 'Воронежская АСТ'), ('Филиал в Бангладеш', 'Филиал в Бангладеш'), ('Атомтехэнерго', 'Атомтехэнерго'), ('АтомЭнергоСбыт', 'АтомЭнергоСбыт'), ('АтомЭнергоРемонт', 'АтомЭнергоРемонт'), ('ЗАЭС', 'ЗАЭС'), ('АтомТеплоЭлектроСеть', 'АтомТеплоЭлектроСеть'), ('Техническая Академия', 'Техническая Академия'), ('ИКАО', 'ИКАО'), ('НИЦ АЭС', 'НИЦ АЭС'), ('ЭНИЦ', 'ЭНИЦ'), ('Энергоатоминвест', 'Энергоатоминвест'), ('Балтийская АЭС, АО', 'Балтийская АЭС, АО'), ('Атомтранс', 'Атомтранс'), ('Атомтеплосбыт', 'Атомтеплосбыт'), ('ВНИИАЭС', 'ВНИИАЭС'), ('Титан - 2', 'Титан - 2'), ('Консист - ОС', 'Консист - ОС'), ('С - Плюс', 'С - Плюс'), ('Неорганические сорбенты', 'Неорганические сорбенты'), ('АТОМДАТА', 'АТОМДАТА'), ('Атомдата - Центр', 'Атомдата - Центр'), ('Атомдата - Иннополис', 'Атомдата - Иннополис')], max_length=300, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='card',
            name='role',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
    ]
