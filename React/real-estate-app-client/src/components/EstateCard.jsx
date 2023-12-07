
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';
/* eslint-disable react/prop-types */


const EstateCard = (estate) => {
    return (
            <Card className="card shadow" style={{ width: '18rem' }} key={estate.id}>
                <Card.Img variant="top" src={estate.thumb} />
                <Card.Body>
                    <Card.Title>{estate.name}</Card.Title>
                    <Card.Text>{estate.description}</Card.Text>
                    <div className="d-flex flex-column mb-3">
                        <div>
                            Rooms: {estate.rooms}
                        </div>
                        <div>
                            Price: {estate.price} {estate.currency}
                        </div>
                    </div>
                    <Button as={Link} to={`/estates/${estate.id}`} variant="primary">Details</Button>
                </Card.Body>
            </Card>
    );
}

export default EstateCard