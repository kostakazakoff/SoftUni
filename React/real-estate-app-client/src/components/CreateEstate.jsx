import { Container } from "react-bootstrap";
import { fetchServer } from "../api/FetchServer";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const CreateEstate = () => {
    let [data, setData] = useState('');

    const CreateEstateSubmitHandler = (e) => {
        e.preventDefault();

        console.log(data);

        fetchServer('real-estates/create', data, 'POST');
    }

    const transformDataToObject = () => {
        if (data === '') {
            data = {};
            setData(data);
        }
    }

    const handleInputData = (e) => {
        e.target.type === 'number'
            ? data[e.target.name] = Number(e.target.value)
            : data[e.target.name] = e.target.value

        setData(data);
    }

    const handleInputImages = (e) => {
        data[e.target.name] = e.target.files
    }

    return (
        <>
            <Container>
                <Form id='creste' onSubmit={CreateEstateSubmitHandler} encType="multipart/form-data" onFocus={transformDataToObject}>

                    <Form.Group className="mb-3" controlId="name">
                        <Form.Label>Property name</Form.Label>
                        <Form.Control
                            type="text"
                            name="name"
                            value={data.name}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="location">
                        <Form.Label>location</Form.Label>
                        <Form.Control
                            type="text"
                            name="location"
                            value={data.location}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="description">
                        <Form.Label>description</Form.Label>
                        <Form.Control
                            type="text"
                            name="description"
                            value={data.description}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="price">
                        <Form.Label>price</Form.Label>
                        <Form.Control
                            type="number"
                            name="price"
                            value={data.price}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="currency">
                        <Form.Label>Currency</Form.Label>
                        <Form.Control
                            type="text"
                            name="currency"
                            value={data.currency}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="latitude">
                        <Form.Label>latitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="latitude"
                            value={data.latitude}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="longitude">
                        <Form.Label>longitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="longitude"
                            value={data.longitude}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="category_id">
                        <Form.Label>category_id</Form.Label>
                        <Form.Control
                            type="number"
                            name="category_id"
                            value={data.category_id}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="rooms">
                        <Form.Label>rooms</Form.Label>
                        <Form.Control
                            type="number"
                            name="rooms"
                            value={data.rooms}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="arrive_hour">
                        <Form.Label>arrive_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="arrive_hour"
                            value={data.arrive_hour}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="leave_hour">
                        <Form.Label>leave_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="leave_hour"
                            value={data.leave_hour}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="user_id">
                        <Form.Label>user_id</Form.Label>
                        <Form.Control
                            type="number"
                            name="user_id"
                            value={data.user_id}
                            onChange={handleInputData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="images">
                        <Form.Label>images</Form.Label>
                        <Form.Control
                            type="file"
                            name="images"
                            multiple
                            value={data.images}
                            onChange={handleInputImages}
                        />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Save
                    </Button>

                </Form>
            </Container>
        </>

    );
}

export default CreateEstate