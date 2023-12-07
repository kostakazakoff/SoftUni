
import { useContext } from 'react';
import { Link } from 'react-router-dom';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import AuthContext from "../api/contexts/authContext";


const Navigation = () => {
    const { credentials } = useContext(AuthContext);

    console.log(credentials);
    return (
        <Navbar variant='pills' sticky="top" expand="lg" className="bg-body-tertiary shadow p-3" style={{ opacity: '0.9' }}>
            <Navbar.Brand as={Link} to='/'>Real Estates Site</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">

                    <Nav.Link as={Link} to='/'>Home</Nav.Link>

                    <Nav.Link as={Link} to='/estates'>Estates</Nav.Link>
                    

                    <NavDropdown title={credentials.email ? credentials.email : 'USER'} id="basic-nav-dropdown" align={{ lg: 'end' }}>
                        {!credentials.email && <NavDropdown.Item href='/login'>Login</NavDropdown.Item>}
                        {credentials.email && <NavDropdown.Item href='/estates/create'>Add estate</NavDropdown.Item>}
                        {credentials.email && <NavDropdown.Divider />}
                        {credentials.email && <NavDropdown.Item href='/login'>Logout</NavDropdown.Item>}
                    </NavDropdown>

                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation;
