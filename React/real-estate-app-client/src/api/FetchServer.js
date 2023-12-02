const baseURL = 'http://localhost:8000/api'

export const fetchServer = async (root, inputData, method='GET') => {
    let options;
    if (method == 'GET') {
        if (inputData.images) {
            console.log(inputData.images);
        }
        options = {
            method: method,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
            }
        };
    } else {
        options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: JSON.stringify({...inputData}),
        };
    }
    
    const response = await fetch(`${baseURL}/${root}`, options);
    const data = await response.json();

    return data;
};
