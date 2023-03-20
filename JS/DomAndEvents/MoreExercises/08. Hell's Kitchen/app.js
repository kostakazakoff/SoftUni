function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
   const input = document.querySelector('textarea');
   const bestRestaurantField = document.querySelector('#bestRestaurant > p');
   const bestWorkersField = document.querySelector('#workers > p');

   function onClick() {
      let restaurants = {};

      // Add restaurant objects to restaurants
      Array.from(JSON.parse(input.value)).forEach(restaurant => {
         let totalSallary = 0;
         let numberOfWorkers = 0;
         let [brand, workers] = restaurant.split(' - ');
         workers = workers.split(', ');
         
         // Add workers, average sallary and best sallary to the current restaurant
         workers.forEach(workerInfo => {
            let [name, sallary] = workerInfo.split(' ');
            sallary = Number(sallary);

            // if there is not such restaurant, creating it
            if (!restaurants.hasOwnProperty(brand)) {
               restaurants[brand] = { 'workers': {}, 'averageSallary': 0, 'bestSallary': 0 };
            }

            // Add the worker objects (worker: sallary)
            restaurants[brand]['workers'][name] = sallary;
            totalSallary += sallary;

            // Select the best sallary
            if (sallary > restaurants[brand]['bestSallary']) {
               restaurants[brand]['bestSallary'] = sallary;
            }

            numberOfWorkers++;
         })
         
         // Calc the average sallary
         restaurants[brand]['averageSallary'] = totalSallary / numberOfWorkers;
      })

      // Sort restaurants by average sallary
      let sotrtedRestBrands = Object.keys(restaurants).sort((a, b) => restaurants[b]['averageSallary'] - restaurants[a]['averageSallary']);

      // Extract the best restaurant by average sallary
      let bestRestBrand = sotrtedRestBrands[0];

      // Formatting the sallaries output
      let averageSallary = restaurants[bestRestBrand]['averageSallary'].toFixed(2)
      let bestSallary = restaurants[bestRestBrand]['bestSallary'].toFixed(2)

      //Adding the output to the field
      bestRestaurantField.textContent = `Name: ${bestRestBrand} Average Salary: ${averageSallary} Best Salary: ${bestSallary}`

      // Creating a best restaurant workers list
      let bestWorkers = [];
      Object.entries(restaurants[bestRestBrand]['workers']).forEach(([k, v]) => {
         bestWorkers.push([k, v])
      })

      // Sorting best workers by sallary and adding it to the output field
      bestWorkersField.textContent = bestWorkers
      .sort((a, b) => b[1] - a[1])
      .map(([a, b]) => `Name: ${a} With Salary: ${b}`)
      .join(' ')
   }
}