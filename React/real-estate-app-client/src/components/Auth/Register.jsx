import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import { Container } from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

import api from "../../api/helpers/Api";
import Path from "../../paths";


const Register = () => {
    const [user, setUser] = useState({});

    const navigate = useNavigate();

    const handleCredentialsChange = (e) => {
        setUser(old => ({ ...old, [e.target.name]: e.target.value }));
    }

    const SubmitHandler = (e) => {
        e.preventDefault();

        if (user.password !== user.re_password) {
            throw new Error('Your password is incorrect');
        }

        if (!user.email || !user.password) {
            throw new Error('Please enter your email and password');
        }

        api.post('register', user)
            .then(response => {
                response.data.success
                    ? navigate(Path.LOGIN)
                    : console.log(response.data.message)
            })
            .catch(err => console.log(err))
    }

    return (
        <>
            <Container style={{ width: '30%', margin: '60px auto' }}>
                <Container style={{ textAlign: "center", marginBottom: "2rem" }}>
                    <div style={{ fontSize: '3rem', }}>Signup</div>
                    <Link to={'/login'} style={{ color: "#0d6efd", textDecoration: "none" }}>Or login to an existing account</Link>
                </Container>

                <Form id='creste' onSubmit={SubmitHandler}>

                    <Form.Group className="mb-3" controlId="name">
                        <Form.Label>Username</Form.Label>
                        <Form.Control
                            type="text"
                            name="name"
                            value={user.name || ''}
                            onChange={handleCredentialsChange}
                        />
                    </Form.Group>

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

                    <Form.Group className="mb-3" controlId="re_password">
                        <Form.Label>Reenter Password</Form.Label>
                        <Form.Control
                            type="password"
                            name="re_password"
                            value={user.re_password || ''}
                            onChange={handleCredentialsChange}
                        />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Register
                    </Button>
                </Form>
            </Container>
        </>
    );
}

export default Register;