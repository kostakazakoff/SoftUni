export default function Slider() {
    return (
        <section id="aa-slider">
            <div className="aa-slider-area">
                {/* Top slider */}
                <div className="aa-top-slider">
                    {/* Top slider single slide */}
                    <div className="aa-top-slider-single">
                        <img src="./public/img/interior2.jpg" alt="img" />
                        {/* Top slider content */}
                        <div className="aa-top-slider-content">
                            <span className="aa-top-slider-catg">Duplex</span>
                            <h2 className="aa-top-slider-title">1560 Square Feet</h2>
                            <p className="aa-top-slider-location">
                                <i className="fa fa-map-marker" />
                                South Beach, Miami (USA)
                            </p>
                            <span className="aa-top-slider-off">30% OFF</span>
                            <p className="aa-top-slider-price">$460,000</p>
                            <a href="#" className="aa-top-slider-btn">
                                Read More <span className="fa fa-angle-double-right" />
                            </a>
                        </div>
                        {/* / Top slider content */}
                    </div>
                </div>
            </div>
        </section>
    )
}