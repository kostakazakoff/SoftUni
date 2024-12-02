/* eslint-disable react/prop-types */
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Figure } from "react-bootstrap";
import api from "../api/helpers/Api";

const EstateDetails = () => {
    const { id } = useParams();
    const [estate, setEstate] = useState({});

    useEffect(() => {
        api.get(`real-estates/${id}`)
            .then(result => result.data.estate)
            .then(result => setEstate(result))
            .catch(e => console.log(e));
    }, [id]);

    return (
        <>
            <Figure>
                <Figure.Image
                    width={600}
                    height={800}
                    alt="171x180"
                    src={estate.images && estate.images[0].url}
                />
                <Figure.Caption>
                    <h2>{estate.name}</h2>
                    <p>{estate.description}</p>
                    <p>Rooms: {estate.rooms}</p>
                    <h4>Price: {estate.price}</h4>
                </Figure.Caption>
            </Figure>
        </>
    );

}

export default EstateDetails