import { Container } from "react-bootstrap";
import { fetchServer } from "../api/FetchServer";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const CreateEstate = () => {
    let [data, setData] = useState('');
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetchServer('list-categories')
            .then(data => setCategories(data))
            .catch(e => console.log(e));
    }, []);

    const SubmitHandler = (e) => {
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

    const handleData = (e) => {
        e.target.type === 'number'
            ? data[e.target.name] = Number(e.target.value)
            : data[e.target.name] = e.target.value;

        setData(data);
    }

    const handleImages = (e) => {
        data[e.target.name] = e.target.files

        setData(data);
    }

    const handleSelected = (e) => {
        data[e.target.name] = Number(e.target.value)

        setData(data);
    }

    return (
        <>
            <Container>
                <Form id='creste' onSubmit={SubmitHandler} encType="multipart/form-data" onFocus={transformDataToObject}>

                    <Form.Group className="mb-3" controlId="name">
                        <Form.Label>Property name</Form.Label>
                        <Form.Control
                            type="text"
                            name="name"
                            value={data.name}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="location">
                        <Form.Label>location</Form.Label>
                        <Form.Control
                            type="text"
                            name="location"
                            value={data.location}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="description">
                        <Form.Label>description</Form.Label>
                        <Form.Control
                            type="text"
                            name="description"
                            value={data.description}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="price">
                        <Form.Label>price</Form.Label>
                        <Form.Control
                            type="number"
                            name="price"
                            value={data.price}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="currency">
                        <Form.Label>Currency</Form.Label>
                        <Form.Control
                            type="text"
                            name="currency"
                            value={data.currency}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="latitude">
                        <Form.Label>latitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="latitude"
                            value={data.latitude}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="longitude">
                        <Form.Label>longitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="longitude"
                            value={data.longitude}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Category</Form.Label>
                        <Form.Select value={data.categories} onChange={handleSelected} name='category_id'>
                            {categories.map((category) => (
                                <option key={category.id} value={category.id}>
                                    {category.name}
                                </option>
                            ))}
                        </Form.Select>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="rooms">
                        <Form.Label>rooms</Form.Label>
                        <Form.Control
                            type="number"
                            name="rooms"
                            value={data.rooms}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="arrive_hour">
                        <Form.Label>arrive_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="arrive_hour"
                            value={data.arrive_hour}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="leave_hour">
                        <Form.Label>leave_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="leave_hour"
                            value={data.leave_hour}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="user_id">
                        <Form.Label>user_id</Form.Label>
                        <Form.Control
                            type="number"
                            name="user_id"
                            value={data.user_id}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="images">
                        <Form.Label>images</Form.Label>
                        <Form.Control
                            type="file"
                            name="images"
                            multiple
                            value={data.images}
                            onChange={handleImages}
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