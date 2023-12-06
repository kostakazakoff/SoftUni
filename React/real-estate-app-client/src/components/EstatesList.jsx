import { useState, useEffect } from "react";
import EstateCard from "./EstateCard";
import api from "../api/helpers/Api";


const EstatesList = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        api.get('real-estates')
            .then(response => response.data)
            .then(state => setData(state.estates))
    }, []);


    return (
        <div className="container-xxl d-flex flex-wrap gap-3 mt-3">
            {data.map(estate => (
                <EstateCard
                    key={estate.id}
                    id={estate.id}
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