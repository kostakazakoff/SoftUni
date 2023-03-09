function moviesOrganiser(arr) {
    let allMovies = [];

    function commandParser(command) {
        if (command.includes('addMovie')) {
            movieName = command.split('addMovie ')[1];
            return ['addMovie', movieName, ''];
        } else if (command.includes('directedBy')) {
            [movieName, value] = command.split(' directedBy ');
            return ['directedBy', movieName, value];
        } else if (command.includes('onDate')) {
            [movieName, value] = command.split(' onDate ');
            return ['onDate', movieName, value];
        }
    }

    arr.forEach(command => {
        [action, movieName, value] = commandParser(command);
        if (action == 'addMovie') {
            allMovies.push({'name': movieName});
        }
        else {
            for (movie of allMovies) {
                if ( movieName == movie.name && action == 'directedBy') {
                    movie['director'] = value;
                } else if (movieName == movie.name && action == 'onDate') {
                    movie['date'] = value;
                }
            }
        }
    });

    for (movie of allMovies) {
        console.log(JSON.stringify(movie));
    }
}

// moviesOrganiser(['addMovie The Avengers',
//     'addMovie Superman',
//     'The Avengers directedBy Anthony Russo',
//     'The Avengers onDate 30.07.2010',
//     'Captain America onDate 30.07.2010',
//     'Captain America directedBy Joe Russo'])