
import { useContext } from 'react';
import { Link } from 'react-router-dom';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import AuthContext from "../api/contexts/authContext";


const Navigation = () => {
    const { email, isAuthenticated } = useContext(AuthContext);

    console.log('isAuthenticated: ' + isAuthenticated);
    return (
        <Navbar variant='pills' sticky="top" expand="lg" className="bg-body-tertiary shadow p-3" style={{ opacity: '0.9' }}>
            <Navbar.Brand as={Link} to='/'>Real Estates Site</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">

                    <Nav.Link as={Link} to='/'>Home</Nav.Link>

                    <Nav.Link as={Link} to='/estates'>Estates</Nav.Link>


                    <NavDropdown title={email ? email : 'USER'} id="basic-nav-dropdown" align={{ lg: 'end' }}>
                        {!email &&
                            <NavDropdown.Item>
                                <Nav.Link as={Link} to='/login'>Login</Nav.Link>
                            </NavDropdown.Item>}
                        {email &&
                            <NavDropdown.Item >
                                <Nav.Link as={Link} to='/estates/create'>Add estate</Nav.Link>
                            </NavDropdown.Item>}
                        {email && <NavDropdown.Divider />}
                        {email &&
                            <NavDropdown.Item>
                                <Nav.Link as={Link} to='/logout'>Logout</Nav.Link>
                            </NavDropdown.Item>}
                    </NavDropdown>

                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation;
