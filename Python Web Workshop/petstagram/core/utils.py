from pets.models import Pet


def mbytes_to_bytes(mb):
    return mb * 1024 * 1024


def get_pet_by_name_and_slug(pet_name, username):
    # TODO: Resolve when user is authenticated
    return Pet.objects.get(slug=pet_name)