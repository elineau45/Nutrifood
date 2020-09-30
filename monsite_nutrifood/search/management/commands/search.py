from django.core.management.base import BaseCommand, CommandError
from search.models import Cat_principal, Produit
import requests


class Command(BaseCommand):
    def __init__(self):
        self.choix_Cat = [
            "Snacks",
            "Boissons",
        ]

        #
        # "Plats préparés",
        # "Biscuits et gâteaux",
        # "Petit-déjeuners",

    def recup_api(self):
        for cat in self.choix_Cat:
            print("\ndébut de la catégorie : ", cat)
            cat_update = Cat_principal.objects.get_or_create(name_cat=cat)
            cat_update[0].save()

            params_get = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "page_size": "10",
                "json": "1",
                "tag_0": cat,
            }

            data_raw = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl", params=params_get
            ).json()

            for product in data_raw["products"]:
                try:
                    print(product["product_name_fr"])

                    name = product["product_name_fr"]
                    produit = Produit.objects.update_or_create(
                        nom_P=name, cat=cat_update[0]
                    )
                    produit[0].save()

                except KeyError:
                    pass

            print("fin de la catégorie : ", cat)

    def handle(self, *args, **options):
        self.recup_api()
        print("\nmise à jour terminée")
