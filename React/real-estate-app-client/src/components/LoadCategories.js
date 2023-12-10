import { useState, useEffect } from "react";
import api from "../api/helpers/Api";
import Path from "../paths";

const LoadCategories = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        api.get(Path.CATEGORIES)
            .then(response => response.data)
            .then(loadedCategories => setCategories([...loadedCategories]))
            .catch(e => console.log(e));
    }, []);

    return categories;
}

export default LoadCategories;