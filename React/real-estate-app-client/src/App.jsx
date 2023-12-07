import { useState } from "react";
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


function App() {

  const [credentials, setCredentials] = useState({});

  console.log(`User credentials: ${{ credentials }}`);

  return (
    <>
      <AuthContext.Provider value={{
        credentials: credentials,
        setCredentials: setCredentials,
      }} >
        <Navigation />

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
