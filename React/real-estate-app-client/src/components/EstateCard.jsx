
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';
/* eslint-disable react/prop-types */
const EstateCard = (props) => {
    return (
            <Card className="card shadow" style={{ width: '18rem' }} key={props.id}>
                <Card.Img variant="top" src="https://imageio.forbes.com/specials-images/imageserve/61cdd9ec2bbdedb659077751/Neutral-living-color-corrected/960x0.jpg?format=jpg&width=1440" />
                <Card.Body>
                    <Card.Title>{props.name}</Card.Title>
                    <Card.Text>{props.description}</Card.Text>
                    <div className="d-flex flex-column mb-3">
                        <div>
                            Rooms: {props.rooms}
                        </div>
                        <div>
                            Price: {props.price}
                        </div>
                    </div>
                    <Button as={Link} to={`/estates/${props.id}`} variant="primary">Details</Button>
                </Card.Body>
            </Card>
    );
}

export default EstateCard