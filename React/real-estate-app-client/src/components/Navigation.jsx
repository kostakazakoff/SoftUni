
import { useContext } from 'react';
import { Link } from 'react-router-dom';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import AuthContext from "../api/contexts/authContext";
import Path from '../paths';


const Navigation = () => {
    const { username, isAuthenticated, jwt } = useContext(AuthContext);

    console.log(`isAuthenticated: ${isAuthenticated}`);
    return (
        <Navbar variant='pills' sticky="top" expand="lg" className="bg-body-tertiary shadow p-3" style={{ opacity: '0.9' }}>
            <Navbar.Brand as={Link} to='/'>RentProperty</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ms-auto">

                    <Nav.Link as={Link} to='/'>Home</Nav.Link>

                    <Nav.Link as={Link} to='/estates'>Estates</Nav.Link>

                    <Nav className="ms-auto">
                        <NavDropdown title={username || 'Guest'} id="basic-nav-dropdown" align="end">
                            {!jwt &&
                                <NavDropdown.Item>
                                    <Nav.Link as={Link} to={Path.LOGIN}>Login</Nav.Link>
                                </NavDropdown.Item>}
                            {!jwt &&
                                <NavDropdown.Item>
                                    <Nav.Link as={Link} to={Path.REGISTER}>Register</Nav.Link>
                                </NavDropdown.Item>}
                            {jwt &&
                                <NavDropdown.Item >
                                    <Nav.Link as={Link} to={Path.CREATE_ESTATE}>Add estate</Nav.Link>
                                </NavDropdown.Item>}
                            {jwt && <NavDropdown.Divider />}
                            {jwt &&
                                <NavDropdown.Item>
                                    <Nav.Link as={Link} to={Path.LOGOUT}>Logout</Nav.Link>
                                </NavDropdown.Item>}
                        </NavDropdown>
                    </Nav>

                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation;
