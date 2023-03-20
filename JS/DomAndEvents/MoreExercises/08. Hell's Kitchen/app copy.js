function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
   const input = document.querySelector('textarea');
   const bestRestaurantField = document.querySelector('#bestRestaurant > p');
   const bestWorkersField = document.querySelector('#workers > p');

   function onClick() {
      let restaurants = {};
      Array.from(JSON.parse(input.value)).forEach(restaurant => {
         let [brand, workers] = restaurant.split(' - ');
         workers = workers.split(', ');
         let totalSallary = 0;
         let numberOfWorkers = 0;

         workers.forEach(workerInfo => {
            let [name, sallary] = workerInfo.split(' ');
            sallary = Number(sallary);

            if (!restaurants.hasOwnProperty(brand)) {
               restaurants[brand] = { 'workers': [], 'averageSallary': 0, 'bestSallary': 0 };
            }

            restaurants[brand]['workers'].push({ name, sallary });
            totalSallary += sallary;
            if (sallary > restaurants[brand]['bestSallary']) {
               restaurants[brand]['bestSallary'] = sallary;
            }
            numberOfWorkers++;
         })

         restaurants[brand]['averageSallary'] = totalSallary / numberOfWorkers;
         restaurants[brand]['workers'].sort((a, b) => b['sallary'] - a['sallary']);
      })

      let sotrtedRestBrands = Object.keys(restaurants).sort((a, b) => restaurants[b]['averageSallary'] - restaurants[a]['averageSallary']);
      let bestRestBrand = sotrtedRestBrands[0];
      let averageSallary = restaurants[bestRestBrand]['averageSallary'].toFixed(2)
      let bestSallary = restaurants[bestRestBrand]['bestSallary'].toFixed(2)
      bestRestaurantField.textContent = `Name: ${bestRestBrand} Average Salary: ${averageSallary} Best Salary: ${bestSallary}`

      let bestWorkers = [];
      Object.values(restaurants[bestRestBrand]['workers']).forEach(w => {
         bestWorkers.push(`Name: ${w['name']} With Salary: ${w['sallary']}`)
      })
      bestWorkersField.textContent = bestWorkers.join(' ')
   }
}