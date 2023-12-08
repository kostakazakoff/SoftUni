import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/helpers/Api";
import AuthContext from "../api/contexts/authContext";


const Logout = () => {
  const { setCredentials } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    setCredentials({})
    .then(navigate('/'));
  }, [])
}

export default Logout;
