import Cookies from 'js-cookie';


const baseURL = 'http://localhost:8000/api'

export const fetchServer = async (root, inputData, method = 'GET') => {

    // const cookieResponse = await fetch('http://localhost:8000/sanctum/csrf-cookie');
    // const token = await cookieResponse['jwt'];

    const csrfToken = 'eyJpdiI6IjNDSTg1L3hYa05aZkl1ZGx5V0NhU2c9PSIsInZhbHVlIjoiTTViQy9Ra0lsMnNCTU92Rys2cWVINW1hZE1FYkxxdGErSnVZazRrZGRMVDJZMnFHK29OWWY3M1ptTkpSbHlOdjZWdHJYT1d5RTkvamFWTFhsUFZZRDNybUhqM1E3Nm5lNE1kVzNkamxZMERPa0xHN1BFS0U1bm9QOWkrWW1YZ2giLCJtYWMiOiI1OThhNjE4OWY0ZTYxMWVkYTNiMzU4NWU0NzE2MDRiN2M4MTBkZjZlMmY1MjQ4MDE2NGVjMzkzNTFjMWJjYWE1IiwidGFnIjoiIn0%3D';

    // Cookies.set('token', token, { expires: 7, secure: false });

    let options;
    if (method == 'GET') {
        options = {
            method: method,
            headers: {
                'credential': 'include',
                // 'Authorization': `Bearer ${token}`,
                'Origin': 'http:localhost:3000',
                'Accept': 'application/json',
            }
        };
    } else {
        options = {
            method: method,
            headers: {
                'Origin': 'http:localhost:3000',
                'X-CSRF-TOKEN': csrfToken,
                credentials: 'include',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ ...inputData }),
        };
    }

    const response = await fetch(`${baseURL}/${root}`, options);
    const data = await response.json();

    return data;
};
