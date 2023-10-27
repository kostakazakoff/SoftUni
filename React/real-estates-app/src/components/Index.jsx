export default function Index() {
    return(
        <>
  <title>Designa 2.01</title>
  <meta charSet="UTF-8" />
  <meta httpEquiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="viewport" content="width=device-width" />
  
  <div className="container">
    <header id="navtop">
      {" "}
      <a href="index.html" className="logo fleft">
        {" "}
        <img src="../../public/logo.png" alt="" />{" "}
      </a>
      <nav className="fright">
        <ul>
          <li>
            <a href="index.html" className="navactive">
              Home
            </a>
          </li>
          <li>
            <a href="about.html">About</a>
          </li>
        </ul>
        <ul>
          <li>
            <a href="works.html">Works</a>
          </li>
          <li>
            <a href="services.html">Services</a>
          </li>
        </ul>
        <ul>
          <li>
            <a href="blog.html">Blog</a>
          </li>
          <li>
            <a href="contact.html">Contact</a>
          </li>
        </ul>
      </nav>
    </header>
    <div className="home-page main">
      <section className="grid-wrap">
        <header className="grid col-full">
          <hr />
          <p className="fleft">Home</p>
          <a href="about.html" className="arrow fright">
            see more infos
          </a>{" "}
        </header>
        <div className="grid col-one-half mq2-col-full">
          <h1>
            Web design <br />
            Web Development <br />
            Graphic Design
          </h1>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.{" "}
          </p>
          <p>
            Vivamus pharetra posuere sapien. Nam consectetuer. Sed aliquam, nunc
            eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum
            bibendum enim nibh eget ipsum.{" "}
          </p>
        </div>
        <div className="slider grid col-one-half mq2-col-full">
          <div className="flexslider">
            <div className="slides">
              <div className="slide">
                <figure>
                  {" "}
                  <img src="../../public/img2.jpg" alt="" />
                  <figcaption>
                    <div>
                      <h5>Caption 1</h5>
                      <p>
                        Lorem ipsum dolor set amet, lorem,{" "}
                        <a href="#">link text</a>
                      </p>
                    </div>
                  </figcaption>
                </figure>
              </div>
              <div className="slide">
                <figure>
                  {" "}
                  <img src="../../public/img.jpg" alt="" />
                  <figcaption>
                    <div>
                      <h5>Caption 2</h5>
                      <p>
                        Fusce dapibus, tellus ac cursus commodo, tortor mauris
                        condimentum nibh.
                      </p>
                    </div>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="services grid-wrap">
        <header className="grid col-full">
          <hr />
          <p className="fleft">Services</p>
          <a href="services.html" className="arrow fright">
            see more services
          </a>{" "}
        </header>
        <article className="grid col-one-third mq3-col-full">
          <aside>01</aside>
          <h5>Web design</h5>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim.
          </p>
        </article>
        <article className="grid col-one-third mq3-col-full">
          <aside>02</aside>
          <h5>Web development</h5>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim.
          </p>
        </article>
        <article className="grid col-one-third mq3-col-full">
          <aside>03</aside>
          <h5>Graphic design</h5>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim.
          </p>
        </article>
      </section>
      <section className="works grid-wrap">
        <header className="grid col-full">
          <hr />
          <p className="fleft">Works</p>
          <a href="works.html" className="arrow fright">
            see more works
          </a>{" "}
        </header>
        <figure className="grid col-one-quarter mq2-col-one-half">
          {" "}
          <a href="work1.html">
            {" "}
            <img src="../../public/img.jpg" alt="" /> <span className="zoom" />{" "}
          </a>
          <figcaption>
            {" "}
            <a href="work1.html" className="arrow">
              Project page!
            </a>
            <p>Lorem ipsum dolor set amet</p>
          </figcaption>
        </figure>
        <figure className="grid col-one-quarter mq2-col-one-half">
          {" "}
          <a href="#">
            {" "}
            <img src="img/img.jpg" alt="" /> <span className="zoom" />{" "}
          </a>
          <figcaption>
            {" "}
            <a href="#" className="arrow">
              Project x
            </a>
            <p>Lorem ipsum dolor set amet</p>
          </figcaption>
        </figure>
        <figure className="grid col-one-quarter mq2-col-one-half">
          {" "}
          <a href="#">
            {" "}
            <img src="img/img.jpg" alt="" /> <span className="zoom" />{" "}
          </a>
          <figcaption>
            {" "}
            <a href="#" className="arrow">
              Project x
            </a>
            <p>Lorem ipsum dolor set amet</p>
          </figcaption>
        </figure>
        <figure className="grid col-one-quarter mq2-col-one-half">
          {" "}
          <a href="#">
            {" "}
            <img src="img/img.jpg" alt="" /> <span className="zoom" />{" "}
          </a>
          <figcaption>
            {" "}
            <a href="#" className="arrow">
              Project x
            </a>
            <p>Lorem ipsum dolor set amet</p>
          </figcaption>
        </figure>
      </section>
    </div>
    {/*main*/}
    <div className="divide-top">
      <footer className="grid-wrap">
        <ul className="grid col-one-third social">
          <li>
            <a href="#">RSS</a>
          </li>
          <li>
            <a href="#">Facebook</a>
          </li>
          <li>
            <a href="#">Twitter</a>
          </li>
          <li>
            <a href="#">Google+</a>
          </li>
          <li>
            <a href="#">Flickr</a>
          </li>
        </ul>
        <div className="up grid col-one-third ">
          {" "}
          <a href="#navtop" title="Go back up">
            ↑
          </a>{" "}
        </div>
        <nav className="grid col-one-third ">
          <ul>
            <li>
              <a href="index.html">Home</a>
            </li>
            <li>
              <a href="about.html">About</a>
            </li>
            <li>
              <a href="works.html">Works</a>
            </li>
            <li>
              <a href="services.html">Services</a>
            </li>
            <li>
              <a href="blog.html">Blog</a>
            </li>
            <li>
              <a href="contact.html">Contact</a>
            </li>
          </ul>
        </nav>
      </footer>
    </div>
  </div>
  {/* Javascript - jQuery */}
  {/*[if (gte IE 6)&(lte IE 8)]><![endif]*/}
</>

    );
}