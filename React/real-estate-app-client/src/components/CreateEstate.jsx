import { Container } from "react-bootstrap";
import { fetchServer } from "../api/FetchServer";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const CreateEstate = () => {
    let [data, setData] = useState({});
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(1);

    useEffect(() => {
        fetchServer('list-categories')
            .then(data => setCategories(data))
            .catch(e => console.log(e));
    }, []);

    const SubmitHandler = (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('image', data.images);
        formData.append('text', JSON.stringify(data));
        console.log(formData.entries());
        fetchServer('real-estates/create', data, 'POST');
    }

    const handleData = (e) => {
        setData(state => ({ ...state, [e.target.name]: e.target.value }));
    }

    const handleImages = (e) => {
        setData(state => ({ ...state, 'images': e.target.files }));
    }
    console.log(data);

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setData(state => ({ ...state, 'category_id': Number(e.target.value) }));
    }


    return (
        <>
            <Container style={{ width: '30%', margin: '60px auto' }}>
                <Form id='creste' onSubmit={SubmitHandler} encType="multipart/form-data">

                    <Form.Group className="mb-3" controlId="name">
                        <Form.Label>Property name</Form.Label>
                        <Form.Control
                            type="text"
                            name="name"
                            value={data.name ? data.name : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="location">
                        <Form.Label>location</Form.Label>
                        <Form.Control
                            type="text"
                            name="location"
                            value={data.location ? data.location : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="description">
                        <Form.Label>description</Form.Label>
                        <Form.Control
                            type="text"
                            name="description"
                            value={data.description ? data.description : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="price">
                        <Form.Label>price</Form.Label>
                        <Form.Control
                            type="number"
                            name="price"
                            value={data.price ? data.price : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Currency</Form.Label>
                        <Form.Select value={data.currency ? data.currency : 'BGN'} onChange={handleData} name='currency'>
                            <option key='BGN' value='1'>BGN</option>
                            <option key='EUR' value='2'>EUR</option>
                            <option key='USD' value='3'>USD</option>
                        </Form.Select>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="latitude">
                        <Form.Label>latitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="latitude"
                            value={data.latitude ? data.latitude : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="longitude">
                        <Form.Label>longitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="longitude"
                            value={data.longitude ? data.longitude : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Category</Form.Label>
                        <Form.Select value={selectedCategory} onChange={handleCategoryChange} name='category_id'>
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
                            value={data.rooms ? data.rooms : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="arrive_hour">
                        <Form.Label>arrive_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="arrive_hour"
                            value={data.arrive_hour ? data.arrive_hour : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="leave_hour">
                        <Form.Label>leave_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="leave_hour"
                            value={data.leave_hour ? data.leave_hour : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="user_id">
                        <Form.Label>user_id</Form.Label>
                        <Form.Control
                            type="number"
                            name="user_id"
                            value={data.user_id ? data.user_id : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="images">
                        <Form.Label>images</Form.Label>
                        <Form.Control
                            type="file"
                            name="images"
                            multiple
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