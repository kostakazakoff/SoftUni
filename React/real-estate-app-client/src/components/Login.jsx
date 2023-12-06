
import { Container } from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/Api";


const LoginPage = () => {
    const [credentials, setCredentials] = useState({});
    const navigate = useNavigate();

    const handleCredentialsChange = (e) => {
        setCredentials(old => ({ ...old, [e.target.name]: e.target.value }))
    }

    const SubmitHandler = (e) => {
        e.preventDefault();

        // fetchServer('login', credentials, 'POST')
        // .then(console.log(Cookies.get()))
        // .then(navigate('/estates'));

        api.post('login', credentials)
            .then(request => console.log(request))
            .then(navigate('/estates'))
            .catch(err => console.log(err));
    }

    return (
        <>
            <Container style={{ width: '30%', margin: '60px auto' }}>
                <Form id='creste' onSubmit={SubmitHandler}>
                    <Form.Group className="mb-3" controlId="email">
                        <Form.Label>Email</Form.Label>
                        <Form.Control
                            type="email"
                            name="email"
                            value={credentials.email ? credentials.email : ''}
                            onChange={handleCredentialsChange}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            name="password"
                            value={credentials.password ? credentials.password : ''}
                            onChange={handleCredentialsChange}
                        />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Login
                    </Button>
                </Form>
            </Container>
        </>
    );
}

export default LoginPage;
