const baseURL = 'http://localhost:8000/api'

export const fetchServer = async (root, inputData, method='GET') => {
    let options;
    if (method == 'POST') {
        if (inputData.images) {
            console.log(inputData.images);
        }
        options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: JSON.stringify({...inputData}),
        };
    } else {
        options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        };
    }
    
    const response = await fetch(`${baseURL}/${root}`, options);
    const data = await response.json();

    return data;
};
