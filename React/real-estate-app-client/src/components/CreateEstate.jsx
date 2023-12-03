import { Container } from "react-bootstrap";
import { fetchServer } from "../api/FetchServer";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const CreateEstate = () => {
    let [data, setData] = useState({
        'user_id': '',
        'name': '',
        'location': '',
        'description': '',
        'price': '',
        'currency': '',
        'latitude': '',
        'longitude': '',
        'category_id': '1',
        'rooms': '',
        'arrive_hour': '',
        'leave_hour': '',
        'images': '',
    });
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
        formData.append('image', Array.from(data.images));
        formData.append('text', data.text);
        console.log(formData.entries());
        fetchServer('real-estates/create', data, 'POST');

        // console.log(Array.from(e.target.images.files));


        // const myHeaders = new Headers();
        // myHeaders.append("Accept", "application/json");

        // const formdata = new FormData();
        // formdata.append("user_id", "123");
        // formdata.append("name", "Гълъбец център");
        // formdata.append("location", "Galabetz, Nesebar, Bulgaria");
        // formdata.append("description", "Хари");
        // formdata.append("price", "0");
        // formdata.append("currency", "BGN");
        // formdata.append("category_id", "2");
        // formdata.append("rooms", "1");
        // formdata.append("latitude", "42.772129");
        // formdata.append("longitude", "27.529766");
        // formdata.append("arrive_hour", "14:00:00");
        // formdata.append("leave_hour", "11:00:00");
        // formdata.append("images", Array.from(e.target.images.files)[0]);

        // const requestOptions = {
        //     method: 'POST',
        //     headers: myHeaders,
        //     body: formdata,
        // };

        // fetch("http://localhost:8000/api/real-estates/create", requestOptions)
        //     .then(response => response.text())
        //     .then(result => console.log(result))
        //     .catch(error => console.log('error', error));
    }

    const handleData = (e) => {
        // e.target.type === 'number'
        //     ? setData(data => ({ ...data, [e.target.name]: Number(e.target.value) }))
        setData(data => ({ ...data, [e.target.name]: e.target.value }));
    }

    const handleImages = (e) => {
        setData(data => ({ ...data, 'images': e.target.files }));
    }
    console.log(data);

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setData(data => ({ ...data, 'category_id': Number(e.target.value) }));
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
                            // value={data.images}
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