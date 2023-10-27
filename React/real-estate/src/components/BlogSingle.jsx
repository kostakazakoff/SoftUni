import Footer from "./Footer";
import Preloader from "./PreloaderScrollBtn";

export default function Blog() {
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
                                <h2>Blog Details</h2>
                                <ol className="breadcrumb">
                                    <li>
                                        <a href="#">HOME</a>
                                    </li>
                                    <li className="active">Blog Details</li>
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
                                                <div className="col-md-12">
                                                    <article className="aa-blog-single aa-blog-details">
                                                        <figure className="aa-blog-img">
                                                            <a href="#">
                                                                <img alt="img" src="img/slider/1.jpg" />
                                                            </a>
                                                            <span className="aa-date-tag">15 April, 16</span>
                                                        </figure>
                                                        <div className="aa-blog-single-content">
                                                            <h2>Lorem ipsum dolor sit amet, consectetur.</h2>
                                                            <div className="aa-blog-single-bottom">
                                                                <a className="aa-blog-author" href="#">
                                                                    <i className="fa fa-user" /> Admin
                                                                </a>
                                                                <a className="aa-blog-comments" href="#">
                                                                    <i className="fa fa-comment-o" />6
                                                                </a>
                                                            </div>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Optio est quaerat magnam exercitationem
                                                                voluptas, voluptatem sed quam ab laborum voluptatum
                                                                tempore dolores itaque, molestias vitae.
                                                            </p>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Laborum molestias eligendi quidem vero alias
                                                                ea. Accusantium quas soluta recusandae, ducimus
                                                                voluptates aut, assumenda earum velit, dignissimos
                                                                repellendus delectus voluptate, labore.
                                                            </p>
                                                            <blockquote>
                                                                <p>
                                                                    Lorem ipsum dolor sit amet, consectetur
                                                                    adipisicing elit. Cupiditate explicabo
                                                                    consequuntur, impedit aut similique cum.
                                                                </p>
                                                                <cite>- Mr. josep</cite>
                                                            </blockquote>
                                                            <h1>H1 Title</h1>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Officia inventore commodi labore. Doloremque
                                                                voluptas ullam iusto nemo quisquam, saepe sit.
                                                            </p>
                                                            <h2>H2 Title</h2>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Officia inventore commodi labore. Doloremque
                                                                voluptas ullam iusto nemo quisquam, saepe sit.
                                                            </p>
                                                            <h3>H3 Title</h3>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Officia inventore commodi labore. Doloremque
                                                                voluptas ullam iusto nemo quisquam, saepe sit.
                                                            </p>
                                                            <h4>H4 Title</h4>
                                                            <p>
                                                                Lorem ipsum dolor sit amet, consectetur adipisicing
                                                                elit. Inventore, provident.
                                                            </p>
                                                        </div>
                                                    </article>
                                                </div>
                                                {/* Post tags */}
                                                <div className="col-md-12">
                                                    <div className="aa-blog-post-tag">
                                                        <ul>
                                                            <li>TAGES:</li>
                                                            <li>
                                                                <a href="#">POPERTY,</a>
                                                            </li>
                                                            <li>
                                                                <a href="#">LAND,</a>
                                                            </li>
                                                            <li>
                                                                <a href="#">FLAT,</a>
                                                            </li>
                                                            <li>
                                                                <a href="#">RENT,</a>
                                                            </li>
                                                            <li>
                                                                <a href="#">SALE,</a>
                                                            </li>
                                                            <li>
                                                                <a href="#">OFFICE</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                {/* Social Share */}
                                                <div className="col-md-12">
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
                                                </div>
                                                {/* post navigation */}
                                                <div className="col-md-12">
                                                    <div className="aa-blog-navigation">
                                                        <div className="aa-blog-pagination-left">
                                                            <a href="#" className="aa-prev">
                                                                <span className="fa fa-angle-double-left"></span>
                                                                PREV
                                                            </a>
                                                        </div>
                                                        <div className="aa-blog-pagination-right">
                                                            <a href="#" className="aa-next">
                                                                NEXT
                                                                <span className="fa fa-angle-double-right"></span>
                                                            </a>
                                                        </div>
                                                    </div>
                                                </div>
                                                {/* Related blog post */}
                                                <div className="col-md-12">
                                                    <div className="aa-blog-related-post">
                                                        <div className="aa-title">
                                                            <h2>Related Post</h2>
                                                            <span />
                                                        </div>
                                                        <div className="aa-blog-related-post-area">
                                                            <div className="row">
                                                                <div className="col-md-6 col-sm-6">
                                                                    <article className="aa-blog-single">
                                                                        <figure className="aa-blog-img">
                                                                            <a href="#">
                                                                                <img src="img/blog-img-1.jpg" alt="img" />
                                                                            </a>
                                                                            <span className="aa-date-tag">
                                                                                15 April, 16
                                                                            </span>
                                                                        </figure>
                                                                        <div className="aa-blog-single-content">
                                                                            <h3>
                                                                                <a href="#">
                                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                                </a>
                                                                            </h3>
                                                                            <p>
                                                                                Lorem ipsum dolor sit amet, consectetur
                                                                                adipisicing elit. Optio est quaerat magnam
                                                                                exercitationem voluptas, voluptatem sed quam
                                                                                ab laborum voluptatum tempore dolores
                                                                                itaque, molestias vitae.
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
                                                                <div className="col-md-6 col-sm-6">
                                                                    <article className="aa-blog-single">
                                                                        <figure className="aa-blog-img">
                                                                            <a href="#">
                                                                                <img src="img/blog-img-2.jpg" alt="img" />
                                                                            </a>
                                                                            <span className="aa-date-tag">
                                                                                15 April, 16
                                                                            </span>
                                                                        </figure>
                                                                        <div className="aa-blog-single-content">
                                                                            <h3>
                                                                                <a href="#">
                                                                                    Lorem ipsum dolor sit amet, consectetur.
                                                                                </a>
                                                                            </h3>
                                                                            <p>
                                                                                Lorem ipsum dolor sit amet, consectetur
                                                                                adipisicing elit. Optio est quaerat magnam
                                                                                exercitationem voluptas, voluptatem sed quam
                                                                                ab laborum voluptatum tempore dolores
                                                                                itaque, molestias vitae.
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
                                                {/* comment threats */}
                                                <div className="col-md-12">
                                                    <div className="aa-comments-area">
                                                        <h3>5 Comments</h3>
                                                        <div className="comments">
                                                            <ul className="commentlist">
                                                                <li>
                                                                    <div className="media">
                                                                        <div className="media-left">
                                                                            <img
                                                                                alt="img"
                                                                                src="img/testimonial-1.png"
                                                                                className="media-object news-img"
                                                                            />
                                                                        </div>
                                                                        <div className="media-body">
                                                                            <h4 className="author-name">Adam Barney</h4>
                                                                            <span className="comments-date">
                                                                                {" "}
                                                                                20th April, 2016
                                                                            </span>
                                                                            <p>
                                                                                Lorem Ipsum is that it has a more-or-less
                                                                                normal distribution of letters, as opposed
                                                                                to ,
                                                                                making it look like readable English
                                                                            </p>
                                                                            <a className="reply-btn" href="#">
                                                                                Reply
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div className="media">
                                                                        <div className="media-left">
                                                                            <img
                                                                                alt="img"
                                                                                src="img/testimonial-2.png"
                                                                                className="media-object news-img"
                                                                            />
                                                                        </div>
                                                                        <div className="media-body">
                                                                            <h4 className="author-name">John Smith</h4>
                                                                            <span className="comments-date">
                                                                                {" "}
                                                                                20th April, 2016
                                                                            </span>
                                                                            <p>
                                                                                Lorem Ipsum is that it has a more-or-less
                                                                                normal distribution of letters, as opposed
                                                                                to using Content here, content here,
                                                                                making it look like readable English
                                                                            </p>
                                                                            <a className="reply-btn" href="#">
                                                                                Reply
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <ul className="children">
                                                                    <li className="author-comments">
                                                                        <div className="media">
                                                                            <div className="media-left">
                                                                                <img
                                                                                    alt="img"
                                                                                    src="img/testimonial-3.png"
                                                                                    className="media-object news-img"
                                                                                />
                                                                            </div>
                                                                            <div className="media-body">
                                                                                <h4 className="author-name">Admin</h4>
                                                                                <span className="comments-date">
                                                                                    {" "}
                                                                                    20th April, 2016
                                                                                </span>
                                                                                <span className="author-tag">Author</span>
                                                                                <p>
                                                                                    Lorem Ipsum is that it has a more-or-less
                                                                                    normal distribution of letters, as opposed
                                                                                    to using Content here, content here,
                                                                                    making it look like readable English
                                                                                </p>
                                                                                <a className="reply-btn" href="#">
                                                                                    Reply
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                    </li>
                                                                    <ul className="children">
                                                                        <li>
                                                                            <div className="media">
                                                                                <div className="media-left">
                                                                                    <img
                                                                                        alt="img"
                                                                                        src="img/testimonial-1.png"
                                                                                        className="media-object news-img"
                                                                                    />
                                                                                </div>
                                                                                <div className="media-body">
                                                                                    <h4 className="author-name">
                                                                                        Adam Barney
                                                                                    </h4>
                                                                                    <span className="comments-date">
                                                                                        {" "}
                                                                                        20th April, 2016
                                                                                    </span>
                                                                                    <p>
                                                                                        Lorem Ipsum is that it has a
                                                                                        more-or-less normal distribution of
                                                                                        letters, as opposed to using Content
                                                                                        here, content here, making it look like
                                                                                        readable English
                                                                                    </p>
                                                                                    <a className="reply-btn" href="#">
                                                                                        Reply
                                                                                    </a>
                                                                                </div>
                                                                            </div>
                                                                        </li>
                                                                    </ul>
                                                                </ul>
                                                                <li>
                                                                    <div className="media">
                                                                        <div className="media-left">
                                                                            <img
                                                                                alt="img"
                                                                                src="img/testimonial-2.png"
                                                                                className="media-object news-img"
                                                                            />
                                                                        </div>
                                                                        <div className="media-body">
                                                                            <h4 className="author-name">Jhon Smith</h4>
                                                                            <span className="comments-date">
                                                                                {" "}
                                                                                20th April, 2016
                                                                            </span>
                                                                            <p>
                                                                                Lorem Ipsum is that it has a more-or-less
                                                                                normal distribution of letters, as opposed
                                                                                to using Content here, content here,
                                                                                making it look like readable English
                                                                            </p>
                                                                            <a className="reply-btn" href="#">
                                                                                Reply
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                            </ul>
                                                            {/* comments pagination */}
                                                            <nav>
                                                                <ul className="pagination comments-pagination">
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
                                                                    <li>
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
                                                {/* Respond box */}
                                                <div className="col-md-12">
                                                    <div id="respond">
                                                        <h3 className="reply-title">Leave a Comment</h3>
                                                        <form id="commentform">
                                                            <p className="comment-notes">
                                                                Your email address will not be published. Required
                                                                fields are marked{" "}
                                                                <span className="required">*</span>
                                                            </p>
                                                            <p className="comment-form-author">
                                                                <label htmlFor="author">
                                                                    Name <span className="required">*</span>
                                                                </label>
                                                                <input
                                                                    type="text"
                                                                    required="required"
                                                                    size={30}
                                                                    defaultValue=""
                                                                    name="author"
                                                                />
                                                            </p>
                                                            <p className="comment-form-email">
                                                                <label htmlFor="email">
                                                                    Email <span className="required">*</span>
                                                                </label>
                                                                <input
                                                                    type="email"
                                                                    required="required"
                                                                    aria-required="true"
                                                                    defaultValue=""
                                                                    name="email"
                                                                />
                                                            </p>
                                                            <p className="comment-form-url">
                                                                <label htmlFor="url">Website</label>
                                                                <input type="url" defaultValue="" name="url" />
                                                            </p>
                                                            <p className="comment-form-comment">
                                                                <label htmlFor="comment">Comment</label>
                                                                <textarea
                                                                    required="required"
                                                                    aria-required="true"
                                                                    rows={8}
                                                                    cols={45}
                                                                    name="comment"
                                                                    defaultValue={""}
                                                                />
                                                            </p>
                                                            <p className="form-allowed-tags">
                                                                You may use these{" "}
                                                                <abbr title="HyperText Markup Language">HTML</abbr>{" "}
                                                                tags and attributes:{" "}
                                                                {/* <code>
                                                                    &lt;a href="" title=""&gt; &lt;abbr title=""&gt;
                                                                    &lt;acronym title=""&gt; &lt;b&gt; &lt;blockquote
                                                                    cite=""&gt; &lt;cite&gt; &lt;code&gt; &lt;del
                                                                    datetime=""&gt; &lt;em&gt; &lt;i&gt; &lt;q
                                                                    cite=""&gt; &lt;s&gt; &lt;strike&gt;
                                                                    &lt;strong&gt;{" "}
                                                                </code> */}
                                                            </p>
                                                            <p className="form-submit">
                                                                <input
                                                                    type="submit"
                                                                    defaultValue="Post Comment"
                                                                    className="aa-browse-btn"
                                                                    name="submit"
                                                                />
                                                            </p>
                                                        </form>
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
                                                                    src="img/blog-img-3.jpg"
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
                                                                    src="img/blog-img-2.jpg"
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
                                                                    src="img/blog-img-1.jpg"
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
                                                        <img src="img/banner-ads.jpg" alt="banner img" />
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