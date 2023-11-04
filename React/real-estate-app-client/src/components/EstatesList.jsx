import { useState, useEffect } from "react";
import EstateCard from "./EstateCard";
import { getAll } from "../api/FetchServer";

const EstatesList = () => {
    const [data, setData] = useState([]);

    console.log(data);

    useEffect(() => {
        getAll('real_estates', 'GET')
            .then(response => setData(response));
    }, []);

    return (
        <div className="container-xxl d-flex flex-wrap gap-3 mt-3">
            {data.map(estate => (
            <EstateCard
                key={estate.id}
                name={estate.name}
                description={estate.description}
            />
            ))}
        </div>
    )
}

export default EstatesList