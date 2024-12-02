class Helper:

    @staticmethod
    def check_for_duplicated_delicacy(name: str, d_list: list):
        if name in [x.name for x in d_list]:
            raise Exception(f"{name} already exists!")

    @staticmethod
    def check_valid_type_of_delicacy(delicacy_type: str, delicacy_types: dict):
        if delicacy_type not in delicacy_types:
            raise Exception(f"{delicacy_type} is not on our delicacy menu!")

    @staticmethod
    def check_for_duplicated_booth_number(booth_number: int, booth_list: list):
        if booth_number in [x.booth_number for x in booth_list]:
            raise Exception(f"Booth number {booth_number} already exists!")

    @staticmethod
    def check_valid_booth_type(booth_type: str, valid_booth_types: dict):
        if booth_type not in valid_booth_types:
            raise Exception(f"{booth_type} is not a valid booth!")

    @staticmethod
    def find_free_booth(number_of_people: int, booth_list: list):
        booth = [x for x in booth_list if not x.is_reserved and x.capacity >= number_of_people]
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        return booth[0]

    @staticmethod
    def find_booth_by_number(booth_number: int, booth_list: list):
        booth = [x for x in booth_list if x.booth_number == booth_number]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        return booth[0]

    @staticmethod
    def find_delicacy_by_name(delicacy_name: str, delicacy_list: list):
        delicacy = [x for x in delicacy_list if x.name == delicacy_name]
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        return delicacy[0]
