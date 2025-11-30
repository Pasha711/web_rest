from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код категорії")
    name = models.CharField(max_length=255, verbose_name="Назва категорії")
    description = models.TextField(blank=True, null=True, verbose_name="Опис категорії")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код виробника")
    name = models.CharField(max_length=255, verbose_name="Назва виробника")
    description = models.TextField(blank=True, null=True, verbose_name="Опис виробника")

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код продукта")
    name = models.CharField(max_length=255, verbose_name="Назва продукта")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='products')
    short_descr = models.CharField(max_length=255, verbose_name="Короткий опис")
    description = models.TextField(blank=True, null=True, verbose_name="Повний опис")


    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    number = models.CharField(max_length=100, unique=True, verbose_name="Номер заказу")
    odate = models.DateField(auto_now_add=True, verbose_name="Дата заказу")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return f"Заказ №{self.number} від {self.odate}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    pdate = models.DateField(verbose_name="Дата встановлення ціни")
    pprice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    qtty = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="Кількість продуктів у наявності")

    def __str__(self):
        return f"Ціна на {self.product.name} від {self.pdate}: {self.pprice}"