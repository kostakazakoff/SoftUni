# Person
You are asked to model an application for storing data about people. You should be able to have a Person and a Child. Every person receives name and age upon initialization. Your task is to model the application.
Create a Child class that inherits Person and has the same constructor definition. However, do not copy the code from the Person class - reuse the Person class's constructor.
Submit in judge a zip file named project, containing a separate file (person.py and child.py) for each of the classes.


# Zoo
Create a zoo project that contains the following classes: 

![image](https://user-images.githubusercontent.com/104040753/199492972-9163efff-9174-4981-b51a-3a05a538dcda.png)

Submit in judge a zip file of the project, containing a separate file for each of the classes using the structure shown below:

![image](https://user-images.githubusercontent.com/104040753/199493018-37067f69-62c8-4b8f-bc4d-9c65fe52f732.png)

Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
Every class should have a constructor, which accepts one parameter: name


# Players and Monsters
Your task is to create the following game hierarchy: 

![image](https://user-images.githubusercontent.com/104040753/199504384-991550ae-2942-4cc8-92cc-36d0a1e182fb.png)

Submit in judge a zip file containing a separate file for each of the classes using the structure shown below:

![image](https://user-images.githubusercontent.com/104040753/199504411-74e2291c-c509-46b0-a19e-9d35e319eb7a.png)

Create a class Hero. It should contain the following attributes:
- username: string
- level: int

Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"


# Need for Speed
Create the following hierarchy with the following classes: 

![image](https://user-images.githubusercontent.com/104040753/199505236-58e980a6-1b61-4e45-84e2-7e0f58d42240.png)

Submit in judge a zip file containing a separate file for each of the classes using the structure shown below:

![image](https://user-images.githubusercontent.com/104040753/199505282-9cc56c3d-7a03-422d-87f8-5263d66eae59.png)

Create a base class Vehicle. It should contain the following attributes:
- DEFAULT_FUEL_CONSUMPTION: float (constant)
- fuel_consumption: float - represents the fuel consumption per kilometer
- fuel: float - represents the quantity of fuel in a specific vehicle
- horse_power: int

Upon initialization, the class should receive fuel and horse_power. The DEFAULT_FUEL_CONSUMPTION value should be set to the fuel_consumption value. 

Each class should have the following methods:
- drive(kilometers) - reduces the fuel based on the traveled kilometers and fuel consumption (km * fuel consumption). Keep in mind that you can start driving the vehicle only if you have enough fuel to finish the driving.

The default fuel consumption for the different vehicles is:
- Vehicle is 1.25
- SportCar is 10
- RaceMotorcycle is 8
- Car is 3


# Shop
Maria is expanding her business, and today, she is opening a grocery shop. You are hired to write a program that keeps track of the shop's inventory.

![image](https://user-images.githubusercontent.com/104040753/199553636-e9ec37b8-6bd6-4ed6-8c2b-35d39a7689c5.png)

In the product.py file, the class Product should be implemented. It is a base class for any type of food and drink.
The class should receive name: str, and quantity: int upon initialization. It should also have 3 additional methods:
- decrease(quantity: int) - decreases the quantity of the product only if there is enough
- increase(quantity: int) - increases the quantity of the product
- __repr__() - override the method, so it returns the name of the product 

In the file drink.py, the class Drink should be implemented. The class should inherit from the Product class. An instance of the Drink class will have a name and a quantity of 10.

In the food.py file, the Food class should be implemented. The class should inherit from the Product class. An instance of the Food class will have a name and a quantity of 15.

In the product_repository.py file, the class ProductRepository should be implemented. It is a repository for all products that are delivered to the grocery shop.

The class should have products: list - an empty list, which will be containing all products (objects). Also, the class should have 4 additional methods:
- add(product: Product) - adds a product to the repository
- find(product_name: str) - returns a product (object) with that name
- remove(product_name) - removes a product from the repository
- __repr__() - override the method, so it returns information for all products in the repository: 

    "{product_name1}: {quantity1}"
    
    {product_name2}: {quantity2}
    
    …
    
    {product_nameN}: {quantityN}"
