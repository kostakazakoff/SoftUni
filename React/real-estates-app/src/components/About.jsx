export default function About() {
    return(
        <>
  <title>Designa 2.01 | About</title>
  
  <div className="container">
    <header id="navtop">
      {" "}
      <a href="index.html" className="logo fleft">
        {" "}
        <img src="img/logo.png" alt="" />{" "}
      </a>
      <nav className="fright">
        <ul>
          <li>
            <a href="index.html">Home</a>
          </li>
          <li>
            <a href="about.html" className="navactive">
              About
            </a>
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
    <div className="about-page main grid-wrap">
      <header className="grid col-full">
        <hr />
        <p className="fleft">About</p>
      </header>
      <aside className="grid col-one-quarter mq2-col-full">
        <p className="mbottom">
          Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
          commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
          pulvinar odio lorem non turpis.{" "}
        </p>
        <menu>
          <ul>
            <li>
              <a href="#navteam" className="arrow">
                Our team
              </a>
            </li>
            <li>
              <a href="#navphilo" className="arrow">
                Our philosophy
              </a>
            </li>
            <li>
              <a href="#navplace" className="arrow">
                Our place
              </a>
            </li>
            <li>
              <a href="#navother" className="arrow">
                Our lorem
              </a>
            </li>
          </ul>
        </menu>
      </aside>
      <section className="grid col-three-quarters mq2-col-full">
        {" "}
        <img src="img/team.jpg" alt="" />
        <article id="navteam">
          <h2>Our team</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
        </article>
        <article id="navphilo">
          <h2>Our philosophy</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
        </article>
        <article id="navplace">
          <h2>Our place</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
        </article>
        <article id="navother">
          <h2>Our lorem</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id
            pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id
            velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed
            quis velit.
          </p>
        </article>
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