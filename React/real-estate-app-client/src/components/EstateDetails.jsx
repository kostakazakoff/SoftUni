/* eslint-disable react/prop-types */
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchServer } from "../api/FetchServer";
import { Figure } from "react-bootstrap";

const EstateDetails = () => {
    const { id } = useParams();
    const [data, setData] = useState({});

    useEffect(() => {
        fetchServer(`real-estates/${id}`)
            .then(result => setData(result));
    }, [id]);

    return (
        <Figure>
            <Figure.Image
                width={171}
                height={180}
                alt="171x180"
                src="https://imageio.forbes.com/specials-images/imageserve/61cdd9ec2bbdedb659077751/Neutral-living-color-corrected/960x0.jpg?format=jpg&width=1440"
            />
            <Figure.Caption>
                <h2>{ data.name }</h2>
                <p>{ data.description }</p>
                <p>Rooms: { data.rooms }</p>
                <h4>Price: { data.price } { data.currency }</h4>
            </Figure.Caption>
        </Figure>
    );

}

export default EstateDetails