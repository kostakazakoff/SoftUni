import Navigation from "./components/Navigation"
import Home from './components/Home'
import EstatesList from './components/EstatesList'
import EstateDetails from './components/EstateDetails'
import { Routes, Route } from 'react-router-dom';
import Footer from "./components/Footer";
import CreateEstate from "./components/CreateEstate";


function App() {
  return (
    <>

      <Navigation />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/estates" element={<EstatesList />} />
        <Route path="/estates/:id" element={<EstateDetails />} />
        <Route path="/estates/create" element={<CreateEstate />} />
      </Routes>

      {/* <Footer /> */}
    </>
  )
}

export default App
