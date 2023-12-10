import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";

import { Container } from "react-bootstrap";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import api from "../api/helpers/Api";
import AuthContext from "../api/contexts/authContext";
import CategoriesContext from '../api/contexts/CategoriesContext';

const CreateEstate = () => {
    let [estateData, setEstateData] = useState({ 'currency': 'BGN', 'category_id': '1' });
    const categories = useContext(CategoriesContext);
    const [selectedCategory, setSelectedCategory] = useState(1);

    const { user_id } = useContext(AuthContext);

    const navigate = useNavigate();

    const SubmitHandler = (e) => {
        e.preventDefault();

        api.post('real-estates/create', { ...estateData })
        .then(navigate('/estates'))
            .catch(err => console.error(err));
    }

    const handleData = (e) => {
        setEstateData(state => ({
            ...state,
            [e.target.name]: e.target.value,
            'user_id': user_id
        }));
    }

    const handleImages = (e) => {
        setEstateData(state => ({ ...state, 'images': e.target.files }));
    }

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setEstateData(state => ({ ...state, 'category_id': Number(e.target.value) }));
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
                            value={estateData.name ? estateData.name : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="location">
                        <Form.Label>location</Form.Label>
                        <Form.Control
                            type="text"
                            name="location"
                            value={estateData.location ? estateData.location : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="description">
                        <Form.Label>description</Form.Label>
                        <Form.Control
                            type="text"
                            name="description"
                            value={estateData.description ? estateData.description : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="price">
                        <Form.Label>price</Form.Label>
                        <Form.Control
                            type="number"
                            name="price"
                            value={estateData.price ? estateData.price : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Currency</Form.Label>
                        <Form.Select value={estateData.currency ? estateData.currency : 'BGN'} onChange={handleData} name='currency'>
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
                            value={estateData.latitude ? estateData.latitude : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="longitude">
                        <Form.Label>longitude</Form.Label>
                        <Form.Control
                            type="text"
                            name="longitude"
                            value={estateData.longitude ? estateData.longitude : ''}
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
                            value={estateData.rooms ? estateData.rooms : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="arrive_hour">
                        <Form.Label>arrive_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="arrive_hour"
                            value={estateData.arrive_hour ? estateData.arrive_hour : ''}
                            onChange={handleData}
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="leave_hour">
                        <Form.Label>leave_hour</Form.Label>
                        <Form.Control
                            type="text"
                            name="leave_hour"
                            value={estateData.leave_hour ? estateData.leave_hour : ''}
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