function attachEvents() {
    const btnLoadPosts = document.getElementById('btnLoadPosts');
    const btnViewPosts = document.getElementById('btnViewPost');
    const menu = document.getElementById('posts');
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const postComments = document.getElementById('post-comments');
    let caschedPosts = {};
    let caschedPostComments = {};
    let firstLoad = false;

    const POSTS_URL = 'http://localhost:3030/jsonstore/blog/posts/'
    const POSTS_COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments/'

    btnLoadPosts.addEventListener('click', () => loadPosts())
    btnViewPosts.addEventListener('click', () => handlePost())

    function loadPosts() {
        firstLoad = true;
        while (menu.firstChild) { menu.removeChild(menu.lastChild) };
        fetch(POSTS_URL)
            .then(res => res.json())
            .then((posts) => { caschedPosts = posts; createMenu() })
            .catch(err => console.error(err));
        fetch(`${POSTS_COMMENTS_URL}`)
            .then(res => res.json())
            .then(data => caschedPostComments = data)
            .catch(err => console.log(err));
    }

    function createMenu() {
        Object.values(caschedPosts).forEach(post => {
            const option = document.createElement('option');
            option.value = post.id
            option.textContent = post.title
            menu.appendChild(option);
        })
        if (firstLoad) { firstLoad = false; handlePost() }
    }

    function handlePost() {
        let id = menu.value
        postTitle.textContent = caschedPosts[id]['title'];
        postBody.textContent = caschedPosts[id]['body'];
        postComments.textContent = '';

        Object.values(caschedPostComments).forEach(post => {
            if (post.postId === id) {
                let li = document.createElement('li');
                li.id = post.id;
                li.textContent = post['text'];
                postComments.appendChild(li)
            }
        })
    }
}

attachEvents();