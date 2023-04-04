document.body.innerHTML = `
<div id="main">
      <div class="form-wrapper">
        <h1>
          DOM Chefs<span
            >Fill the form with the chef and his dish information!</span
          >
        </h1>
        <form>
          <div class="section"><span>1</span>Chef Information</div>
          <div class="inner-wrap">
            <label
              >First Name <input type="text" id="first-name" name="field1"
            /></label>
            <label
              >Last Name <input type="text" id="last-name" name="field2"
            /></label>
            <label>Age <input type="number" id="age" name="field3" /></label>
            <p id="gender">Gender</p>
            <select id="genderSelect">
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>

          <div class="section"><span>2</span>Dish Information</div>
          <div class="inner-wrap">
            <label for="task">Dish description</label>
            <textarea id="task" name="task" rows="4" cols="50"></textarea>
          </div>
          <div class="button-section">
            <input type="button" id="form-btn" value="Submit" />
          </div>
        </form>
      </div>
      <div id="side-wrapper">
        <ul id="in-progress">
          <h3>In progress</h3>
        </ul>

        <div id="finished-wrapper">
          <h3>Finished cooking</h3>
          <ul id="finished">
            
          </ul>
          <button id="clear-btn">Clear</button>
        </div>

        <p id="message">
          Dishes still in progress: <span id="progress-count">0</span>
        </p>
      </div>
    </div>
    <script src="app.js"></script>
`
result();
const createPost = {
    firstName: () => document.getElementById("first-name"),
    lastName: () => document.getElementById("last-name"),
    gender: () => document.getElementById("genderSelect"),
    age: () => document.getElementById("age"),
    description: () => document.getElementById("task"),
    addBtn: () => document.getElementById("form-btn"),
}

createPost.firstName().value = "Peter"
createPost.lastName().value = "Johnson"
createPost.gender().value = "Male"
createPost.age().value = "31"
createPost.description().value = "Biscuits n gravy. An irresistible Southern favorite, biscuits and gravy would be a cliche if they werent so darned delicious."

createPost.addBtn().click();

expect((document.querySelector(".each-line>article>h4")).textContent).to.equal('Peter Johnson', 'Chef name is invalid.');
expect((document.querySelectorAll(".each-line>article>p"))[0].textContent).to.equal('Male, 31', 'Chef age or gender is invalid.');
expect((document.querySelectorAll(".each-line>article>p"))[1].textContent).to.equal('Dish description: Biscuits n gravy. An irresistible Southern favorite, biscuits and gravy would be a cliche if they werent so darned delicious.', 'Dish description is invalid');

