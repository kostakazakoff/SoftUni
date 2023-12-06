import { useNavigate } from "react-router-dom";
import api from "../api/Api";


const Logout = () => {
    const navigate = useNavigate();
    api.post('logout')
        .then((response) => console.log(response))
        // .then(navigate('/login'))
        .catch((err) => console.log(err));
}

export default Logout;