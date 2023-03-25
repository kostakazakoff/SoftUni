function attachEvents() {
    const locationInput = document.getElementById('location');
    const submitBtn = document.getElementById('submit');
    const forecastDiv = document.getElementById('forecast');
    const todayDiv = document.getElementById('current');
    const upcomingDiv = document.getElementById('upcoming');
    const LOCATIONS_URL = 'http://localhost:3030/jsonstore/forecaster/locations/';
    const TODAY_WEATHER_URL = 'http://localhost:3030/jsonstore/forecaster/today/';
    const UPCOMING_WEATHER_URL = 'http://localhost:3030/jsonstore/forecaster/upcoming/';
    let cityCode;

    const weatherSymbols = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☔',
        'Degrees': '°'
    }

    submitBtn.addEventListener('click', getLocation);

    function errorMessage() {
        forecastDiv.style.display = 'block';
        forecastDiv.textContent = 'Error';
    }

    function getLocation() {
        fetch(LOCATIONS_URL)
            .then(res => res.json())
            .then(data => getCurrentWeather(data))
            .catch(() => errorMessage())
    }

    function getCurrentWeather(locations) {
        forecastDiv.style.display = 'block';
        Object.values(locations).forEach(loc => {
            if (loc.name === locationInput.value) {
                cityCode = loc.code;
            }
        })

        fetch(`${TODAY_WEATHER_URL}${cityCode}`)
            .then(res => res.json())
            .then(data => createTodayEl(data))
            .then(getUpcomingWeather())
            .catch(() => errorMessage())
    }

    function getUpcomingWeather() {
        upcomingDiv.innerHTML = '<div class="label">Three-day forecast</div>'
        fetch(`${UPCOMING_WEATHER_URL}${cityCode}`)
            .then(res => res.json())
            .then((data) => createUpcomingEl(data))
            .catch(() => errorMessage())
    }

    function createTodayEl(data) {
        todayDiv.innerHTML = `
        <div class="label">Current conditions</div>
        <div class="forecast">
            <span class="condition symbol">${weatherSymbols[data.forecast.condition]}</span>
            <span class="condition">
                <span class="forecast-data">${data.name}</span>
                <span class="forecast-data">${data.forecast.low}${weatherSymbols['Degrees']}/${data.forecast.high}${weatherSymbols['Degrees']}</span>
                <span class="forecast-data">${data.forecast.condition}</span>
            </span>
        </div>
        `
    }

    function createUpcomingEl(data) {
        info = document.createElement('div');
        info.className = 'forecast-info';
        Object.values(data.forecast).forEach(day => {
            info.innerHTML += `
            <span class="upcoming">
                <span class="symbol">${weatherSymbols[day.condition]}</span>
                <span class="forecast-data">${day.low}${weatherSymbols['Degrees']}/${day.high}${weatherSymbols['Degrees']}</span>
                <span class="forecast-data">${day.condition}</span>
            </span>
            `
        })
        upcomingDiv.appendChild(info);
    }
}

attachEvents();


// <div class="forecast-info">
//             <span class="upcoming">
//                 <span class="symbol">${weatherSymbols[data.forecast.condition]}</span>
//                 <span class="forecast-data">
//                 ${data.forecast.low}${weatherSymbols['Degrees']}/
//                 ${data.forecast.high}${weatherSymbols['Degrees']}
//                 </span>
//                 <span class="forecast-data">${data.forecast.condition}</span>
//             </span>
//         </div>