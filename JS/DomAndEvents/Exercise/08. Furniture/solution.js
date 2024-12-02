function solve() {
  const inputField = document.querySelector('textarea');
  const generateBtn = document.querySelector('button');
  const tableContent = document.querySelector('table tbody');
  const buyBtn = document.querySelector('button:last-child');
  const outputField = document.querySelectorAll('textarea')[1];

  generateBtn.addEventListener('click', addProduct);
  buyBtn.addEventListener('click', buyProducts);

  function createChildImg(obj, parentEl) {
    newTd = document.createElement('td');
    newImg = document.createElement('img');
    newImg.src = obj['img'];
    newTd.appendChild(newImg);
    parentEl.appendChild(newTd);
  }

  function createChildP(obj, pContent, parentEl) {
    newTd = document.createElement('td');
    newP = document.createElement('p');
    newP.textContent = obj[pContent]
    newTd.appendChild(newP);
    parentEl.appendChild(newTd);
  }

  function createChildChkBox(parentEl) {
    newTd = document.createElement('td');
    newChkBox = document.createElement('input');
    newChkBox.setAttribute('type', 'checkbox');
    newTd.appendChild(newChkBox);
    parentEl.appendChild(newTd);
  }

  function addProduct() {
    if (inputField) {
      let arrOfObjects = JSON.parse(inputField.value);
      Object.values(arrOfObjects).forEach(newProduct => {
        const newTr = document.createElement('tr');
        createChildImg(newProduct, newTr);
        createChildP(newProduct, 'name', newTr);
        createChildP(newProduct, 'price', newTr);
        createChildP(newProduct, 'decFactor', newTr);
        createChildChkBox(newTr);
        tableContent.appendChild(newTr);
      });
    }
  }

  function buyProducts() {
    let boughtProducts = [];
    let totalPrice = 0;
    let totalDecFactor = 0;
    let count = 0;
    const chkBoxes = Array.from(document.querySelectorAll('input[type="checkbox"]'))
      .filter(c => c.checked === true);

    chkBoxes.forEach(chkBox => {
      let details = Array.from(chkBox.parentElement.parentElement.children).slice(1, -1);
      boughtProducts.push(details[0].textContent.trim());
      totalPrice += Number(details[1].textContent);
      totalDecFactor += Number(details[2].textContent);
      count++;
    });

    let averageDecFactor = totalDecFactor / count;
    outputField.value = `Bought furniture: ${boughtProducts.join(', ')}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${averageDecFactor}`;
  }
}