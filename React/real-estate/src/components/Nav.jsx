export default function Nav() {
    return (
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
                        {/* <a class="navbar-brand aa-logo-img" href="index.html"><img src="../../public/img/logo.png" alt="logo"></a> */}
                    </div>
                    <div id="navbar" className="navbar-collapse collapse">
                        <ul id="top-menu" className="nav navbar-nav navbar-right aa-main-nav">
                            <li className="active">
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
                            <li>
                                <a href="404.html">404 PAGE</a>
                            </li>
                        </ul>
                    </div>
                    {/*/.nav-collapse */}
                </div>
            </nav>
        </section>
    )
}