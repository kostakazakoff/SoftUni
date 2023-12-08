import { useEffect, useState } from "react";
import { Routes, Route } from 'react-router-dom';

import AuthContext from "./api/contexts/authContext";

import Navigation from "./components/Navigation";
import Home from './components/Home';
import EstatesList from './components/EstatesList';
import EstateDetails from './components/EstateDetails';
import CreateEstate from "./components/CreateEstate";
import Login from "./components/Login";
import Logout from "./components/Logout";
import Footer from "./components/Footer";

import api from "./api/helpers/Api";


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

  return (
    <>
      <AuthContext.Provider value={{
        email: credentials.email,
        isAuthenticated: !!credentials.email,
        setCredentials: setCredentials,
      }} >
        <Navigation credentials={credentials} />

        <Routes>
          <Route path='/login' element={<Login />} />
          <Route path='/logout' element={<Logout />} />

          <Route path="/" element={<Home />} />
          <Route path="/estates" element={<EstatesList />} />
          <Route path="/estates/:id" element={<EstateDetails />} />
          <Route path="/estates/create" element={<CreateEstate />} />
        </Routes>

        {/* <Footer /> */}
      </AuthContext.Provider>
    </>
  )
}

export default App
