function solve() {
    const btnDepart = document.getElementById('depart');
    const btnArrive = document.getElementById('arrive');
    const info = document.getElementById('info');
    const URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    let stopName;
    let nextId = '1567';
    let atWork = true;

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
                btnArrive.disabled = true;
                info.textContent = 'Error'
                atWork = false;
            })
    }

    async function arrive() {
        if (atWork) {
            btnArrive.disabled = true;
            btnDepart.disabled = false;
            info.textContent = `Arriving at ${stopName}`;
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();