import AdvancedSearch from "./components/AdvancedSearch"
import Header from "./components/Header"
import Nav from "./components/Nav"
import Slider from "./components/Slider"

function App() {
  return (
      <>
        {/* Pre Loader */}
        <div id="aa-preloader-area">
          <div className="pulse" />
        </div>
        {/* SCROLL TOP BUTTON */}
        <a className="scrollToTop" href="#">
          <i className="fa fa-angle-double-up" />
        </a>
        {/* END SCROLL TOP BUTTON */}
        <Header />
        {/* Start menu section */}
        <Nav />
        {/* End menu section */}
        {/* Start slider  */}
        <Slider />
        {/* End slider  */}
        {/* Advance Search */}
        <AdvancedSearch />
        {/* / Advance Search */}
        {/* About us */}
        <section id="aa-about-us">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-about-us-area">
                  <div className="row">
                    <div className="col-md-5">
                      <div className="aa-about-us-left">
                        <img src="../../public/img/about-us.png" alt="image" />
                      </div>
                    </div>
                    <div className="col-md-7">
                      <div className="aa-about-us-right">
                        <div className="aa-title">
                          <h2>About Us</h2>
                          <span />
                        </div>
                        <p>
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                          Repellat ab dignissimos vitae maxime adipisci blanditiis
                          rerum quae quos! Id at rerum maxime modi fugit vero
                          corrupti, ad atque sit laborum ipsum sunt blanditiis
                          suscipit odio, aut nostrum assumenda nobis rem a maiores
                          temporibus non commodi laboriosam, doloremque expedita!
                          Corporis, provident?
                        </p>
                        <ul>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Esse, blanditiis.
                          </li>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                          </li>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Quia.
                          </li>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Esse, blanditiis.
                          </li>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                          </li>
                          <li>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Quia.
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / About us */}
        {/* Latest property */}
        <section id="aa-latest-property">
          <div className="container">
            <div className="aa-latest-property-area">
              <div className="aa-title">
                <h2>Latest Properties</h2>
                <span />
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum sit ea
                  nobis quae vero voluptatibus.
                </p>
              </div>
              <div className="aa-latest-properties-content">
                <div className="row">
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/1.jpg" alt="img" />
                      </a>
                      <div className="aa-tag for-sale">For Sale</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$35000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/2.jpg" alt="img" />
                      </a>
                      <div className="aa-tag for-rent">For Rent</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$11000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/3.jpg" alt="img" />
                      </a>
                      <div className="aa-tag sold-out">Sold Out</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$15000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/4.jpg" alt="img" />
                      </a>
                      <div className="aa-tag for-sale">For Sale</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$35000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/5.jpg" alt="img" />
                      </a>
                      <div className="aa-tag sold-out">Sold Out</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$11000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                  <div className="col-md-4">
                    <article className="aa-properties-item">
                      <a href="#" className="aa-properties-item-img">
                        <img src="../../public/img/item/6.jpg" alt="img" />
                      </a>
                      <div className="aa-tag for-rent">For Rent</div>
                      <div className="aa-properties-item-content">
                        <div className="aa-properties-info">
                          <span>5 Rooms</span>
                          <span>2 Beds</span>
                          <span>3 Baths</span>
                          <span>1100 SQ FT</span>
                        </div>
                        <div className="aa-properties-about">
                          <h3>
                            <a href="#">Appartment Title</a>
                          </h3>
                          <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Enim molestiae vero ducimus quibusdam odit vitae.
                          </p>
                        </div>
                        <div className="aa-properties-detial">
                          <span className="aa-price">$15000</span>
                          <a href="#" className="aa-secondary-btn">
                            View Details
                          </a>
                        </div>
                      </div>
                    </article>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Latest property */}
        {/* Service section */}
        <section id="aa-service">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-service-area">
                  <div className="aa-title">
                    <h2>Our Service</h2>
                    <span />
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum
                      sit ea nobis quae vero voluptatibus.
                    </p>
                  </div>
                  {/* service content */}
                  <div className="aa-service-content">
                    <div className="row">
                      <div className="col-md-3">
                        <div className="aa-single-service">
                          <div className="aa-service-icon">
                            <span className="fa fa-home" />
                          </div>
                          <div className="aa-single-service-content">
                            <h4>
                              <a href="#">Property Sale</a>
                            </h4>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Iusto repellendus quasi asperiores itaque dolorem
                              at.
                            </p>
                          </div>
                        </div>
                      </div>
                      <div className="col-md-3">
                        <div className="aa-single-service">
                          <div className="aa-service-icon">
                            <span className="fa fa-check" />
                          </div>
                          <div className="aa-single-service-content">
                            <h4>
                              <a href="#">Property Rent</a>
                            </h4>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Iusto repellendus quasi asperiores itaque dolorem
                              at.
                            </p>
                          </div>
                        </div>
                      </div>
                      <div className="col-md-3">
                        <div className="aa-single-service">
                          <div className="aa-service-icon">
                            <span className="fa fa-crosshairs" />
                          </div>
                          <div className="aa-single-service-content">
                            <h4>
                              <a href="#">Property Development</a>
                            </h4>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Iusto repellendus quasi asperiores itaque dolorem
                              at.
                            </p>
                          </div>
                        </div>
                      </div>
                      <div className="col-md-3">
                        <div className="aa-single-service">
                          <div className="aa-service-icon">
                            <span className="fa fa-bar-chart-o" />
                          </div>
                          <div className="aa-single-service-content">
                            <h4>
                              <a href="#">Market Analysis</a>
                            </h4>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Iusto repellendus quasi asperiores itaque dolorem
                              at.
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Service section */}
        {/* Promo Banner Section */}
        <section id="aa-promo-banner">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-promo-banner-area">
                  <h3>Find Your Best Property</h3>
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Doloribus, ex illum corporis quibusdam numquam quisquam optio
                    explicabo. Officiis odit quia odio dignissimos eius repellat id!
                  </p>
                  <a href="#" className="aa-view-btn">
                    View Details
                  </a>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Promo Banner Section */}
        {/* Our Agent Section*/}
        <section id="aa-agents">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-agents-area">
                  <div className="aa-title">
                    <h2>Our Agents</h2>
                    <span />
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum
                      sit ea nobis quae vero voluptatibus.
                    </p>
                  </div>
                  {/* agents content */}
                  <div className="aa-agents-content">
                    <ul className="aa-agents-slider">
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-1.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Philip Smith</a>
                            </h4>
                            <span>Top Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-5.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Adam Barney</a>
                            </h4>
                            <span>Expert Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-3.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Paul Walker</a>
                            </h4>
                            <span>Director</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-4.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">John Smith</a>
                            </h4>
                            <span>Jr. Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-1.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Philip Smith</a>
                            </h4>
                            <span>Top Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-5.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Adam Barney</a>
                            </h4>
                            <span>Expert Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-3.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">Paul Walker</a>
                            </h4>
                            <span>Director</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-single-agents">
                          <div className="aa-agents-img">
                            <img
                              src="../../public/img/agents/agent-4.png"
                              alt="agent member image"
                            />
                          </div>
                          <div className="aa-agetns-info">
                            <h4>
                              <a href="#">John Smith</a>
                            </h4>
                            <span>Jr. Agent</span>
                            <div className="aa-agent-social">
                              <a href="#">
                                <i className="fa fa-facebook" />
                              </a>
                              <a href="#">
                                <i className="fa fa-twitter" />
                              </a>
                              <a href="#">
                                <i className="fa fa-linkedin" />
                              </a>
                              <a href="#">
                                <i className="fa fa-google-plus" />
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Our Agent Section*/}
        {/* Client Testimonial */}
        <section id="aa-client-testimonial">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-client-testimonial-area">
                  <div className="aa-title">
                    <h2>What Client Say</h2>
                    <span />
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Necessitatibus eaque quas debitis animi ipsum, veritatis!
                    </p>
                  </div>
                  {/* testimonial content */}
                  <div className="aa-testimonial-content">
                    {/* testimonial slider */}
                    <ul className="aa-testimonial-slider">
                      <li>
                        <div className="aa-testimonial-single">
                          <div className="aa-testimonial-img">
                            <img src="../../public/img/testimonial-1.png" alt="testimonial img" />
                          </div>
                          <div className="aa-testimonial-info">
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Cupiditate consequuntur ducimus cumque iure modi
                              nesciunt recusandae eligendi vitae voluptatibus,
                              voluptatum tempore, ipsum nisi perspiciatis. Rerum
                              nesciunt fuga ab natus, dolorem?
                            </p>
                          </div>
                          <div className="aa-testimonial-bio">
                            <p>David Muller</p>
                            <span>Web Designer</span>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-testimonial-single">
                          <div className="aa-testimonial-img">
                            <img src="../../public/img/testimonial-3.png" alt="testimonial img" />
                          </div>
                          <div className="aa-testimonial-info">
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Cupiditate consequuntur ducimus cumque iure modi
                              nesciunt recusandae eligendi vitae voluptatibus,
                              voluptatum tempore, ipsum nisi perspiciatis. Rerum
                              nesciunt fuga ab natus, dolorem?
                            </p>
                          </div>
                          <div className="aa-testimonial-bio">
                            <p>David Muller</p>
                            <span>Web Designer</span>
                          </div>
                        </div>
                      </li>
                      <li>
                        <div className="aa-testimonial-single">
                          <div className="aa-testimonial-img">
                            <img src="../../public/img/testimonial-2.png" alt="testimonial img" />
                          </div>
                          <div className="aa-testimonial-info">
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Cupiditate consequuntur ducimus cumque iure modi
                              nesciunt recusandae eligendi vitae voluptatibus,
                              voluptatum tempore, ipsum nisi perspiciatis. Rerum
                              nesciunt fuga ab natus, dolorem?
                            </p>
                          </div>
                          <div className="aa-testimonial-bio">
                            <p>David Muller</p>
                            <span>Web Designer</span>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* Client Testimonial */}
        {/* Client brand */}
        <section id="aa-client-brand">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-client-brand-area">
                  <ul className="aa-client-brand-slider">
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-1.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-2.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-3.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-5.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-4.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-1.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-2.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-3.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-5.png" alt="brand image" />
                      </div>
                    </li>
                    <li>
                      <div className="aa-client-single-brand">
                        <img src="../../public/img/client-brand-4.png" alt="brand image" />
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Client brand */}
        {/* Latest blog */}
        <section id="aa-latest-blog">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-latest-blog-area">
                  <div className="aa-title">
                    <h2>Latest News</h2>
                    <span />
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe
                      magni, est harum repellendus. Accusantium, nostrum!
                    </p>
                  </div>
                  <div className="aa-latest-blog-content">
                    <div className="row">
                      {/* start single blog */}
                      <div className="col-md-4">
                        <article className="aa-blog-single">
                          <figure className="aa-blog-img">
                            <a href="#">
                              <img src="../../public/img/blog-img-1.jpg" alt="img" />
                            </a>
                            <span className="aa-date-tag">15 April, 16</span>
                          </figure>
                          <div className="aa-blog-single-content">
                            <h3>
                              <a href="#">Lorem ipsum dolor sit amet, consectetur.</a>
                            </h3>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Optio est quaerat magnam exercitationem voluptas,
                              voluptatem sed quam ab laborum voluptatum tempore
                              dolores itaque, molestias vitae.
                            </p>
                            <div className="aa-blog-single-bottom">
                              <a href="#" className="aa-blog-author">
                                <i className="fa fa-user" /> Admin
                              </a>
                              <a href="#" className="aa-blog-comments">
                                <i className="fa fa-comment-o" />6
                              </a>
                            </div>
                          </div>
                        </article>
                      </div>
                      {/* start single blog */}
                      <div className="col-md-4">
                        <article className="aa-blog-single">
                          <figure className="aa-blog-img">
                            <a href="#">
                              <img src="../../public/img/blog-img-2.jpg" alt="img" />
                            </a>
                            <span className="aa-date-tag">15 April, 16</span>
                          </figure>
                          <div className="aa-blog-single-content">
                            <h3>
                              <a href="#">Lorem ipsum dolor sit amet, consectetur.</a>
                            </h3>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Optio est quaerat magnam exercitationem voluptas,
                              voluptatem sed quam ab laborum voluptatum tempore
                              dolores itaque, molestias vitae.
                            </p>
                            <div className="aa-blog-single-bottom">
                              <a href="#" className="aa-blog-author">
                                <i className="fa fa-user" /> Admin
                              </a>
                              <a href="#" className="aa-blog-comments">
                                <i className="fa fa-comment-o" />6
                              </a>
                            </div>
                          </div>
                        </article>
                      </div>
                      {/* start single blog */}
                      <div className="col-md-4">
                        <article className="aa-blog-single">
                          <figure className="aa-blog-img">
                            <a href="#">
                              <img src="../../public/img/blog-img-3.jpg" alt="img" />
                            </a>
                            <span className="aa-date-tag">15 April, 16</span>
                          </figure>
                          <div className="aa-blog-single-content">
                            <h3>
                              <a href="#">Lorem ipsum dolor sit amet, consectetur.</a>
                            </h3>
                            <p>
                              Lorem ipsum dolor sit amet, consectetur adipisicing
                              elit. Optio est quaerat magnam exercitationem voluptas,
                              voluptatem sed quam ab laborum voluptatum tempore
                              dolores itaque, molestias vitae.
                            </p>
                            <div className="aa-blog-single-bottom">
                              <a href="#" className="aa-blog-author">
                                <i className="fa fa-user" /> Admin
                              </a>
                              <a href="#" className="aa-blog-comments">
                                <i className="fa fa-comment-o" />6
                              </a>
                            </div>
                          </div>
                        </article>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* / Latest blog */}
        {/* Footer */}
        <footer id="aa-footer">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="aa-footer-area">
                  <div className="row">
                    <div className="col-md-3 col-sm-6 col-xs-12">
                      <div className="aa-footer-left">
                        <p>
                          Designed by{" "}
                          <a rel="nofollow" href="http://www.markups.io/">
                            MarkUps.io
                          </a>
                        </p>
                      </div>
                    </div>
                    <div className="col-md-3 col-sm-6 col-xs-12">
                      <div className="aa-footer-middle">
                        <a href="#">
                          <i className="fa fa-facebook" />
                        </a>
                        <a href="#">
                          <i className="fa fa-twitter" />
                        </a>
                        <a href="#">
                          <i className="fa fa-google-plus" />
                        </a>
                        <a href="#">
                          <i className="fa fa-youtube" />
                        </a>
                      </div>
                    </div>
                    <div className="col-md-6 col-sm-12 col-xs-12">
                      <div className="aa-footer-right">
                        <a href="#">Home</a>
                        <a href="#">Support</a>
                        <a href="#">License</a>
                        <a href="#">FAQ</a>
                        <a href="#">Privacy &amp; Term</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </footer>
        {/* / Footer */}
      </>
  )
}

export default App
