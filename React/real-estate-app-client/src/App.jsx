import { useEffect, useState } from "react";
import { Routes, Route } from 'react-router-dom';

import AuthContext from "./api/contexts/authContext";

import Navigation from "./components/Navigation";
import Home from './components/Home';
import EstatesList from './components/EstatesList';
import EstateDetails from './components/EstateDetails';
import CreateEstate from "./components/CreateEstate";
import Login from "./components/Auth/Login";
import Logout from "./components/Auth/Logout";
import Footer from "./components/Footer";

import api from "./api/helpers/Api";
import Path from "./paths";
import Register from "./components/Auth/Register";


function App() {

  const [credentials, setCredentials] = useState({});

  useEffect(() => {
    localStorage.setItem('credentials', JSON.stringify(credentials));
  }, [credentials])

  useEffect(() => {
    const savedCredentials = JSON.parse(localStorage.getItem('credentials'));
    if (savedCredentials !== null) {
      setCredentials(state => ({...state, ...savedCredentials}));
    }
  }, [])

  useEffect(() => {
    api.get('user')
    .then(result => console.log('Current USER', result));
  }, [])

  console.log('Credentials: ', credentials)

  return (
    <>
      <AuthContext.Provider value={{
        user_id: credentials.user_id,
        email: credentials.email,
        jwt: credentials.jwt,
        isAuthenticated: !!credentials.jwt,
        setCredentials: setCredentials,
      }} >
        <Navigation credentials={credentials} />

        <Routes>
          <Route path={Path.LOGIN} element={<Login />} />
          <Route path={Path.LOGOUT} element={<Logout />} />
          <Route path={Path.REGISTER} element={<Register />} />

          <Route path={Path.HOME} element={<Home />} />
          <Route path={Path.ESTATES} element={<EstatesList />} />
          <Route path={Path.SHOW_ESTATE} element={<EstateDetails />} />
          <Route path={Path.CREATE_ESTATE} element={<CreateEstate />} />
        </Routes>

        {/* <Footer /> */}
      </AuthContext.Provider>
    </>
  )
}

export default App
