window.addEventListener("load", solve);

function solve() {
  const fName = document.getElementById('first-name');
  const lName = document.getElementById('last-name');
  const age = document.getElementById('age');
  const title = document.getElementById('story-title');
  const storyText = document.getElementById('story');
  const genre = document.getElementById('genre');
  const publishBtn = document.getElementById('form-btn');
  const publishedStoryUl = document.getElementById('preview-list');

  function publishStory() {

    const li = document.createElement('li');
    li.className = 'story-info';

    li.innerHTML = `
    <article>
    <h4>Name: ${fName.value} ${lName.value}</h4>
    <p>Age: ${age.value}</p>
    <p>Title: ${title.value}</p>
    <p>Genre: ${genre.value}</p>
    <p>${storyText.value}</p>
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
    const pubFullName = document.querySelector('article :nth-child(1)');
    const pubAge = document.querySelector('article :nth-child(2)');
    const pubTitle = document.querySelector('article :nth-child(3)');
    const pubGenre = document.querySelector('article :nth-child(4)');
    const pubStory = document.querySelector('article :nth-child(5)');

    [fName.value, lName.value] = pubFullName.textContent.split(' ').slice(1);
    age.value = pubAge.textContent.split(' ')[1];
    title.value = pubTitle.textContent.split(' ')[1];
    storyText.value = pubStory.textContent;
    genre.value = pubGenre.textContent.split(' ')[1];

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
    publishedStoryUl.remove(this.parentNode);
    publishBtn.disabled = false;
  }
}