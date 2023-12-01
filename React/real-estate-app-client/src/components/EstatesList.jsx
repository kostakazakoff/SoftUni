import { useState, useEffect } from "react";
import EstateCard from "./EstateCard";
import { fetchServer } from "../api/FetchServer";


const EstatesList = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchServer('real-estates')
            .then(data => setData(data.estates))
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