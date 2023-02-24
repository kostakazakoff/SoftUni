function orderArray(arr){
    result = arr.sort((a, b) => a.localeCompare(b));
    for (i in result) {
        console.log(`${Number(i)+1}.${result[i]}`)
        }
    }