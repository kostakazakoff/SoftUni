function solve() {
  const inputField = document.querySelector('textarea');
  const generateBtn = document.querySelector('button');
  const tableContent = document.querySelector('table tbody');
  const buyBtn = document.querySelector('button:last-child');
  const outputField = document.querySelectorAll('textarea')[1];

  generateBtn.addEventListener('click', addProduct);
  buyBtn.addEventListener('click', buyProducts);

  function addProduct() {
    if (inputField) {
      let arrOfObjects = JSON.parse(inputField.value);
      Object.values(arrOfObjects).forEach(newProduct => {
        console.log(newProduct)
        
        let newChild = `
        <tr>
            <td>
                <img src="${newProduct['image']}">
            </td>
            <td>
                <p>${newProduct['name']}</p>
            </td>
            <td>
                <p>${newProduct['price']}</p>
            </td>
            <td>
                <p>${newProduct['decFactor']}</p>
            </td>
            <td>
                <input type="checkbox" />
            </td>
        </tr>
        `;

        tableContent.innerHTML += newChild;
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