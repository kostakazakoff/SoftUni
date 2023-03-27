function solve() {
    const btnDepart = document.getElementById('depart');
    const btnArrive = document.getElementById('arrive');
    const info = document.querySelector('.info');
    const URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    let stopName;
    let nextId = 'depot';

    function depart() {
        btnDepart.disabled = true;
        btnArrive.disabled = false;
        fetch(`${URL}${nextId}`)
            .then((response) => response.json())
            .then((data) => {
                stopName = data.name;
                nextId = data.next;
                info.textContent = `Next stop ${stopName}`;
            })
            .catch(() => {
                info.textContent = 'Error';
                btnArrive.disabled = true;
                btnArrive.disabled = true;
            })
    }

    async function arrive() {
        btnArrive.disabled = true;
        btnDepart.disabled = false;
        info.textContent = `Arriving at ${stopName}`;
        }

    return {
        depart,
        arrive
    };
}

let result = solve();