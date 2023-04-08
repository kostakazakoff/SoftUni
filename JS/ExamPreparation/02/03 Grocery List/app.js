function grocery() {
    let productToUpdateId = null;
    const inputForm = document.querySelector('.list');
    const productsTableTbody = document.getElementById('tbody');
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/'
    const productInputFields = {
        'product': document.getElementById('product'),
        'count': document.getElementById('count'),
        'price': document.getElementById('price')
    }
    const productInputBtns = {
        'addProductBtn': document.getElementById('add-product'),
        'updateProductBtn': document.getElementById('update-product'),
        'loadAllProductsBtn': document.getElementById('load-product')
    }

    productInputBtns.loadAllProductsBtn.addEventListener('click', loadAllProducts);
    productInputBtns.addProductBtn.addEventListener('click', addProduct);
    productInputBtns.updateProductBtn.addEventListener('click', updateProduct);

    function loadAllProducts(e) {
        e?.preventDefault();

        fetch(BASE_URL)
            .then(res => res.json())
            .then(data => addProductsToTable(data))
            .catch(err => console.error(err));
    }

    function addProductsToTable(allProducts) {
        productsTableTbody.innerHTML = '';

        Object.values(allProducts).forEach(p => {
            const tr = createHTMLElement('tr', productsTableTbody, null, null, p._id);
            createHTMLElement('td', tr, p.product, ['name']);
            createHTMLElement('td', tr, p.count, ['count-product']);
            createHTMLElement('td', tr, p.price, ['product-price']);
            const pBtns = createHTMLElement('td', tr, null, ['btn']);
            const updateBtn = createHTMLElement('button', pBtns, 'Update', ['update']);
            const deleteBtn = createHTMLElement('button', pBtns, 'Delete', ['delete']);

            updateBtn.addEventListener('click', prepareProductToUpdate);
            deleteBtn.addEventListener('click', deleteProduct);
        })
    }

    function addProduct(e) {
        e?.preventDefault();

        const [product, count, price] = Object.values(productInputFields).map(tag => tag.value)
        const newProduct = { product, count, price }

        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newProduct)
        })
            .then(() => { inputForm.reset(); loadAllProducts() })
            .catch(err => console.error(err));
    }

    function updateProduct(e) {
        e?.preventDefault();

        const [product, count, price] = Object.values(productInputFields).map(tag => tag.value)
        const editedProduct = { product, count, price };

        fetch(`${BASE_URL}${productToUpdateId}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(editedProduct)
        })
            .then(() => {
                inputForm.reset();
                productInputBtns.addProductBtn.disabled = false;
                productInputBtns.updateProductBtn.disabled = true;
                loadAllProducts()
            })
            .catch(err => console.error(err));
    }

    function prepareProductToUpdate() {
        const [product, count, price] = Array
            .from(this.parentNode.parentNode.querySelectorAll('td'))
            .map(tag => tag.textContent);

        productInputFields.product.value = product;
        productInputFields.count.value = count;
        productInputFields.price.value = price;

        productToUpdateId = this.parentNode.parentNode.id;

        productInputBtns.addProductBtn.disabled = true;
        productInputBtns.updateProductBtn.disabled = false;
    }

    function deleteProduct() {
        const id = this.parentNode.parentNode.id;
        fetch(`${BASE_URL}${id}`, {
            method: 'DELETE',
        })
            .then(() => loadAllProducts())
            .catch((err) => console.error(err));
    }

    function createHTMLElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);

        if (content && useInnerHtml) {
            htmlElement.innerHTML = content;
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content;
            }

            if (content && type === 'input') {
                htmlElement.value = content;
            }
        }

        if (classes && classes.length > 0) {
            htmlElement.classList.add(...classes);
        }

        if (id) {
            htmlElement.id = id;
        }

        // { src: 'link', href: 'http' }
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key])
            }
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;
    }
}

grocery()