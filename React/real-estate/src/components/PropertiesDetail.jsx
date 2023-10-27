import Footer from "./Footer";
import Preloader from "./PreloaderScrollBtn";

export default function PropertiesDetail() {
    return (
        <>
            <Preloader />
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
                                <li className="dropdown active">
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
                                <li>
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
                                <h2>Properties Details</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">APPARTMENT TITLE</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* End Proerty header  */}
            {/* Start Properties  */}
            <section id="aa-properties">
                <div className="container">
                    <div className="row">
                        <div className="col-md-8">
                            <div className="aa-properties-content">
                                {/* Start properties content body */}
                                <div className="aa-properties-details">
                                    <div className="aa-properties-details-img">
                                        <img src="img/slider/1.jpg" alt="img" />
                                        <img src="img/slider/2.jpg" alt="img" />
                                        <img src="img/slider/3.jpg" alt="img" />
                                    </div>
                                    <div className="aa-properties-info">
                                        <h2>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex,
                                            alias!
                                        </h2>
                                        <span className="aa-price">$65000</span>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae
                                            voluptatibus veniam non voluptate, ipsa eius magni aliquid
                                            ratione sit, odio reprehenderit in quis repudiandae dolor.
                                        </p>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet
                                            consequatur, veritatis, ducimus in aliquam magnam voluptatibus
                                            ullam libero fugiat temporibus at, aliquid explicabo placeat
                                            eligendi, assumenda magni saepe eius consequuntur.
                                        </p>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                            Praesentium dicta aliquid, autem, cum, impedit nostrum, rem
                                            molestias quisquam ab iure enim totam? Itaque esse ut adipisci
                                            officiis nulla repellendus ratione dolore, iste ex doloribus
                                            tenetur eos provident quam quasi maxime.
                                        </p>
                                        <h4>Propery Features</h4>
                                        <ul>
                                            <li>4 Bedroom</li>
                                            <li>3 Baths</li>
                                            <li>Kitchen</li>
                                            <li>Air Condition</li>
                                            <li>Belcony</li>
                                            <li>Gym</li>
                                            <li>Garden</li>
                                            <li>CCTV</li>
                                            <li>Children Play Ground</li>
                                            <li>Comunity Center</li>
                                            <li>Security System</li>
                                        </ul>
                                        <h4>Property Video</h4>
                                        <iframe
                                            width="100%"
                                            height={480}
                                            src="https://www.youtube.com/embed/CegXQps0In4"
                                            frameBorder={0}
                                            allowFullScreen=""
                                        />
                                        <h4>Property Map</h4>
                                        <iframe
                                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6851.201919469417!2d-86.11773906635584!3d33.47324776828677!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x888bdb60cc49c571%3A0x40451ca6baf275c7!2s36008+AL-77%2C+Talladega%2C+AL+35160%2C+USA!5e0!3m2!1sbn!2sbd!4v1460452919256"
                                            width="100%"
                                            height={450}
                                            frameBorder={0}
                                            style={{ border: 0 }}
                                            allowFullScreen=""
                                        />
                                    </div>
                                    {/* Properties social share */}
                                    <div className="aa-properties-social">
                                        <ul>
                                            <li>Share</li>
                                            <li>
                                                <a href="#">
                                                    <i className="fa fa-facebook" />
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <i className="fa fa-twitter" />
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <i className="fa fa-google-plus" />
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <i className="fa fa-pinterest" />
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    {/* Nearby properties */}
                                    <div className="aa-nearby-properties">
                                        <div className="aa-title">
                                            <h2>Nearby Properties</h2>
                                            <span />
                                        </div>
                                        <div className="aa-nearby-properties-area">
                                            <div className="row">
                                                <div className="col-md-6">
                                                    <article className="aa-properties-item">
                                                        <a className="aa-properties-item-img" href="#">
                                                            <img alt="img" src="img/item/1.jpg" />
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
                                                                    Lorem ipsum dolor sit amet, consectetur
                                                                    adipisicing elit. Enim molestiae vero ducimus
                                                                    quibusdam odit vitae.
                                                                </p>
                                                            </div>
                                                            <div className="aa-properties-detial">
                                                                <span className="aa-price">$35000</span>
                                                                <a className="aa-secondary-btn" href="#">
                                                                    View Details
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6">
                                                    <article className="aa-properties-item">
                                                        <a className="aa-properties-item-img" href="#">
                                                            <img alt="img" src="img/item/2.jpg" />
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
                                                                    Lorem ipsum dolor sit amet, consectetur
                                                                    adipisicing elit. Enim molestiae vero ducimus
                                                                    quibusdam odit vitae.
                                                                </p>
                                                            </div>
                                                            <div className="aa-properties-detial">
                                                                <span className="aa-price">$35000</span>
                                                                <a className="aa-secondary-btn" href="#">
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
                            </div>
                        </div>
                        {/* Start properties sidebar */}
                        <div className="col-md-4">
                            <aside className="aa-properties-sidebar">
                                {/* Start Single properties sidebar */}
                                <div className="aa-properties-single-sidebar">
                                    <h3>Properties Search</h3>
                                    <form action="">
                                        <div className="aa-single-advance-search">
                                            <input type="text" placeholder="Type Your Location" />
                                        </div>
                                        <div className="aa-single-advance-search">
                                            <select id="" name="">
                                                <option selected="" value={0}>
                                                    Category
                                                </option>
                                                <option value={1}>Flat</option>
                                                <option value={2}>Land</option>
                                                <option value={3}>Plot</option>
                                                <option value={4}>Commercial</option>
                                            </select>
                                        </div>
                                        <div className="aa-single-advance-search">
                                            <select id="" name="">
                                                <option selected="" value={0}>
                                                    Type
                                                </option>
                                                <option value={1}>Flat</option>
                                                <option value={2}>Land</option>
                                                <option value={3}>Plot</option>
                                                <option value={4}>Commercial</option>
                                            </select>
                                        </div>
                                        <div className="aa-single-advance-search">
                                            <select id="" name="">
                                                <option selected="" value={0}>
                                                    Type
                                                </option>
                                                <option value={1}>Flat</option>
                                                <option value={2}>Land</option>
                                                <option value={3}>Plot</option>
                                                <option value={4}>Commercial</option>
                                            </select>
                                        </div>
                                        <div className="aa-single-filter-search">
                                            <span>AREA (SQ)</span>
                                            <span>FROM</span>
                                            <span id="skip-value-lower" className="example-val">
                                                30.00
                                            </span>
                                            <span>TO</span>
                                            <span id="skip-value-upper" className="example-val">
                                                100.00
                                            </span>
                                            <div
                                                id="aa-sqrfeet-range"
                                                className="noUi-target noUi-ltr noUi-horizontal noUi-background"
                                            ></div>
                                        </div>
                                        <div className="aa-single-filter-search">
                                            <span>PRICE ($)</span>
                                            <span>FROM</span>
                                            <span id="skip-value-lower2" className="example-val">
                                                30.00
                                            </span>
                                            <span>TO</span>
                                            <span id="skip-value-upper2" className="example-val">
                                                100.00
                                            </span>
                                            <div
                                                id="aa-price-range"
                                                className="noUi-target noUi-ltr noUi-horizontal noUi-background"
                                            ></div>
                                        </div>
                                        <div className="aa-single-advance-search">
                                            <input
                                                type="submit"
                                                defaultValue="Search"
                                                className="aa-search-btn"
                                            />
                                        </div>
                                    </form>
                                </div>
                                {/* Start Single properties sidebar */}
                                <div className="aa-properties-single-sidebar">
                                    <h3>Populer Properties</h3>
                                    <div className="media">
                                        <div className="media-left">
                                            <a href="#">
                                                <img
                                                    className="media-object"
                                                    src="img/item/1.jpg"
                                                    alt="img"
                                                />
                                            </a>
                                        </div>
                                        <div className="media-body">
                                            <h4 className="media-heading">
                                                <a href="#">This is Title</a>
                                            </h4>
                                            <p>
                                                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                            </p>
                                            <span>$65000</span>
                                        </div>
                                    </div>
                                    <div className="media">
                                        <div className="media-left">
                                            <a href="#">
                                                <img
                                                    className="media-object"
                                                    src="img/item/1.jpg"
                                                    alt="img"
                                                />
                                            </a>
                                        </div>
                                        <div className="media-body">
                                            <h4 className="media-heading">
                                                <a href="#">This is Title</a>
                                            </h4>
                                            <p>
                                                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                            </p>
                                            <span>$65000</span>
                                        </div>
                                    </div>
                                    <div className="media">
                                        <div className="media-left">
                                            <a href="#">
                                                <img
                                                    className="media-object"
                                                    src="img/item/1.jpg"
                                                    alt="img"
                                                />
                                            </a>
                                        </div>
                                        <div className="media-body">
                                            <h4 className="media-heading">
                                                <a href="#">This is Title</a>
                                            </h4>
                                            <p>
                                                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                            </p>
                                            <span>$65000</span>
                                        </div>
                                    </div>
                                </div>
                            </aside>
                        </div>
                    </div>
                </div>
            </section>
            {/* / Properties  */}
            <Footer />
        </>

    )
}