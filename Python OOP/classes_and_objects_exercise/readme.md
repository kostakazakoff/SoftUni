# Vet

Create a class called Vet. Upon initialization, it should receive a name (string). It should also have an instance attribute called animals (empty list by default).

There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; and space (5 by default). You should create 3 additional instance methods:
- register_animal(animal_name)
    - If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
    - Otherwise, returns "Not enough space"
- unregister_animal(animal_name)
    - If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
    - Otherwise, returns "{animal} not in the clinic"
- info()

Returns info about the vet, the number of animals in his list and the free space in the clinic:

"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


# Time
Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers).
The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59.
You should also create 3 additional instance methods:
- set_time(hours, minutes, seconds) - updates the time with the new values
- get_time() - returns "{hh}:{mm}:{ss}"
- next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)


# Account
Create a class called Account. Upon initialization, it should receive an id (number), a name (string), and a balance (integer; optional; 0 by default). The class should also have 3 additional instance methods:
- credit(amount) - adds the amount to the balance and returns the new balance
- debit(amount)
    - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance.
    - Otherwise, return "Amount exceeded balance"
- info() - returns "User {name} with account {id} has {balance} balance"


# Pizza Delivery
Create a class called PizzaDelivery. Upon initialization, it should receive a name (string), a price (float), and ingredients (dictionary). The class should also have an instance attribute ordered set to False by default. You should also create 3 additional instance methods:
- add_extra(ingredient: str, quantity: int, price_per_quantity: float):
    - If we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update the pizza price by adding the ingredient price for the given quantity
    - If we do not have this ingredient in our pizza, we should add it and update the pizza price
- remove_ingredient(ingredient: str, quantity: int, price_per_quantity: float):
    - If we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
    - If we have the ingredient, but we try to remove more than we have available, we should return the following message "Please check again the desired quantity of {ingredient}!"
    - Otherwise, remove the given quantity of the ingredient and update the pizza price by removing the ingredient price for the given quantity
- make_order()
    - Set the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared with {ingredient: quantity} and the price will be {price}lv.". The ingredients should be separated by a comma and a space ", "
    - Keep in mind that once the pizza is ordered, no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"


# To-do List
In this exercise, we are going to create a whole project step-by-step, starting with the project structure:

![image](https://user-images.githubusercontent.com/104040753/198872501-186feec4-b7a3-4598-8546-d871852455b6.png)

Create separate files for each class, as shown above. You are tasked to create two classes: a Task class and a Section class.
The Task class should receive a name (string) and a due_date (str) upon initialization. A task also has two attributes: comments (empty list) and completed set to False by default.
### The Task class
should also have five additional methods:
- change_name(new_name: str)
    - Changes the name of the task and returns the new name.
    - If the new name is the same as the current name, returns "Name cannot be the same."
- change_due_date(new_date: str) 
    - Changes the due date of the task and returns the new date.
    - If the new date is the same as the current date, returns "Date cannot be the same."
- add_comment(comment: str)
    - Adds a comment to the task.
- edit_comment(comment_number: int, new_comment: str)
    - The comment number value represents the index of the comment we want to edit. The method should change the comment and return all the comments, separated by comma and space (", ")
    - If the comment number is out of range, returns "Cannot find comment."
-  details()
    - Returns the task's details in this format:
    "Name: {task_name} - Due Date: {due_date}"

### The Section class
should receive a name (string) upon initialization. The task also has one instance attribute:
tasks (empty list)

### The Section class
should also have four methods:
- add_task(new_task: Task)
    - Adds a new task to the collection and returns "Task {task details} is added to the section"
    - If the task is already in the collection, returns "Task is already in the section {section_name}"
- complete_task(task_name: str) 
    - Changes the task to completed (True) and returns "Completed task {task_name}"
    - If the task is not found, returns "Could not find task with the name {task_name}"
- clean_section()
    - Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
- view_section()
    - Returns information about the section and its tasks in this format:
    
        "Section {section_name}:
        
        {details of the first task}
        
        {details of the second task}
        
        …
        
        {details of the n task}"
        

# Guild System
You are tasked to create two classes: a Player class and a Guild class. 

![image](https://user-images.githubusercontent.com/104040753/199203776-94299eda-7276-4900-ad26-3ce0b082d7d4.png)

### The Player class
should receive a name (string), a hp (int), and a mp (int) upon initialization. The Player also has 2 instance attributes: skills (empty dictionary that will contain the skills of each player and its mana cost) and a guild set to "Unaffiliated" by default.
The Player class should also have two additional methods:
- add_skill(skill_name, mana_cost)
    - Adds the skill and the corresponding mana cost to the dictionary of skills. Returns "Skill {skill_name} added to the collection of the player {player_name}"
    - If the skill is already in the collection, returns "Skill already added"
- player_info() 
    - Returns the player's information, including their skills, in this format:
    
        "Name: {player_name}

        Guild: {guild_name}
        
        HP: {hp}
        
        MP: {mp}
        
        ==={skill_name_1} - {skill_mana_cost}
        
        ==={skill_name_2} - {skill_mana_cost}
        
        …
        
        ==={skill_name_N} - {skill_mana_cost}"

The Guild class receives a name (string). The Guild should also have one instance attribute players (an empty list which will contain the players of the guild). The class also has 3 additional methods:
- assign_player(player: Player)
    - Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
    - If he is already in the guild, returns "Player {player_name} is already in the guild."
    - If the player is in another guild, returns "Player {player_name} is in another guild."
- kick_player(player_name: str)
    - Removes the player from the guild and returns "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class to "Unaffiliated".
    - If there is no such player in the guild, returns "Player {player_name} is not in the guild."
- guild_info() 
    - Returns the guild's information, including the players in the guild, in the format:

        "Guild: {guild_name}

        {first_player's info}
        
        …
        
        {Nplayer's info}"


# Spoopify
You are tasked to create three classes: a Song class, an Album class, and a Band class.

![image](https://user-images.githubusercontent.com/104040753/199204712-266698a8-b291-41cc-bd3f-7ddde0d596d2.png)

### The Song class
should receive a name (string), a length (float), and a single (bool) upon initialization. It has one method:
get_info()
Returns the information of the song in this format: "{song_name} - {song_length}"

### The Album class
should receive a name (string) upon initialization and might receive one or more songs. It also has instance attributes: published (False by default) and songs (an empty list). It has four methods:
- add_song(song: Song)
    - Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
    - If the song is single, returns "Cannot add {song_name}. It's a single"
    - If the album is published, returns "Cannot add songs. Album is published."
    - If the song is already added, return "Song is already in the album."
- remove_song(song_name: str)
    - Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
    - If the song is not in the album, returns "Song is not in the album."
    - If the album is published, returns "Cannot remove songs. Album is published."
- publish()
    - Publishes the album (set to True) and returns "Album {name} has been published."
    - If the album is published, returns "Album {name} is already published."
- details()
    - Returns the information of the album, with the songs in it, in the format: 

        "Album {name}

        == {first_song_info}
        
        == {second_song_info}
        
        …
        
        == {n_song_info}"

### The Band class
should receive a name (string) upon initialization. It also has an attribute albums (an empty list). 
The class has three methods:
- add_album(album: Album)
    - Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
    - If the album is already added, returns "Band {band_name} already has {album_name} in their library."
- remove_album(album_name: str)
    - Removes the album from the collection and returns "Album {name} has been removed."
    - If the album is published, returns "Album has been published. It cannot be removed."
    - If the album is not in the collection, returns "Album {name} is not found."
- details()
    - Returns the information of the band, with their albums, in this format: 
        "Band {name}
        
        {album details}
        
        ...
        
        {album details}"



# Library*
Create a class called Library, where the information regarding the users and books rented/available will be stored. Create another one called User, where the information for each of the library users will be stored, and Registration class, where user information will be administrated (created/edited/deleted) and stored in the Library records.

![image](https://user-images.githubusercontent.com/104040753/199205979-2cbe34ef-03ea-44c9-b0c3-a8f6f7c5abf1.png)

### Class User
In the user.py file, create class User. Upon initialization, it should receive user_id (int) and username (string). The class should also have an instance attribute books that is an empty list. You should also create 2 instance methods:
- info() - returns a string containing the books currently rented by the user in ascending order separated by comma and space.
- __str__() - override the method to get a string in the following format "{user_id}, {username}, {list of rented books}"


### Class Library
In the library.py create a class Library. Upon initialization, it will not receive anything, but it should have the following instance attributes: 
- user_records - an empty list that will store the users (users objects) of the library
- books_available - an empty dictionary that will keep information regarding the authors (key: str) and the books available for each of the authors (list of strings)
- rented_books - an empty dictionary that will keep information regarding the usernames (key: str) and nested dictionary as a value in which will keep information regarding the book names (key: str) and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}).

You should also create 2 additional instance methods:
- get_book(author: str, book_name: str, days_to_return: int, user: User):
    - If the book is available in the library adds it to the books list for this user, updates the library records (rented_books and available_books dicts), and returns the following message: "{book_name} successfully rented for the next {days_to_return} days!"
    - If it is already rented, returns the following message "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"
- return_book(author:str, book_name:str, user: User):
    - If the book is in the user's books list, returns it in the library (update books_available and rented_books class attributes) and removes it from the books list for this user
    - Otherwise, returns the following message "{username} doesn't have this book in his/her records!"

### Class Registration 
In the registration.py, create a class called Registration. Upon initialization, It will not receive anything, but we'll have these three methods.
- add_user(user: User, library: Library):
    - Adds the user if we do not have them in the library's user records already
    - Otherwise, returns the message "User with id = {user_id} already registered in the library!"
- remove_user(user: User, library: Library):
    - Removes the user from the library records if present
    - Otherwise, returns the message "We could not find such user to remove!"
- change_username(user_id: int, new_username: str, library: Library):
    - If there is a record with the same user id in the library and the username is different than the provided one, changes the username with the new one provided and returns the message "Username successfully changed to: {new_username} for user id: {user_id}". Changes his username in the rented_books dictionary as well (if present).
    - If the new username is the same for this id, returns the following message "Please check again the provided username - it should be different than the username used so far!".
    - If there is no record for the provided id returns "There is no user with id = {user_id}!"
