from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd, customer = self.get_info(customer_id, dvd_id)
        rented_by_customer = dvd in customer.rented_dvds
        if rented_by_customer:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd, customer = self.get_info(customer_id, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD" 
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def get_info(self, customer_id, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        return dvd, customer

    def __repr__(self):
        customers = '\n'.join([repr(x) for x in self.customers])
        dvds = '\n'.join([repr(x) for x in self.dvds])
        return f'{customers}\n{dvds}'