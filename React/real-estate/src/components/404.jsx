import Footer from "./Footer";
import Preloader from "./PreloaderScrollBtn";

export default function Error404() {
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
                                <li className="active">
                                    <a href="#">404 PAGE</a>
                                </li>
                                {/* <li class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">PAGES <span class="caret"></span></a>
        <ul class="dropdown-menu" role="menu">                
          <li><a href="properties-detail.html">PRODUCT DETAILS</a></li>
          <li><a href="blog-single.html">BLOG DETAILS</a></li>                
          <li class="active"><a href="404.html">404 PAGE</a></li>                
        </ul>
      </li> */}
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
                                <h2>404 Error</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">404</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* End Proerty header  */}
            <section id="aa-error">
                <div className="container">
                    <row>
                        <div className="col-md-12">
                            <div className="aa-error-area">
                                <h2>404</h2>
                                <p>
                                    <span className="fa fa-warning" />
                                    Oops! The Page you requested was not found!
                                </p>
                                <a href="#">Back Home</a>
                            </div>
                        </div>
                    </row>
                </div>
            </section>
            <Footer />
        </>
    )
}