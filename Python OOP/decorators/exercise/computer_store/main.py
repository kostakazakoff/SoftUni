from project.computer_store_app import ComputerStoreApp

 
computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)) 
print(computer_store.build_computer("Desktop Computer", "Apple", "Macbook", "Apple M1 Max", 128))
print(computer_store.warehouse)
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
print(computer_store.sell_computer(8000, "Apple M1 Max", 32))
print(computer_store.profits)