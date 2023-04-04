window.addEventListener("load", solve);

function solve() {
  const form = document.querySelector('form');
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

  publishBtn.addEventListener('click', publish);

  function publish(e) {
    if (e) { e.preventDefault() }

    const validSellPrice = inputDOMSelectors.sellPrice.value >= inputDOMSelectors.price.value;
    const validInput = Object.values(inputDOMSelectors).every(f => f.value.length > 0);

    if (!validInput || !validSellPrice) {
      return;
    }

    const { make, model, year, fuel, price, sellPrice } = inputDOMSelectors;
    casch = {
      make: make.value,
      model: model.value,
      year: year.value,
      fuel: fuel.value,
      price: price.value,
      sellPrice: sellPrice.value
    }

    
  }
}
