import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

import { Container } from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

import api from "../../api/helpers/Api";
import AuthContext from "../../api/contexts/authContext";


const Login = () => {
    const { setCredentials } = useContext(AuthContext);
    const [user, setUser] = useState({});

    const navigate = useNavigate();

    const handleCredentialsChange = (e) => {
        setUser(old => ({ ...old, [e.target.name]: e.target.value }));
    }

    const SubmitHandler = (e) => {
        e.preventDefault();

        if (!user.email || !user.password) {
            throw new Error('Please enter your email and password');
        }

        api.post('login', user)
            .then(
                response => setCredentials(credentials => ({
                    ...credentials,
                    ...response.data.user,
                    'jwt': response.data.jwt,
                })))
            .then(navigate('/estates'))
            .catch(err => console.log(err))
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
                            value={user.email || ''}
                            onChange={handleCredentialsChange}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            name="password"
                            value={user.password || ''}
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

export default Login;
