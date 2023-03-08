function songsFilter(arr) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
        isChosen(type) {
            if (type == this.typeList || type == 'all') {
                return true;
            };
        };
    }

    [numberOfSongs, ...songsInfo] = arr;
    choice = songsInfo[songsInfo.length - 1];
    songsInfo.slice(0, -1)
        .forEach(song => {
            newSong = new Song(...song.split('_'));
            if (newSong.isChosen(choice)) {
                console.log(newSong.name)
            }
        });
}

// songsFilter([4,
//     'favourite_DownTown_3:14',
//     'listenLater_Andalouse_3:24',
//     'favourite_In To The Night_3:58',
//     'favourite_Live It Up_3:48',
//     'all']
// )