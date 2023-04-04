window.addEventListener("load", solve);

function solve() {
  const form = document.querySelector('form');
  const publishTableBody = document.getElementById('table-body');
  const totalProfitField = document.getElementById('profit');
  const carsList = document.getElementById('cars-list');

  const make = document.getElementById('make');
  const model = document.getElementById('model');
  const year = document.getElementById('year');
  const fuel = document.getElementById('fuel');
  const price = document.getElementById('original-cost');
  const sellPrice = document.getElementById('selling-price');

  const publishBtn = document.getElementById('publish');

  let totalProfit = 0;

  publishBtn.addEventListener('click', publish);

  function publish(e) {
    e.preventDefault();

    const validSellPrice = parseInt(sellPrice.value) > parseInt(price.value);
    const validInput = [make, model, year, fuel, price, sellPrice].every(field => field.value.length > 0);

    if (!validInput || !validSellPrice) {
      return;
    }

    const tr = createHTMLElement('tr', publishTableBody, null, ['row']);
    createHTMLElement('td', tr, make.value);
    createHTMLElement('td', tr, model.value);
    createHTMLElement('td', tr, year.value);
    createHTMLElement('td', tr, fuel.value);
    createHTMLElement('td', tr, price.value);
    createHTMLElement('td', tr, sellPrice.value);
    const td = createHTMLElement('td', tr);
    const editBtn = createHTMLElement('button', td, 'Edit', ['action-btn', 'edit']);
    const sellBtn = createHTMLElement('button', td, 'Sell', ['action-btn', 'sell']);

    form.reset();

    editBtn.addEventListener('click', edit);
    sellBtn.addEventListener('click', sell);
  }

  function edit() {
    make.value = this.parentNode.parentNode.querySelector('td:nth-child(1)').textContent;
    model.value = this.parentNode.parentNode.querySelector('td:nth-child(2)').textContent;
    year.value = this.parentNode.parentNode.querySelector('td:nth-child(3)').textContent;
    fuel.value = this.parentNode.parentNode.querySelector('td:nth-child(4)').textContent;
    price.value = this.parentNode.parentNode.querySelector('td:nth-child(5)').textContent;
    sellPrice.value = this.parentNode.parentNode.querySelector('td:nth-child(6)').textContent;


    this.parentNode.parentNode.remove();
  }

  function sell() {
    const _make = this.parentNode.parentNode.querySelector('td:nth-child(1)').textContent;
    const _model = this.parentNode.parentNode.querySelector('td:nth-child(2)').textContent;
    const _year = this.parentNode.parentNode.querySelector('td:nth-child(3)').textContent;
    const _price = parseInt(this.parentNode.parentNode.querySelector('td:nth-child(5)').textContent);
    const _sellPrice = parseInt(this.parentNode.parentNode.querySelector('td:nth-child(6)').textContent);
    
    const profit = _sellPrice - _price;

    const li = createHTMLElement('li', carsList, null, ['each-list']);
    createHTMLElement('span', li, `${_make} ${_model}`);
    createHTMLElement('span', li, _year);
    createHTMLElement('span', li, profit);

    totalProfit += profit;
    totalProfitField.textContent = totalProfit.toFixed(2);

    this.parentNode.parentNode.remove();
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