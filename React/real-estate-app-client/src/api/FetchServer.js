const baseURL = 'http://localhost:8000/api'

export const fetchServer = async (root, inputData, method='GET') => {
    let options;
    if (method == 'GET') {
        options = {
            method: method,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
            }
        };
    } else {
        options = {
            method: method,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'multipart/form-data',
                'Accept': 'application/json',
            },
            body: JSON.stringify({...inputData}),
        };
    }
    
    const response = await fetch(`${baseURL}/${root}`, options);
    const data = await response.json();

    return data;
};
