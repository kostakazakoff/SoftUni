function songsFilter(arr) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
        print(chosenType) {
            if (chosenType == this.typeList || chosenType == 'all') {
                console.log(this.name);
            };
        };
    };

    [numberOfSongs, ...songsInfo] = arr;
    choice = songsInfo[songsInfo.length - 1];
    songsInfo.slice(0, -1)
        .forEach(song => {
            newSong = new Song(...song.split('_'));
            newSong.print(choice)
        });
}

// songsFilter([4,
//     'favourite_DownTown_3:14',
//     'listenLater_Andalouse_3:24',
//     'favourite_In To The Night_3:58',
//     'favourite_Live It Up_3:48',
//     'listenLater']
// )