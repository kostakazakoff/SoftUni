const baseURL = 'http://localhost:8080/api'

export const getData = async (root, method='GET') => {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const response = await fetch(`${baseURL}/${root}`, options);
    const data = await response.json();

    return Object.values(data)[0];
};
