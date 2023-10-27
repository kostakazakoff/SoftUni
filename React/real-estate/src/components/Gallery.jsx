import Footer from "./Footer";
import Preloader from "./PreloaderScrollBtn";

export default function Gallery() {
    return (
        <>
            <Preloader />
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
                                <li className="active">
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
                                <h2>Gallery</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">Gallery</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* End Proerty header  */}
            <section id="aa-gallery">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="aa-gallery-area">
                                <div className="aa-title">
                                    <h2>Gallery View</h2>
                                    <span />
                                    <p>
                                        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                                        Excepturi commodi eum dolorem aut eos, debitis quaerat
                                        reiciendis, officiis consectetur ducimus atque suscipit ab at
                                        tempora!
                                    </p>
                                </div>
                                {/* Start gallery */}
                                <div className="aa-gallery-content">
                                    <div className="aa-gallery-top">
                                        {/* Start gallery menu */}
                                        <ul>
                                            <li data-filter="all" className="filter active">
                                                All
                                            </li>
                                            <li data-filter=".apartment" className="filter">
                                                Apartment
                                            </li>
                                            <li data-filter=".livingroom" className="filter">
                                                Living Room
                                            </li>
                                            <li data-filter=".bedroom" className="filter">
                                                Bedroom
                                            </li>
                                            <li data-filter=".kitchen" className="filter">
                                                Kitchen
                                            </li>
                                            <li data-filter=".garage" className="filter">
                                                Garage
                                            </li>
                                        </ul>
                                    </div>
                                    {/* Start gallery image */}
                                    <div id="mixit-container" className="aa-gallery-body">
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix apartment">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/1.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/1.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix garage">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/2.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/2.jpg"
                                                    >
                                                        <span className="fa fa-eye" />
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix livingroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/3.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/3.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix bedroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/4.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/4.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix apartment">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/5.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/5.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix livingroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/6.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/6.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix apartment">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/7.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/7.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix garage">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/8.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/8.jpg"
                                                    >
                                                        <span className="fa fa-eye" />
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix livingroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/9.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/9.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix bedroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/10.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/10.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix kitchen">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/11.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/11.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        {/* start single gallery image */}
                                        <div className="aa-single-gallery mix livingroom">
                                            <div className="aa-single-gallery-item">
                                                <div className="aa-single-gallery-img">
                                                    <a href="#">
                                                        <img src="img/gallery/small/12.jpg" alt="img" />
                                                    </a>
                                                </div>
                                                <div className="aa-single-gallery-info">
                                                    <a
                                                        className="fancybox"
                                                        data-fancybox-group="gallery"
                                                        href="img/gallery/big/12.jpg"
                                                    >
                                                        <span className="fa fa-eye"></span>
                                                    </a>
                                                    <a className="aa-link" href="#">
                                                        <span className="fa fa-link" />
                                                    </a>
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
            <Footer />
        </>
    )
}