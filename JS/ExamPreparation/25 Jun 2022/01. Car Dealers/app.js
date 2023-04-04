window.addEventListener("load", solve);

function solve() {
  const form = document.querySelector('form');
  const publishTableBody = document.getElementById('table-body');
  const totalProfitField = document.getElementById('profit');
  const carsList = document.getElementById('cars-list');
  const inputDOMSelectors = {
    make: document.getElementById('make'),
    model: document.getElementById('model'),
    year: document.getElementById('year'),
    fuel: document.getElementById('fuel'),
    price: document.getElementById('original-cost'),
    sellPrice: document.getElementById('selling-price')
  };
  const publishBtn = document.getElementById('publish');

  let casch = {};
  let totalProfit = 0;

  publishBtn.addEventListener('click', publish);

  function publish(e) {
    e.preventDefault();

    const validSellPrice = parseFloat(inputDOMSelectors.sellPrice.value) >= parseFloat(inputDOMSelectors.price.value);
    const validInput = Object.values(inputDOMSelectors).every(f => f.value.trim().length > 0);

    if (!validInput || !validSellPrice) {
      return;
    }

    const { make, model, year, fuel, price, sellPrice } = inputDOMSelectors;
    casch[inputDOMSelectors.make.value] = {
      make: make.value,
      model: model.value,
      year: year.value,
      fuel: fuel.value,
      price: price.value,
      sellPrice: sellPrice.value
    }

    const tr = createHTMLElement('tr', publishTableBody, null, ['row']);
    createHTMLElement('td', tr, inputDOMSelectors.make.value);
    createHTMLElement('td', tr, inputDOMSelectors.model.value);
    createHTMLElement('td', tr, inputDOMSelectors.year.value);
    createHTMLElement('td', tr, inputDOMSelectors.fuel.value);
    createHTMLElement('td', tr, inputDOMSelectors.price.value);
    createHTMLElement('td', tr, inputDOMSelectors.sellPrice.value);
    const td = createHTMLElement('td', tr);
    const editBtn = createHTMLElement('button', td, 'Edit', ['action-btn', 'edit']);
    const sellBtn = createHTMLElement('button', td, 'Sell', ['action-btn', 'sell']);

    form.reset();

    editBtn.addEventListener('click', edit);
    sellBtn.addEventListener('click', sell);
  }

  function edit() {
    const car = this.parentNode.parentNode.querySelector('td:nth-child(1)').textContent;
    for (const key in casch[car]) {
      inputDOMSelectors[key].value = casch[car][key];
    }
    this.parentNode.parentNode.remove();
  }

  function sell() {
    const car = this.parentNode.parentNode.querySelector('td:nth-child(1)').textContent;

    const make = casch[car].make;
    const model = casch[car].model;
    const year = casch[car].year;
    const price = casch[car].price;
    const sellPrice = casch[car].sellPrice;
    const profit = sellPrice - price;

    const li = createHTMLElement('li', carsList, null, ['each-list']);
    createHTMLElement('span', li, `${make} ${model}`);
    createHTMLElement('span', li, year);
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
