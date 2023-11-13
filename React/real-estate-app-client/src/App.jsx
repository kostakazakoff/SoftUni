import Navigation from "./components/Navigation"
import Home from './components/Home'
import EstatesList from './components/EstatesList'
import EstateDetails from './components/EstateDetails'
import { Routes, Route } from 'react-router-dom';


function App() {

  return (
    <>
      <Navigation />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/estates" element={<EstatesList />} />
        <Route path="/estate-details" element={<EstateDetails />} />
      </Routes>
    </>
  )
}

export default App
