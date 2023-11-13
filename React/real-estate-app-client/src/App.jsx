import Navigation from "./components/Navigation"
import Home from './components/Home'
import EstatesList from './components/EstatesList'
import EstateDetails from './components/EstateDetails'
import { Routes, Route } from 'react-router-dom';
import Footer from "./components/Footer";


function App() {
  return (
    <>
    
      <Navigation />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/estates" element={<EstatesList />} />
          <Route path="/estates/:id" element={<EstateDetails />} />
        </Routes>
      
      <Footer />
    </>
  )
}

export default App
