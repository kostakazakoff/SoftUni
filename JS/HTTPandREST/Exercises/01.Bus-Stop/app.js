function getInfo() {
    const busStopIdInput = document.getElementById('stopId');
    const busStopId = busStopIdInput.value;
    const busStopName = document.getElementById('stopName');
    const busesOutput = document.getElementById('buses');
    const URL = 'http://localhost:3030/jsonstore/bus/businfo/';

    fetch(`${URL}${busStopId}`, { method: 'GET' })
        .then((response) => response.json())
        .then((data) => outputData(data))
        .catch((err) => busStopName.textContent = err)

    function outputData(data) {
        ({ buses, name } = data)
        busStopName.textContent = name;
        Object.entries(buses).forEach(([busId, time]) => {
            const li = document.createElement('li');
            li.textContent = `Bus ${busId} arrives in ${time} minutes`;
            busesOutput.appendChild(li);
        })
    }
}