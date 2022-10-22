from django.db import models
from users.models import CustomUser


class Config(models.Model):
    allow_edit = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'config'


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=[(0, 'agreed'),
                                                  (1, 'onchecking'),
                                                  (2, 'rejected'),
                                                  (3, 'default')], default=3)
    organization_list = [
        (None, "Выберите организацию"),
        ("ЦА", "ЦА"),
        ('Балаковская АЭС', 'Балаковская АЭС'),
        ('Белоярская АЭС', 'Белоярская АЭС'),
        ('Билибинская АЭС', 'Билибинская АЭС'),
        ('Калининская АЭС', 'Калининская АЭС'),
        ('Кольская АЭС', 'Кольская АЭС'),
        ('Курская АЭС', 'Курская АЭС'),
        ('Ленинградская АЭС', 'Ленинградская АЭС'),
        ('Нововоронежская АЭС', 'Нововоронежская АЭС'),
        ('Ростовская АЭС', 'Ростовская АЭС'),
        ('Смоленская АЭС', 'Смоленская АЭС'),
        ('ПАТЭС', 'ПАТЭС'),
        ('Технологический филиал', 'Технологический филиал'),
        ('ОДИЦ ВВЭР', 'ОДИЦ ВВЭР'),
        ('ОДИЦ РБМК', 'ОДИЦ РБМК'),
        ('Строящаяся Балтийская АЭС', 'Строящаяся Балтийская АЭС'),
        ('ИЦ Аккую', 'ИЦ Аккую'),
        ('Воронежская АСТ', 'Воронежская АСТ'),
        ('Филиал в Бангладеш', 'Филиал в Бангладеш'),
        ('Атомтехэнерго', 'Атомтехэнерго'),
        ('АтомЭнергоСбыт', 'АтомЭнергоСбыт'),
        ('АтомЭнергоРемонт', 'АтомЭнергоРемонт'),
        ('ЗАЭС', 'ЗАЭС'),
        ('АтомТеплоЭлектроСеть', 'АтомТеплоЭлектроСеть'),
        ('Техническая Академия', 'Техническая Академия'),
        ('ИКАО', 'ИКАО'),
        ('НИЦ АЭС', 'НИЦ АЭС'),
        ('ЭНИЦ', 'ЭНИЦ'),
        ('Энергоатоминвест', 'Энергоатоминвест'),
        ('Балтийская АЭС, АО', 'Балтийская АЭС, АО'),
        ('Атомтранс', 'Атомтранс'),
        ('Атомтеплосбыт', 'Атомтеплосбыт'),
        ('ВНИИАЭС', 'ВНИИАЭС'),
        ('Титан - 2', 'Титан - 2'),
        ('Консист - ОС', 'Консист - ОС'),
        ('С - Плюс', 'С - Плюс'),
        ('Неорганические сорбенты', 'Неорганические сорбенты'),
        ( 'АТОМДАТА', 'АТОМДАТА'),
        ('Атомдата - Центр', 'Атомдата - Центр'),
        ('Атомдата - Иннополис', 'Атомдата - Иннополис')]
    send = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.CharField(choices=organization_list, verbose_name="Организация", max_length=300)
    function = models.PositiveIntegerField(choices=[
        (None, 'Выберите функцию'),
        (0, "Экономика и финансы"),
        (1, "Сооружение"),
        (2, "Международные и новые бизнесы"),
        (3, "Производство"),
        (4, "Инвестиционная деятельность"),
        (5, "Управление персоналом"),
        (6, "Управление качеством"),
        (7, "Генеральная инспекция"),
        (8, "ФАИП и ГОЗ / КВЛ"),
        (9, "Сбыт"),
        (10, "Корпоративное управление, Правовое обеспечение, Управление имуществом, Непрофильные активы"),
        (11, "Инновационная деятельность"),
        (12, "Безопасность"),
        (13, "Административное управление"),
        (14, "Закупки и МТО"),
        (15, "Внутренний контроль и аудит"),
        (16, "Бухгалтерия")], verbose_name='Функция')
    role = models.CharField(max_length=100, verbose_name="Должность")
    fio = models.CharField(max_length=300, verbose_name="ФИО сотрудника")
    name = models.CharField(max_length=3000, verbose_name='Наименование КПЭ')
    method = models.PositiveIntegerField(choices=[
        (None, 'Выберите методику расчета КПЭ'),
        (0, "Дискретный"),
        (1, "Непрерывный"),
        (2, "Отсекающий"),
        (3, "Понижающий")], verbose_name='Методика расчета')
    low_level = models.CharField(max_length=3000, verbose_name='Нижний уровень')
    target_level = models.CharField(max_length=3000, verbose_name='Целевой уровень')
    high_level = models.CharField(max_length=3000, verbose_name="Верхний уровень")
    weight = models.IntegerField(verbose_name='Вес')
    passport = models.FileField(upload_to='passports/', verbose_name="Паспорт", default="", null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'card'
