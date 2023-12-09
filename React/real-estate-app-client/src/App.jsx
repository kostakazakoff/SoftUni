import { Routes, Route } from 'react-router-dom';

import { AuthProvider } from "./api/contexts/authContext";

import Navigation from "./components/Navigation";
import Home from './components/Home';
import EstatesList from './components/EstatesList';
import EstateDetails from './components/EstateDetails';
import CreateEstate from "./components/CreateEstate";
import Login from "./components/Auth/Login";
import Logout from "./components/Auth/Logout";
import Footer from "./components/Footer";

import Path from "./paths";
import Register from "./components/Auth/Register";


function App() {

  return (
    <>
      <AuthProvider>

        <Navigation/>

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
        
      </AuthProvider>
    </>
  )
}

export default App
