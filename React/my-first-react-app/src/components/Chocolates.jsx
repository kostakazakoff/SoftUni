import ChocolateBox from "./ChocolateBox";

export default function Chocolates() {
    return (
        <section className="chocolate_section ">
            <div className="container">
                <div className="heading_container">
                    <h2>Our chocolate products</h2>
                    <p>
                        Many desktop publishing packages and web pagend web page editors now
                        use Lorem Ipsum as their
                    </p>
                </div>
            </div>
            <div className="container">
                <div className="chocolate_container">
                    <ChocolateBox />  
                </div>
            </div>
        </section>
    )
}