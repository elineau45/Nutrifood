from django.db import models


class Cat_principal(models.Model):
    name_cat = models.CharField(max_length=200)

    def __str__(self):
        return self.name_cat


class Produit(models.Model):
    nom_P = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat_principal, on_delete=models.CASCADE)
    # a mettre en dessous, car utilise la class Cat_principal

    # code_P = models.CharField(max_length=200)
    # cat_P = models.CharField(max_length=200)
    # photo_P = models.ImageField()

    def __str__(self):
        return self.nom_P


# class Propriete(models.Model):
#     id_code_P = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     nutriscore = models.CharField(max_length=200)


# class Client(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nom_C = models.CharField(max_length=200)
#     prenom_C = models.CharField(max_length=200)
#     mail_C = models.CharField(max_length=200)


# class FavoriClient(models.Model):
#     id_client = models.IntegerField()
#     produit_rech = models.CharField(max_length=200)
#     produit_trouv = models.CharField(max_length=200)
