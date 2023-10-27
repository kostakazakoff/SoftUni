import Footer from "./Footer";
import Preloader from "./PreloaderScrollBtn";

export default function Properties() {
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
                                <h2>Properties Page</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">PROPERTIES</li>
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
                                {/* start properties content head */}
                                <div className="aa-properties-content-head">
                                    <div className="aa-properties-content-head-left">
                                        <form action="" className="aa-sort-form">
                                            <label htmlFor="">Sort by</label>
                                            <select name="">
                                                <option value={1} selected="Default">
                                                    Default
                                                </option>
                                                <option value={2}>Name</option>
                                                <option value={3}>Price</option>
                                                <option value={4}>Date</option>
                                            </select>
                                        </form>
                                        <form action="" className="aa-show-form">
                                            <label htmlFor="">Show</label>
                                            <select name="">
                                                <option value={1} selected={12}>
                                                    6
                                                </option>
                                                <option value={2}>12</option>
                                                <option value={3}>24</option>
                                            </select>
                                        </form>
                                    </div>
                                    <div className="aa-properties-content-head-right">
                                        <a id="aa-grid-properties" href="#">
                                            <span className="fa fa-th" />
                                        </a>
                                        <a id="aa-list-properties" href="#">
                                            <span className="fa fa-list" />
                                        </a>
                                    </div>
                                </div>
                                {/* Start properties content body */}
                                <div className="aa-properties-content-body">
                                    <ul className="aa-properties-nav">
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/6.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/1.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/2.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/5.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/3.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                        <li>
                                            <article className="aa-properties-item">
                                                <a className="aa-properties-item-img" href="#">
                                                    <img alt="img" src="img/item/4.jpg" />
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
                                                            Lorem ipsum dolor sit amet, consectetur adipisicing
                                                            elit. Enim molestiae vero ducimus quibusdam odit
                                                            vitae.
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
                                        </li>
                                    </ul>
                                </div>
                                {/* Start properties content bottom */}
                                <div className="aa-properties-content-bottom">
                                    <nav>
                                        <ul className="pagination">
                                            <li>
                                                <a href="#" aria-label="Previous">
                                                    <span aria-hidden="true">«</span>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">1</a>
                                            </li>
                                            <li>
                                                <a href="#">2</a>
                                            </li>
                                            <li className="active">
                                                <a href="#">3</a>
                                            </li>
                                            <li>
                                                <a href="#">4</a>
                                            </li>
                                            <li>
                                                <a href="#">5</a>
                                            </li>
                                            <li>
                                                <a href="#" aria-label="Next">
                                                    <span aria-hidden="true">»</span>
                                                </a>
                                            </li>
                                        </ul>
                                    </nav>
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