import About from "./About";
import Chocolates from "./Chocolates";
import ContactUs from "./ContactUs";
import Footer from "./Footer";
import Hero from "./Hero";
import Info from "./Info";
import Offer from "./Offer";

export default function Body() {
    return (
        <div className="main_body_content">
            <Hero />
            <About />
            <Chocolates />
            <Offer />
            <ContactUs />
            <Info />
            <Footer />
        </div>
    )
}