function catsInClass(arrOfCats) {
    class Cat {
        constructor(catName, catAge) {
            this.catName = catName;
            this.catAge = catAge;
        };
        meow() {
            console.log(`${this.catName}, age ${this.catAge} says Meow`);
        };
    }

    arrOfCats.forEach(cat => {
        let newCat = new Cat(...cat.split(' '));
        newCat.meow();
    });
}

// catsInClass(['Mellow 2', 'Tom 5'])