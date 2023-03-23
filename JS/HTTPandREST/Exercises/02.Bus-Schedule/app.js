function solve() {
    const btnDepart = document.getElementById('depart');
    const btnArrive = document.getElementById('arrive');
    const info = document.getElementById('info');
    const URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    let stopName;
    let nextId = 'depot';
    let atWork = true;

    function depart() {
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
        btnDepart.disabled = true;
        btnArrive.disabled = false;
    }

    async function arrive() {
        if (atWork) {
            info.textContent = `Arriving at ${stopName}`;
            btnArrive.disabled = true;
            btnDepart.disabled = false; 
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();