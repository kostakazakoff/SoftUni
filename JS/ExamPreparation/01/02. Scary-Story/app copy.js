window.addEventListener("load", solve);

function solve() {
  const fName = document.getElementById('first-name');
  const lName = document.getElementById('last-name');
  const age = document.getElementById('age');
  const title = document.getElementById('story-title');
  const storyText = document.getElementById('story');
  const publishBtn = document.getElementById('form-btn');
  const publishedStoryUl = document.getElementById('preview-list');

  function publishStory() {
    const genre = document.querySelector('option:checked').innerText;
    const li = document.createElement('li');
    li.className = 'story-info';
    li.innerHTML = `
    <article>
    <h4 id="pub-fullname">Name: ${fName.value} ${lName.value}</h4>
    <p id="pub-age">Age: ${age.value}</p>
    <p id="pub-title">Title: ${title.value}</p>
    <p id="pub-genre">Genre: ${genre}</p>
    <p id="pub-story">${storyText.value}</p>
    </article>
    <button class="save-btn">Save Story</button>
    <button class="edit-btn">Edit Story</button>
    <button class="delete-btn">Delete Story</button>
    `;
    publishedStoryUl.appendChild(li);
    const saveBtn = document.querySelector('.save-btn');
    const editBtn = document.querySelector('.edit-btn');
    const deleteBtn = document.querySelector('.delete-btn');

    [fName, lName, age, title, storyText].map(el => el.value = '');

    publishBtn.disabled = true;

    editBtn.addEventListener('click', () => editStory());
    saveBtn.addEventListener('click', () => saveStory());
    deleteBtn.addEventListener('click', () => cleanPublishList());
  }

  function editStory() {
    const pubFullName = document.getElementById('pub-fullname');
    const pubAge = document.getElementById('pub-age');
    const pubTitle = document.getElementById('pub-title');
    const pubStory = document.getElementById('pub-story');
    
    [fName.value, lName.value] = pubFullName.innerText.split(' ').slice(1);
    age.value = pubAge.textContent.split(' ')[1];
    title.value = pubTitle.textContent.split(' ')[1];
    storyText.value = pubStory.textContent;

    cleanPublishList()
  }

  function saveStory() {
    document.getElementById('main').innerHTML = '<h1>Your scary story is saved!</h1>'
  }

  publishBtn.addEventListener('click', () => {
    const validInput = [fName, lName, age, title, storyText].every((el) => el.value.length > 0);
    if (validInput) { publishStory() }
  })

  function cleanPublishList() {
    publishedStoryUl.innerHTML = '<h3>Preview</h3>'
    publishBtn.disabled = false;
  }
}
