import { useState, useEffect } from "react";
import EstateCard from "./EstateCard";
import { getAll } from "../api/FetchServer";


const EstatesList = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        getAll('real_estates')
            .then(data => setData(data))
    }, []);


    return (
        <div className="container-xxl d-flex flex-wrap gap-3 mt-3">
            {data.map(estate => (
                <EstateCard
                    key={estate.id}
                    name={estate.name}
                    description={estate.description}
                    rooms={estate.rooms}
                    price={estate.price}
                />
            ))}
        </div>

    )
}

export default EstatesList