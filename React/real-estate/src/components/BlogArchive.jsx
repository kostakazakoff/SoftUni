import Footer from "./Footer";

export default function BlogArchive() {
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
                            {/* <a class="navbar-brand aa-logo-img" href="index.html"><img src="./public/img/logo.png" alt="logo"></a> */}
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
                                <li className="dropdown active">
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
                                <h2>Blog Page</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">Blog</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* End Proerty header  */}
            {/* Start Blog  */}
            <section id="aa-blog">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="aa-blog-area">
                                <div className="row">
                                    <div className="col-md-8">
                                        <div className="aa-blog-content">
                                            <div className="row">
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-1.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-2.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-3.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-1.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-2.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-3.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-1.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                                <div className="col-md-6 col-sm-6">
                                                    <article className="aa-blog-single">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="./public/img/blog-img-3.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h3>
                                                                <a href="#">
                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                </a>
                                                            </h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </article>
                                                </div>
                                            </div>
                                            <div className="row">
                                                <div className="col-md-12">
                                                    <div className="aa-properties-content-bottom">
                                                        <nav>
                                                            <ul className="pagination">
                                                                <li>
                                                                    <a aria-label="Previous" href="#">
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
                                                                    <a aria-label="Next" href="#">
                                                                        <span aria-hidden="true">»</span>
                                                                    </a>
                                                                </li>
                                                            </ul>
                                                        </nav>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    {/* Start blog sidebar */}
                                    <div className="col-md-4">
                                        <aside className="aa-blog-sidebar">
                                            {/* Start single sidebar */}
                                            <div className="aa-blog-sidebar-single">
                                                <form action="">
                                                    <div className="aa-blog-search">
                                                        <input
                                                            className="aa-search-text"
                                                            type="text"
                                                            placeholder="Search..."
                                                        />
                                                        <button className="aa-search-submit" type="submit">
                                                            <i className="fa fa-search" />
                                                        </button>
                                                    </div>
                                                </form>
                                            </div>
                                            {/* Start single sidebar */}
                                            <div className="aa-blog-sidebar-single">
                                                <h3>Categories</h3>
                                                <ul className="aa-blog-catg">
                                                    <li>
                                                        Properties <span>15000</span>
                                                    </li>
                                                    <li>
                                                        Apartment <span>5000</span>
                                                    </li>
                                                    <li>
                                                        Office <span>3000</span>
                                                    </li>
                                                    <li>
                                                        Residential <span>4500</span>
                                                    </li>
                                                    <li>
                                                        Commercial <span>1000</span>
                                                        <ul>
                                                            <li>
                                                                category 2.1 <span>50</span>
                                                            </li>
                                                            <li>
                                                                category 2.2 <span>100</span>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                    <li>
                                                        Villa <span>800</span>
                                                    </li>
                                                    <li>
                                                        Bungalow <span>200</span>
                                                    </li>
                                                    <li>
                                                        News <span>375</span>
                                                    </li>
                                                    <li>
                                                        Reviews <span>458</span>
                                                    </li>
                                                </ul>
                                            </div>
                                            {/* Start single sidebar */}
                                            <div className="aa-blog-sidebar-single">
                                                <h3>Tags</h3>
                                                <div className="tag-cloud">
                                                    <a href="#">Apartment</a>
                                                    <a href="#">Propery</a>
                                                    <a href="#">Residential</a>
                                                    <a href="#">Commercial</a>
                                                    <a href="#">Office</a>
                                                    <a href="#">Rent</a>
                                                    <a href="#">Sale</a>
                                                    <a href="#">Villa</a>
                                                </div>
                                            </div>
                                            {/* Start single sidebar */}
                                            <div className="aa-blog-sidebar-single">
                                                <h3>Recent Post</h3>
                                                <div className="aa-blog-recent-post">
                                                    <div className="media">
                                                        <div className="media-left">
                                                            <a href="#">
                                                                <img
                                                                    alt="img"
                                                                    src="./public/img/blog-img-3.jpg"
                                                                    className="media-object"
                                                                />
                                                            </a>
                                                        </div>
                                                        <div className="media-body">
                                                            <h4 className="media-heading">
                                                                <a href="#">This is Title</a>
                                                            </h4>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit.
                                                            </p>
                                                            <span>15 April, 16</span>
                                                        </div>
                                                    </div>
                                                    <div className="media">
                                                        <div className="media-left">
                                                            <a href="#">
                                                                <img
                                                                    alt="img"
                                                                    src="./public/img/blog-img-2.jpg"
                                                                    className="media-object"
                                                                />
                                                            </a>
                                                        </div>
                                                        <div className="media-body">
                                                            <h4 className="media-heading">
                                                                <a href="#">This is Title</a>
                                                            </h4>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit.
                                                            </p>
                                                            <span>15 April, 16</span>
                                                        </div>
                                                    </div>
                                                    <div className="media">
                                                        <div className="media-left">
                                                            <a href="#">
                                                                <img
                                                                    alt="img"
                                                                    src="./public/img/blog-img-1.jpg"
                                                                    className="media-object"
                                                                />
                                                            </a>
                                                        </div>
                                                        <div className="media-body">
                                                            <h4 className="media-heading">
                                                                <a href="#">This is Title</a>
                                                            </h4>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit.
                                                            </p>
                                                            <span>15 April, 16</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            {/* Start single sidebar */}
                                            <div className="aa-blog-sidebar-single">
                                                <div className="aa-banner-ads">
                                                    <a href="#">
                                                        <img src="./public/img/banner-ads.jpg" alt="banner img" />
                                                    </a>
                                                </div>
                                            </div>
                                        </aside>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* / Blog  */}
            <Footer />
        </>
    )
}