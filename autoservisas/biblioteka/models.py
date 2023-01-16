from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Paslauga(models.Model):
    pavadinimas = models.CharField('Paslauga', max_length=200, help_text='Įveskite paslaugą.')
    kaina = models.FloatField('Kaina', max_length=10, help_text='Įveskite paslaugos kainą.')

    def __str__(self):
        return f'{self.pavadinimas}, {self.kaina}'


class Automobilis(models.Model):
    valstybinis_nr = models.CharField("Valstybinis_NR", max_length=6)
    automobilis_id = models.ForeignKey("AutomobilisModelis", on_delete=models.SET_NULL, null=True)
    vin_kodas = models.TextField('VIN_kodas', max_length=17, help_text='Įveskite automobilio VIN kodą.')
    klientas = models.TextField('Klientas', max_length=25, help_text='Įveskite automobilio savininką.')

    # uzsakymo_eilute = models.ManyToManyField(Paslauga, help_text='Išrinkite užsakymą/us.')

    def __str__(self):
        return f"{self.klientas}, {self.automobilis_id}"

    # def get_absolute_url(self):
    #     return reverse('book-detail', args=[str(self.id)])


class Uzsakymas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus užsakymo ID')
    automobilis = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    atsiemimo_data = models.DateField('Atsiėmimo data', null=False, blank=False)
    suma = models.FloatField('Suma', max_length=10, help_text='Įveskite bendrą paslaugų sumą.')

    class Meta:
        ordering = ['atsiemimo_data']

    def __str__(self):
        return f'{self.id} {self.automobilis}'


class AutomobilisModelis(models.Model):
    metai = models.CharField('Metai', max_length=20)
    marke = models.CharField('Markė', max_length=20)
    modelis = models.CharField('Modelis', max_length=20)
    variklis = models.CharField('Variklis', max_length=20)

    # class Meta:
    #     ordering = ['marke', 'modelis']
    class Meta:
        verbose_name = "Modelis"
        verbose_name_plural = "Modeliai"

    # def get_absolute_url(self):
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.marke}, {self.modelis}'


class UzsakymoEilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField('Kiekis', help_text='Įveskite paslaugų kiekį.')
    kaina = models.CharField('Kaina', max_length=200, help_text='Įveskite paslaugų kainą.')

    LOAN_STATUS = (
        ("a", "Administruojama"),
        ("t", "tvarkoma"),
        ("b", "baigta"),
        ("p", "pasiimti"),
        ("d", "atiduota")
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="a",
        help_text="Status"
    )

    def __str__(self):
        return f'{self.paslauga_id} - {self.kiekis}: {self.kaina}'
