import { useState, useEffect } from "react";
import EstateCard from "./EstateCard";
import api from "../api/helpers/Api";


const EstatesList = () => {
    const [estates, setEstates] = useState([]);

    useEffect(() => {
        api.get('real-estates')
            .then(response => response.data.estates)
            .then(result => setEstates(result))
            .catch(err => console.log(err));
    }, []);

    return (
        <div className="container-xxl d-flex flex-wrap gap-3 mt-3 justify-content-center">
            {estates.map(estate => (
                <EstateCard
                    key={estate.id}
                    id={estate.id}
                    thumb={estate.thumb}
                    name={estate.name}
                    description={estate.description}
                    rooms={estate.rooms}
                    price={estate.price}
                    currency='EUR'
                />
            ))}
        </div>
    )
}

export default EstatesList