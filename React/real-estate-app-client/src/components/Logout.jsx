import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/helpers/Api";
import AuthContext from "../api/contexts/authContext";

import Cookies from 'js-cookie';


const Logout = () => {
  const { setCredentials } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    api.post('logout')
    .then(setCredentials({}))
    .then(navigate('/'))
    .catch(err => console.log(err));
  }, [])
}

export default Logout;
