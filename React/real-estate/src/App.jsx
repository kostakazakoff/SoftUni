import AboutUs from "./components/AboutUs"
import AdvancedSearch from "./components/AdvancedSearch"
import Banner from "./components/Banner"
import Blogs from "./components/Blogs"
import ClientBrand from "./components/ClientBrand"
import ClientTestimonial from "./components/ClientTestimonial"
import Footer from "./components/Footer"
import Header from "./components/Header"
import Nav from "./components/Nav"
import Preloader from "./components/PreloaderScrollBtn"
import Property from "./components/Property"
import Service from "./components/Service"
import Slider from "./components/Slider"
import Team from "./components/Team"

function App() {
  return (
      <>
        <Preloader />
        <Header />
        <Nav />
        <Slider />
        <AdvancedSearch />
        <AboutUs />
        <Property />
        <Service />
        <Banner />
        <Team />
        <ClientTestimonial/>
        <ClientBrand />
        <Blogs />
        <Footer />
      </>
  )
}

export default App
