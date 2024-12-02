class LibraryCollection {
    constructor(capacity) {
        this.capacity = capacity;
        this.books = [];
    }

    addBook(bookName, bookAuthor) {
        if (this.capacity === 0) {
            throw new Error('Not enough space in the collection.')
        }
        this.books.push({ bookName, bookAuthor, payed: false });
        this.capacity--;
        return `The ${bookName}, with an author ${bookAuthor}, collect.`
    }

    payBook(bookName) {
        const book = this.books.find(b => b.bookName === bookName);
        if (!book) { throw new Error(`${bookName} is not in the collection.`) };
        if (book.payed) { throw new Error(`${bookName} has already been paid.`) };
        book.payed = true;
        return `${bookName} has been successfully paid.`;
    }

    removeBook(bookName) {
        const book = this.books.find(b => b.bookName === bookName);
        if (!book) { throw new Error(`The book, you're looking for, is not found.`) };
        if (!book.payed) { throw new Error(`${bookName} need to be paid before removing from the collection.`) };
        const idx = this.books.indexOf(book);
        this.books.splice(idx, 1);
        this.capacity++;
        return `${bookName} remove from the collection.`;
    }

    getStatistics(bookAuthor) {
        if (bookAuthor) {
            const book = this.books.find(b => b.bookAuthor === bookAuthor);
            if (!book) { throw new Error(`${bookAuthor} is not in the collection.`) };
            return `${book.bookName} == ${book.bookAuthor} - ${this.bookStatus(book)}.`
        }
        let output = [`The book collection has ${this.capacity} empty spots left.`];
        let sortedBooks = this.books.sort((a, b) => this.sortBooks(a, b));
        sortedBooks.forEach(b => output.push(`${b.bookName} == ${b.bookAuthor} - ${this.bookStatus(b)}.`));
        return output.join('\n');
    }

    sortBooks(a, b) {
        const aName = a.bookName;
        const bName = b.bookName;
        return aName.localeCompare(bName);
    }

    bookStatus(book) {
        let status = book.payed;
        if (status) { status = 'Has Paid' } else { status = 'Not Paid' };
        return status;
    }
}

// const library = new LibraryCollection(5)
// library.addBook('Don Quixote', 'Miguel de Cervantes');
// library.payBook('Don Quixote');
// library.addBook('In Search of Lost Time', 'Marcel Proust');
// library.addBook('Ulysses', 'James Joyce');
// console.log(library.getStatistics());
