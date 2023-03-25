function attachEvents() {
    const btnLoadPosts = document.getElementById('btnLoadPosts');
    const btnViewPosts = document.getElementById('btnViewPost');
    const menu = document.getElementById('posts');
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const postComments = document.getElementById('post-comments');

    const POSTS_URL = 'http://localhost:3030/jsonstore/blog/posts/'
    const POSTS_COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments/'

    btnLoadPosts.addEventListener('click', () => loadPosts())

    btnViewPosts.addEventListener('click', () => {
        fetch(`${POSTS_URL}${menu.value}`)
            .then(res => res.json())
            .then(post => handlePost(post))
            .catch(err => console.log(err));
    })

    function loadPosts() {
        fetch(POSTS_URL)
            .then(res => res.json())
            .then(posts => createMenu(posts))
            .catch(err => console.error(err));
    }

    function createMenu(posts) {
        Object.values(posts).forEach(post => {
            const option = document.createElement('option');
            option.value = post.id
            option.textContent = post.title
            menu.appendChild(option);
        })
    }

    function handlePost(post) {
        postTitle.textContent = post.title;
        postBody.textContent = post.body;
        postComments.textContent = ''
        fetch(`${POSTS_COMMENTS_URL}`)
            .then(res => res.json())
            .then(info => {
                Object.values(info).forEach(comment => {
                    if (comment.postId === post.id) {
                        let li = document.createElement('li');
                        li.id = comment.id;
                        li.textContent = comment.text;
                        postComments.appendChild(li)
                    }
                })
            })
            .catch(err => console.log(err));
    }
}

attachEvents();