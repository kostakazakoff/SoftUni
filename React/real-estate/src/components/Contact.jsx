import Footer from "./Footer";

export default function Contact() {
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
            {/* Start header section */}
            <header id="aa-header">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="aa-header-area">
                                <div className="row">
                                    <div className="col-md-6 col-sm-6 col-xs-6">
                                        <div className="aa-header-left">
                                            <div className="aa-telephone-no">
                                                <span className="fa fa-phone" />
                                                1-900-523-3564
                                            </div>
                                            <div className="aa-email hidden-xs">
                                                <span className="fa fa-envelope-o" /> info@markups.com
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6 col-sm-6 col-xs-6">
                                        <div className="aa-header-right">
                                            <a href="register.html" className="aa-register">
                                                Register
                                            </a>
                                            <a href="signin.html" className="aa-login">
                                                Login
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            {/* End header section */}
            {/* Start menu section */}
            <section id="aa-menu-area">
                <nav className="navbar navbar-default main-navbar" role="navigation">
                    <div className="container">
                        <div className="navbar-header">
                            {/* FOR MOBILE VIEW COLLAPSED BUTTON */}
                            <button
                                type="button"
                                className="navbar-toggle collapsed"
                                data-toggle="collapse"
                                data-target="#navbar"
                                aria-expanded="false"
                                aria-controls="navbar"
                            >
                                <span className="sr-only">Toggle navigation</span>
                                <span className="icon-bar" />
                                <span className="icon-bar" />
                                <span className="icon-bar" />
                            </button>
                            {/* LOGO */}
                            {/* Text based logo */}
                            <a className="navbar-brand aa-logo" href="index.html">
                                {" "}
                                Home <span>Property</span>
                            </a>
                            {/* Image based logo */}
                            {/* <a class="navbar-brand aa-logo-img" href="index.html"><img src="img/logo.png" alt="logo"></a> */}
                        </div>
                        <div id="navbar" className="navbar-collapse collapse">
                            <ul id="top-menu" className="nav navbar-nav navbar-right aa-main-nav">
                                <li>
                                    <a href="index.html">HOME</a>
                                </li>
                                <li className="dropdown">
                                    <a
                                        className="dropdown-toggle"
                                        data-toggle="dropdown"
                                        href="properties.html"
                                    >
                                        PROPERTIES <span className="caret" />
                                    </a>
                                    <ul className="dropdown-menu" role="menu">
                                        <li>
                                            <a href="properties.html">PROPERTIES</a>
                                        </li>
                                        <li>
                                            <a href="properties-detail.html">PROPERTIES DETAIL</a>
                                        </li>
                                    </ul>
                                </li>
                                <li>
                                    <a href="gallery.html">GALLERY</a>
                                </li>
                                <li className="dropdown">
                                    <a
                                        className="dropdown-toggle"
                                        data-toggle="dropdown"
                                        href="blog-archive.html"
                                    >
                                        BLOG <span className="caret" />
                                    </a>
                                    <ul className="dropdown-menu" role="menu">
                                        <li>
                                            <a href="blog-archive.html">BLOG</a>
                                        </li>
                                        <li>
                                            <a href="blog-single.html">BLOG DETAILS</a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="active">
                                    <a href="contact.html">CONTACT</a>
                                </li>
                                <li>
                                    <a href="404.html">404 PAGE</a>
                                </li>
                            </ul>
                        </div>
                        {/*/.nav-collapse */}
                    </div>
                </nav>
            </section>
            {/* End menu section */}
            {/* Start Proerty header  */}
            <section id="aa-property-header">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="aa-property-header-inner">
                                <h2>Contact</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">Contact</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* End Proerty header  */}
            <section id="aa-contact">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="aa-contact-area">
                                <div className="aa-contact-top">
                                    <div className="aa-contact-top-left">
                                        <iframe
                                            width="100%"
                                            height={450}
                                            frameBorder={0}
                                            allowFullScreen=""
                                            style={{ border: 0 }}
                                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6851.201919469417!2d-86.11773906635584!3d33.47324776828677!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x888bdb60cc49c571%3A0x40451ca6baf275c7!2s36008+AL-77%2C+Talladega%2C+AL+35160%2C+USA!5e0!3m2!1sbn!2sbd!4v1460452919256"
                                        />
                                    </div>
                                    <div className="aa-contact-top-right">
                                        <h2>Contact</h2>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                            Beatae placeat aspernatur aperiam, quisquam voluptas enim
                                            tempore ab itaque nam modi eos corrupti distinctio nobis
                                            labore dolorum quae tenetur. Sapiente, sequi.
                                        </p>
                                        <ul className="contact-info-list">
                                            <li>
                                                {" "}
                                                <i className="fa fa-phone" /> 1-700-564-6321
                                            </li>
                                            <li>
                                                {" "}
                                                <i className="fa fa-envelope-o" /> info@homeproperty.com
                                            </li>
                                            <li>
                                                {" "}
                                                <i className="fa fa-map-marker" /> 36008 AL-77, Talladega,
                                                AL 35160, USA
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="aa-contact-bottom">
                                    <div className="aa-title">
                                        <h2>Send Your Message</h2>
                                        <span />
                                        <p>
                                            Your email address will not be published. Required fields are
                                            marked <strong className="required">*</strong>
                                        </p>
                                    </div>
                                    <div className="aa-contact-form">
                                        <form className="contactform">
                                            <p className="comment-form-author">
                                                <label htmlFor="author">
                                                    Name <span className="required">*</span>
                                                </label>
                                                <input
                                                    type="text"
                                                    name="author"
                                                    defaultValue=""
                                                    size={30}
                                                    required="required"
                                                />
                                            </p>
                                            <p className="comment-form-email">
                                                <label htmlFor="email">
                                                    Email <span className="required">*</span>
                                                </label>
                                                <input
                                                    type="email"
                                                    name="email"
                                                    defaultValue=""
                                                    aria-required="true"
                                                    required="required"
                                                />
                                            </p>
                                            <p className="comment-form-url">
                                                <label htmlFor="subject">Subject</label>
                                                <input type="text" name="subject" />
                                            </p>
                                            <p className="comment-form-comment">
                                                <label htmlFor="comment">Message</label>
                                                <textarea
                                                    name="comment"
                                                    cols={45}
                                                    rows={8}
                                                    aria-required="true"
                                                    required="required"
                                                    defaultValue={""}
                                                />
                                            </p>
                                            <p className="form-submit">
                                                <input
                                                    type="submit"
                                                    name="submit"
                                                    className="aa-browse-btn"
                                                    defaultValue="Send Message"
                                                />
                                            </p>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <Footer />
        </>
    )
}