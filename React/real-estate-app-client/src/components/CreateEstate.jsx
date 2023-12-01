import { Container } from "react-bootstrap";
import { fetchServer } from "../api/FetchServer";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const CreateEstate = () => {
    const [data, setData] = useState();

    const CreateEstateSubmitHandler = (e) => {
        e.preventDefault();

        const estateData = Object.fromEntries(new FormData(e.currentTarget));

        const responseData = fetchServer('real-estates/create', estateData, 'POST');

        // console.log(responseData);
    }

    return (
        <Container>
            <Form id='creste' onSubmit={CreateEstateSubmitHandler} encType="multipart/form-data">
                <Form.Group className="mb-3" controlId="name">
                    <Form.Label>Property name</Form.Label>
                    <Form.Control type="text" placeholder="Enter property name" name="name" />
                    {/* <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text> */}
                </Form.Group>

                <Form.Group className="mb-3" controlId="location">
                    <Form.Label>Location</Form.Label>
                    <Form.Control type="text" name="location" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="description">
                    <Form.Label>Description</Form.Label>
                    <Form.Control type="text" name="description" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="price">
                    <Form.Label>Price</Form.Label>
                    <Form.Control type="text" name="price" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="currency">
                    <Form.Label>Currency</Form.Label>
                    <Form.Control type="text" name="currency" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="latitude">
                    <Form.Label>Latitude</Form.Label>
                    <Form.Control type="text" name="latitude" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="longitude">
                    <Form.Label>Longitude</Form.Label>
                    <Form.Control type="text" name="longitude" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="category_id">
                    <Form.Label>Category</Form.Label>
                    <Form.Control type="number" name="category_id" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="rooms">
                    <Form.Label>Rooms</Form.Label>
                    <Form.Control type="number" name="rooms" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="arrive_hour">
                    <Form.Label>Arrive hour</Form.Label>
                    <Form.Control type="text" name="arrive_hour" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="leave_hour">
                    <Form.Label>Leave hour</Form.Label>
                    <Form.Control type="text" name="leave_hour" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="user_id">
                    <Form.Label>Ouner</Form.Label>
                    <Form.Control type="number" name="user_id" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="images">
                    <Form.Label>Images</Form.Label>
                    <Form.Control type="file" multiple name="images" />
                </Form.Group>

                <Button variant="primary" type="submit">
                    Save
                </Button>
            </Form>
        </Container>
    );
}

export default CreateEstate