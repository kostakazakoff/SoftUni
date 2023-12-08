import { Container } from "react-bootstrap";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";
import axios from "axios";
import api from "../api/helpers/Api";
import { useNavigate } from "react-router-dom";

const CreateEstate = () => {
    let [formData, setFormData] = useState({ 'currency': 'BGN', 'category_id': '1' });
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(1);

    const navigate = useNavigate();

    axios.defaults.withCredentials = true;
    axios.defaults.withXSRFToken = true;

    useEffect(() => {
        api.get('list-categories')
            .then(categories => categories.data)
            .then(result => setCategories(result))
            .catch(e => console.log(e));
    }, []);

    const SubmitHandler = (e) => {
        e.preventDefault();

        api.get('user')
            // .then(response => console.log(response.data.id))
            .then(response => response.data.id)
            .then(user_id => setFormData(state => ({ ...state, 'user_id': user_id })))
            .then(
                api.post('real-estates/create', { ...formData })
                    .catch(err => console.error(err))
            )
            // .then(navigate('/estates'))
            .catch(err => console.error(err));
    }

    const handleData = (e) => {
        setFormData(state => ({ ...state, [e.target.name]: e.target.value }));
    }

    const handleImages = (e) => {
        setFormData(state => ({ ...state, 'images': e.target.files }));
    }

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setFormData(state => ({ ...state, 'category_id': Number(e.target.value) }));
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
                            value={formData.name ? formData.name : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="location">
                        <Form.Label>location</Form.Label>
                        <Form.Control
                            type="text"
                            name="location"
                            value={formData.location ? formData.location : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="description">
                        <Form.Label>description</Form.Label>
                        <Form.Control
                            type="text"
                            name="description"
                            value={formData.description ? formData.description : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="price">
                        <Form.Label>price</Form.Label>
                        <Form.Control
                            type="number"
                            name="price"
                            value={formData.price ? formData.price : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Currency</Form.Label>
                        <Form.Select value={formData.currency ? formData.currency : 'BGN'} onChange={handleData} name='currency'>
                            <option key='BGN' value='BGN'>BGN</option>
                            <option key='EUR' value='EUR'>EUR</option>
                            <option key='USD' value='USD'>USD</option>
                        </Form.Select>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="latitude">
                        <Form.Label>latitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="latitude"
                            value={formData.latitude ? formData.latitude : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="longitude">
                        <Form.Label>longitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="longitude"
                            value={formData.longitude ? formData.longitude : ''}
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
                            value={formData.rooms ? formData.rooms : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="arrive_hour">
                        <Form.Label>arrive_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="arrive_hour"
                            value={formData.arrive_hour ? formData.arrive_hour : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="leave_hour">
                        <Form.Label>leave_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="leave_hour"
                            value={formData.leave_hour ? formData.leave_hour : ''}
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